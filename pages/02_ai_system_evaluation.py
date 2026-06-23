import streamlit as st

from components.app_data import AI_EVAL_DIMENSIONS
from components.ui_helpers import render_navigation, render_page_header


RESPONSE_EXAMPLE = {
    "user_question": "Can I return opened headphones after 45 days?",
    "policy": (
        "Store policy: unopened electronics can be returned within 30 days. "
        "Opened electronics are not returnable unless defective. Defective items can be exchanged "
        "within one year with proof of purchase."
    ),
    "responses": [
        {
            "name": "Response A",
            "text": (
                "Yes. Since it has only been 45 days, you should still be able to return the "
                "headphones. Bring your receipt and the store can process the refund."
            ),
            "scores": {
                "Domain accuracy": 2,
                "Generation quality": 4,
                "Instruction following": 4,
                "Cost and latency": 5,
            },
            "note": "Fluent and fast, but it invents a return option that the policy does not allow.",
        },
        {
            "name": "Response B",
            "text": (
                "Opened headphones usually cannot be returned after 45 days. If they are defective "
                "and you have proof of purchase, you may be able to exchange them within one year."
            ),
            "scores": {
                "Domain accuracy": 5,
                "Generation quality": 4,
                "Instruction following": 5,
                "Cost and latency": 3,
            },
            "note": "More grounded in the policy, though it may be slower or cost more if it uses retrieval.",
        },
    ],
}


def weighted_score(scores, weights):
    """Calculate a weighted score out of 5."""
    total_weight = sum(weights.values())
    if total_weight == 0:
        return 0
    return sum(scores[name] * weight for name, weight in weights.items()) / total_weight


render_page_header(2)

st.header("Four Production Evaluation Dimensions")

cols = st.columns(2)
for index, dimension in enumerate(AI_EVAL_DIMENSIONS):
    with cols[index % 2]:
        st.subheader(dimension["name"])
        for question in dimension["questions"]:
            st.markdown(f"- {question}")

st.header("Practical Example: Score Two AI Responses")
st.write(
    "Here is a small customer-support evaluation. Notice that the smoother answer is not "
    "necessarily the better answer."
)

with st.expander("Policy and user question", expanded=True):
    st.markdown(f"**Policy:** {RESPONSE_EXAMPLE['policy']}")
    st.markdown(f"**User question:** {RESPONSE_EXAMPLE['user_question']}")

response_cols = st.columns(2)
for response, col in zip(RESPONSE_EXAMPLE["responses"], response_cols):
    with col:
        st.subheader(response["name"])
        st.write(response["text"])
        st.caption(response["note"])

st.subheader("Adjust the importance of each dimension")
weight_cols = st.columns(4)
weights = {}
for dimension, col in zip(
    ["Domain accuracy", "Generation quality", "Instruction following", "Cost and latency"],
    weight_cols,
):
    with col:
        weights[dimension] = st.slider(dimension, 0, 5, 3, key=f"weight_{dimension}")

score_rows = []
for response in RESPONSE_EXAMPLE["responses"]:
    row = {"Response": response["name"]}
    row.update(response["scores"])
    row["Weighted score"] = round(weighted_score(response["scores"], weights), 2)
    score_rows.append(row)

st.dataframe(score_rows, hide_index=True, use_container_width=True)
winner = max(score_rows, key=lambda row: row["Weighted score"])
st.success(f"Current winner by your weights: {winner['Response']}")

with st.expander("What this example teaches", expanded=True):
    st.write(
        "Response A sounds confident, but it fails the domain policy. Response B is less broad, "
        "but it is grounded in the actual rule. This is why AI evaluation separates domain "
        "capability, generation quality, instruction following, and cost/latency instead of "
        "collapsing everything into 'which answer sounds better?'"
    )

st.header("Try It: Draft an Evaluation Rubric")
use_case = st.selectbox(
    "Choose an AI application",
    ["Customer support assistant", "RAG research assistant", "JSON extraction tool"],
)

rubrics = {
    "Customer support assistant": [
        "Domain answer is correct for the customer policy.",
        "Tone is helpful and concise.",
        "The response does not invent policy details.",
        "The answer includes a clear next step.",
    ],
    "RAG research assistant": [
        "Answer uses retrieved context instead of unsupported claims.",
        "Citations match the answer content.",
        "The answer identifies uncertainty when context is incomplete.",
        "The response is organized for quick review.",
    ],
    "JSON extraction tool": [
        "Output is valid JSON.",
        "Required fields are present.",
        "Values match the source text.",
        "No extra commentary appears outside the JSON object.",
    ],
}

st.subheader("Starter rubric")
for item in rubrics[use_case]:
    st.checkbox(item, value=True)

with st.expander("Middle-ground lesson takeaway", expanded=True):
    st.write(
        "A rubric should be concrete enough that two reviewers would mostly agree. Avoid vague "
        "phrases like 'good answer' unless you define examples of good, bad, and borderline."
    )

render_navigation(2)
