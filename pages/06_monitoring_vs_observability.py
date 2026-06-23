import streamlit as st

from components.app_data import MONITORING_ITEMS, OBSERVABILITY_ITEMS, TRIAGE_SCENARIOS
from components.ui_helpers import render_navigation, render_page_header


render_page_header(6)

left, right = st.columns(2)
with left:
    st.header("Monitoring")
    st.write("Watching known metrics.")
    for item in MONITORING_ITEMS:
        st.markdown(f"- {item}")
with right:
    st.header("Observability")
    st.write("Understanding unknown failures.")
    for item in OBSERVABILITY_ITEMS:
        st.markdown(f"- {item}")

st.header("Try It: Incident Triage")
scenario = st.selectbox("Choose a symptom", list(TRIAGE_SCENARIOS.keys()))

st.subheader("Investigation path")
for step in TRIAGE_SCENARIOS[scenario]:
    st.markdown(f"- {step}")

with st.expander("Lesson takeaway", expanded=True):
    st.write(
        "Monitoring tells you that a metric crossed a threshold. Observability helps you follow "
        "one request across the system and discover which component actually caused the change."
    )

render_navigation(6)
