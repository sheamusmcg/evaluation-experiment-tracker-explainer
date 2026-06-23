import streamlit as st

from components.ui_helpers import init_state, render_navigation, render_page_header


init_state()
render_page_header(7)

st.header("Log a Run")

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

st.header("Run Table")
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

render_navigation(7)
