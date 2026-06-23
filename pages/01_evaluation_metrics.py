import streamlit as st

from components.app_data import METRIC_ROWS
from components.ui_helpers import metric_card, render_navigation, render_page_header


render_page_header(1)

st.header("Metrics You May Already Know")
st.write(
    "These metrics are useful because they compress many examples into a small signal. "
    "They become dangerous when the number is treated as complete proof that the system is ready."
)
st.dataframe(METRIC_ROWS, hide_index=True, use_container_width=True)

st.header("Try It: Confusion Matrix Tradeoffs")
st.write("Change the counts and watch how accuracy, precision, and recall move differently.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    tp = st.number_input("True positives", min_value=0, value=42)
with col2:
    fp = st.number_input("False positives", min_value=0, value=8)
with col3:
    fn = st.number_input("False negatives", min_value=0, value=15)
with col4:
    tn = st.number_input("True negatives", min_value=0, value=135)

total = tp + fp + fn + tn
accuracy = (tp + tn) / total if total else 0
precision = tp / (tp + fp) if tp + fp else 0
recall = tp / (tp + fn) if tp + fn else 0

m1, m2, m3 = st.columns(3)
with m1:
    metric_card("Accuracy", f"{accuracy:.1%}", "Overall correctness")
with m2:
    metric_card("Precision", f"{precision:.1%}", "How many predicted positives were right")
with m3:
    metric_card("Recall", f"{recall:.1%}", "How many real positives were found")

with st.expander("What this teaches", expanded=True):
    st.write(
        "Accuracy can look strong when the negative class is large. Precision and recall force "
        "you to ask which mistake is more expensive: false positives or false negatives. For AI "
        "systems, this same habit applies to hallucinations, format errors, latency, and cost."
    )

render_navigation(1)
