import streamlit as st

from components.ui_helpers import init_state, render_navigation, render_page_header


init_state()
render_page_header(7)

st.info(
    "This is a simulated experiment tracker. It does not call a real model, send prompts to an API, "
    "store secrets, or measure live token usage. The numbers you enter are teaching values so you "
    "can practice the tracking workflow safely."
)

with st.expander("Why this lab does not ask for an API key", expanded=True):
    st.write(
        "Putting API keys into a teaching app is a poor default habit. In real projects, keys "
        "belong in environment variables, secret managers, or Streamlit secrets, not in regular "
        "text boxes. This lab focuses on the engineering discipline of tracking experiments "
        "without asking learners to expose credentials."
    )

st.header("Log a Simulated Run")

with st.form("run_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        run_name = st.text_input("Run name", f"Run {len(st.session_state.tracker_runs) + 1}")
        model = st.selectbox("Model", ["Fast model", "Balanced model", "Large model", "Custom model"])
    with col2:
        prompt = st.text_input("Prompt version", "v4 revised rubric")
        retrieval = st.selectbox("Retrieval setting", ["top_k=3", "top_k=5", "top_k=8", "none"])
    with col3:
        quality = st.slider("Quality score", 0.0, 1.0, 0.84, 0.01)
        latency = st.slider("Latency seconds", 0.1, 10.0, 2.5, 0.1)
        cost = st.slider("Cost cents", 0.1, 10.0, 1.4, 0.1)
    notes = st.text_area("Notes", "Improved formatting, still needs citation checks.")
    submitted = st.form_submit_button("Log run")

if submitted:
    st.session_state.tracker_runs.append(
        {
            "Run": run_name,
            "Model": model,
            "Prompt": prompt,
            "Retrieval": retrieval,
            "Quality": round(quality, 2),
            "Latency sec": round(latency, 1),
            "Cost cents": round(cost, 1),
            "Notes": notes,
        }
    )
    st.success(f"Logged {run_name}.")

st.header("Simulated Run Table")
st.dataframe(st.session_state.tracker_runs, hide_index=True, use_container_width=True)

st.header("Compare Runs")
objective = st.radio(
    "Decision rule",
    ["Maximize quality", "Quality per cent", "Quality per second"],
    horizontal=True,
)

runs = st.session_state.tracker_runs
if objective == "Maximize quality":
    best = max(runs, key=lambda row: row["Quality"])
elif objective == "Quality per cent":
    best = max(runs, key=lambda row: row["Quality"] / row["Cost cents"])
else:
    best = max(runs, key=lambda row: row["Quality"] / row["Latency sec"])

st.success(f"Current best by '{objective}': {best['Run']}")

with st.expander("What this lab is teaching", expanded=True):
    st.write(
        "The best run depends on the decision rule. Production AI engineering is often a tradeoff "
        "between quality, latency, cost, reliability, and operational complexity."
    )

st.header("Offline Practice: Run a Real Experiment Safely")
st.write(
    "Try this outside the app using any model interface you already have access to. Do not paste "
    "an API key here. The goal is to practice tracking, not credential handling."
)

st.subheader("Experiment prompt")
st.write(
    "Ask the same model to answer the same question three times, changing only the prompt style."
)

practice_rows = [
    {
        "Run": "A",
        "Change one thing": "Direct prompt",
        "Record": "Answer quality, latency you observed, notable mistakes",
    },
    {
        "Run": "B",
        "Change one thing": "Prompt with explicit rubric",
        "Record": "Whether the answer follows the rubric better",
    },
    {
        "Run": "C",
        "Change one thing": "Prompt with required output format",
        "Record": "Whether structure improves or content gets worse",
    },
]
st.dataframe(practice_rows, hide_index=True, use_container_width=True)

with st.expander("What to write down after the offline experiment", expanded=True):
    st.markdown("- The exact prompt version you used")
    st.markdown("- The response you received")
    st.markdown("- Your quality score and why you gave it")
    st.markdown("- Approximate latency if you observed it")
    st.markdown("- Any cost information the external tool already shows you")
    st.markdown("- Which run you would keep and what you would try next")

render_navigation(7)
