import streamlit as st

from components.app_data import SAMPLE_RUNS, TRACKING_TOOLS
from components.ui_helpers import render_navigation, render_page_header


RUN_RECORD_FIELDS = [
    {
        "Field": "Run name",
        "Example": "rag_prompt_v2_top5",
        "Why it matters": "Gives the experiment a human-readable identity.",
    },
    {
        "Field": "Parameters",
        "Example": "model=balanced, top_k=5, temperature=0.2",
        "Why it matters": "Shows what changed between runs.",
    },
    {
        "Field": "Metrics",
        "Example": "quality=0.86, latency=2.3s, cost=1.2 cents",
        "Why it matters": "Makes tradeoffs visible.",
    },
    {
        "Field": "Artifacts",
        "Example": "eval_results.csv, prompt.txt, sample_outputs.json",
        "Why it matters": "Keeps evidence attached to the run.",
    },
    {
        "Field": "Notes",
        "Example": "Better grounded answers, one citation miss remains.",
        "Why it matters": "Captures judgment that numbers do not fully explain.",
    },
]


EXPERIMENT_LOG = [
    {
        "Run": "baseline",
        "Change": "Original prompt, top_k=3",
        "Quality": 0.72,
        "Latency sec": 1.1,
        "Cost cents": 0.4,
        "Decision": "Keep as fallback",
        "Reason": "Fast and cheap, but misses policy details.",
    },
    {
        "Run": "prompt_v2",
        "Change": "Added rubric and citation instruction",
        "Quality": 0.81,
        "Latency sec": 1.4,
        "Cost cents": 0.5,
        "Decision": "Continue",
        "Reason": "Better answer structure with little added cost.",
    },
    {
        "Run": "prompt_v2_top5",
        "Change": "Raised retrieval from top_k=3 to top_k=5",
        "Quality": 0.86,
        "Latency sec": 2.3,
        "Cost cents": 1.2,
        "Decision": "Candidate",
        "Reason": "Best balance of quality, latency, and cost.",
    },
    {
        "Run": "large_model_top8",
        "Change": "Large model with top_k=8",
        "Quality": 0.91,
        "Latency sec": 4.8,
        "Cost cents": 4.6,
        "Decision": "Reject for now",
        "Reason": "Quality improved, but not enough to justify cost and latency.",
    },
]


render_page_header(4)

st.header("What Gets Tracked")
st.write(
    "The deck contrasts guessing from memory with engineering discipline. A tracker records "
    "what changed, what happened, and which artifacts prove it."
)

st.subheader("Tools Mentioned in the Deck")
st.dataframe(TRACKING_TOOLS, hide_index=True, use_container_width=True)

st.header("Practical Example: Anatomy of a Tracked Run")
st.write(
    "A tracker is useful because it keeps the experiment setup, the outcome, and the evidence "
    "in one place. If you cannot reconstruct the run later, you did not really track it."
)
st.dataframe(RUN_RECORD_FIELDS, hide_index=True, use_container_width=True)

with st.expander("Example run note", expanded=True):
    st.code(
        """Run: prompt_v2_top5
Parameters:
  model: balanced
  prompt_version: v2_rubric_guided
  retrieval_top_k: 5
  temperature: 0.2
Metrics:
  quality: 0.86
  latency_seconds: 2.3
  cost_cents: 1.2
Artifacts:
  prompt.txt
  eval_results.csv
  sample_outputs.json
Decision:
  Candidate for staging. Better grounded than baseline without large cost jump.""",
        language="yaml",
    )

st.subheader("Example Runs")
st.dataframe(SAMPLE_RUNS, hide_index=True, use_container_width=True)

st.header("Practical Example: Compare an Experiment History")
st.write(
    "This table tells the story of a small improvement cycle. Notice that the highest-quality "
    "run is not automatically the one you would deploy."
)
st.dataframe(EXPERIMENT_LOG, hide_index=True, use_container_width=True)

selected_run = st.selectbox("Inspect a run decision", [row["Run"] for row in EXPERIMENT_LOG], index=2)
selected = next(row for row in EXPERIMENT_LOG if row["Run"] == selected_run)
decision_col, reason_col = st.columns(2)
with decision_col:
    st.subheader("Decision")
    st.success(selected["Decision"])
with reason_col:
    st.subheader("Reason")
    st.write(selected["Reason"])

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
