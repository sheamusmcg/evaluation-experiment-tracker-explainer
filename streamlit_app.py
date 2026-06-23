import streamlit as st

from components.ui_helpers import init_state


st.set_page_config(
    page_title="Evaluation and Experiment Tracker Explainer",
    page_icon=":material/analytics:",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_state()

pages = {
    "Evaluation": [
        st.Page("pages/01_evaluation_metrics.py", title="Evaluation Metrics", icon=":material/analytics:"),
        st.Page("pages/02_ai_system_evaluation.py", title="AI Eval Criteria", icon=":material/rule_settings:"),
        st.Page("pages/03_evaluation_pipeline.py", title="Eval Pipeline", icon=":material/schema:"),
    ],
    "Tracking": [
        st.Page("pages/04_experiment_tracking.py", title="Experiment Tracking", icon=":material/track_changes:"),
    ],
    "Production": [
        st.Page("pages/05_observability_architecture.py", title="Observability Architecture", icon=":material/hub:"),
        st.Page("pages/06_monitoring_vs_observability.py", title="Monitoring vs Observability", icon=":material/monitor_heart:"),
    ],
    "Lab": [
        st.Page("pages/07_tracker_lab.py", title="Tracker Lab", icon=":material/science:"),
    ],
}

page = st.navigation(pages)
page.run()
