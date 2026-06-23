import streamlit as st

from components.app_data import PIPELINE_STEPS
from components.ui_helpers import render_navigation, render_page_header


render_page_header(3)

st.header("Three-Step Pipeline")

cols = st.columns(3)
for col, step in zip(cols, PIPELINE_STEPS):
    with col:
        st.subheader(f"{step['step']} {step['name']}")
        st.write(step["summary"])

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
