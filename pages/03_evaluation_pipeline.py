import streamlit as st

from components.app_data import PIPELINE_STEPS
from components.ui_helpers import render_navigation, render_page_header


COMPONENT_SCORECARD = [
    {
        "Component": "Retriever",
        "Question": "Did we fetch the right source chunks?",
        "Example metric": "Context relevance",
        "Pass signal": "Top chunks contain the policy paragraph",
    },
    {
        "Component": "Prompt",
        "Question": "Did the prompt ask for the behavior we want?",
        "Example metric": "Instruction coverage",
        "Pass signal": "Prompt requires grounded answer and citation",
    },
    {
        "Component": "Model output",
        "Question": "Did the final answer satisfy the rubric?",
        "Example metric": "Faithfulness and completeness",
        "Pass signal": "Answer matches source and says when unsure",
    },
]


FAILURE_CASES = {
    "Retriever missed the source": {
        "symptom": "The final answer says employees get 20 PTO days, but the current policy says 15.",
        "component": "Retriever",
        "evidence": "The retrieved chunks came from an old benefits overview instead of the current PTO policy.",
        "next_test": "Add examples where old and current policy documents disagree.",
        "fix": "Improve retrieval filters, freshness ranking, or metadata constraints.",
    },
    "Prompt allowed guessing": {
        "symptom": "The right policy chunk was retrieved, but the answer adds a made-up exception.",
        "component": "Prompt",
        "evidence": "The prompt did not say to answer only from retrieved context or to admit missing information.",
        "next_test": "Score whether answers stay within context and include uncertainty when context is incomplete.",
        "fix": "Add grounding instructions, citation requirements, and a refusal path for missing evidence.",
    },
    "Output ignored the rubric": {
        "symptom": "Retrieval and prompt look good, but the final answer omits the required citation.",
        "component": "Model output",
        "evidence": "The response is factually correct but fails the output format requirement.",
        "next_test": "Add exact checks for citation format plus a rubric score for completeness.",
        "fix": "Tighten output schema, add examples, or post-process for required fields.",
    },
}


render_page_header(3)

st.header("Three-Step Pipeline")

cols = st.columns(3)
for col, step in zip(cols, PIPELINE_STEPS):
    with col:
        st.subheader(f"{step['step']} {step['name']}")
        st.write(step["summary"])

st.header("Practical Example: Debug a RAG Evaluation")
st.write(
    "Suppose a RAG assistant answers a benefits-policy question incorrectly. An end-to-end "
    "score only tells you the answer failed. A component-level eval tells you where to look."
)

with st.expander("Eval case", expanded=True):
    st.markdown("**User question:** How many PTO days do full-time employees get?")
    st.markdown("**Expected source:** Current PTO policy, updated this year.")
    st.markdown("**Expected answer:** Full-time employees receive 15 PTO days, with a citation to the current policy.")

st.subheader("Component scorecard")
st.dataframe(COMPONENT_SCORECARD, hide_index=True, use_container_width=True)

failure = st.selectbox("Choose the failure you discovered", list(FAILURE_CASES.keys()))
case = FAILURE_CASES[failure]

diag_col1, diag_col2 = st.columns(2)
with diag_col1:
    st.subheader("Symptom")
    st.write(case["symptom"])
    st.subheader("Likely failing component")
    st.success(case["component"])
with diag_col2:
    st.subheader("Evidence")
    st.write(case["evidence"])
    st.subheader("Next eval to add")
    st.write(case["next_test"])

with st.expander("What you would fix"):
    st.write(case["fix"])

with st.expander("What this example teaches", expanded=True):
    st.write(
        "A poor final answer does not automatically mean the model is bad. The retriever may "
        "have found the wrong context, the prompt may have allowed guessing, or the output may "
        "have ignored a formatting rule. Component evals keep those problems separate."
    )

st.header("Try It: Build a Small Eval Plan")
system_name = st.text_input("System or feature being evaluated", "RAG answer generator")
component = st.selectbox(
    "Which component are you testing first?",
    ["Retriever", "Prompt", "Model output", "Post-processing", "End-to-end flow"],
)
method = st.selectbox(
    "Evaluation method",
    ["Exact check", "Rubric score", "Human review", "Model judge", "Hybrid"],
)
failure_mode = st.text_input("Failure mode to add to the eval set", "Answer cites an irrelevant document")

st.subheader("Draft plan")
st.write(f"Evaluate **{component}** for **{system_name}** using **{method}**.")
st.write(f"Add examples that catch this failure mode: **{failure_mode}**.")

with st.expander("What to log for this eval"):
    st.markdown("- Input example")
    st.markdown("- Expected behavior")
    st.markdown("- Actual output")
    st.markdown("- Score or pass/fail result")
    st.markdown("- Notes about why the result passed or failed")

render_navigation(3)
