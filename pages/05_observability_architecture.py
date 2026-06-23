import streamlit as st

from components.app_data import ARCHITECTURE_LAYERS
from components.ui_helpers import render_navigation, render_page_header


render_page_header(5)

st.header("Five AI Engineering Layers")
st.dataframe(ARCHITECTURE_LAYERS, hide_index=True, use_container_width=True)

st.header("Try It: What Should You Watch?")
layer_name = st.selectbox("Choose a layer", [layer["layer"] for layer in ARCHITECTURE_LAYERS])
layer = next(item for item in ARCHITECTURE_LAYERS if item["layer"] == layer_name)

left, right = st.columns(2)
with left:
    st.subheader("Examples")
    st.write(layer["examples"])
with right:
    st.subheader("Signals to watch")
    st.write(layer["watch"])

with st.expander("Cross-layer observability", expanded=True):
    st.write(
        "Monitoring and observability sit across all layers. A useful trace should show the "
        "input, retrieval result, guardrail decision, model route, latency, cost, and final output."
    )

render_navigation(5)
