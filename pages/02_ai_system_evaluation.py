import streamlit as st

from components.app_data import AI_EVAL_DIMENSIONS
from components.ui_helpers import render_navigation, render_page_header


render_page_header(2)

st.header("Four Production Evaluation Dimensions")

cols = st.columns(2)
for index, dimension in enumerate(AI_EVAL_DIMENSIONS):
    with cols[index % 2]:
        st.subheader(dimension["name"])
        for question in dimension["questions"]:
            st.markdown(f"- {question}")

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
