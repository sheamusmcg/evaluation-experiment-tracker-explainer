import streamlit as st

from components.app_data import SAMPLE_RUNS, TRACKING_TOOLS
from components.ui_helpers import render_navigation, render_page_header


render_page_header(4)

st.header("What Gets Tracked")
st.write(
    "The deck contrasts guessing from memory with engineering discipline. A tracker records "
    "what changed, what happened, and which artifacts prove it."
)

st.subheader("Tools Mentioned in the Deck")
st.dataframe(TRACKING_TOOLS, hide_index=True, use_container_width=True)

st.subheader("Example Runs")
st.dataframe(SAMPLE_RUNS, hide_index=True, use_container_width=True)

st.header("Try It: Pick a Winning Run")
priority = st.radio(
    "Optimization goal",
    ["Highest quality", "Best quality under 3 seconds", "Lowest cost with acceptable quality"],
    horizontal=True,
)

if priority == "Highest quality":
    candidates = SAMPLE_RUNS
    winner = max(candidates, key=lambda row: row["Quality"])
elif priority == "Best quality under 3 seconds":
    candidates = [row for row in SAMPLE_RUNS if row["Latency sec"] <= 3]
    winner = max(candidates, key=lambda row: row["Quality"])
else:
    candidates = [row for row in SAMPLE_RUNS if row["Quality"] >= 0.80]
    winner = min(candidates, key=lambda row: row["Cost cents"])

st.success(f"Recommended run: {winner['Run']} - {winner['Notes']}")

with st.expander("Why this matters", expanded=True):
    st.write(
        "A run is not just a score. It is a bundle of parameters, metrics, artifacts, and notes. "
        "That bundle lets you compare tradeoffs instead of relying on whichever result you remember."
    )

render_navigation(4)
