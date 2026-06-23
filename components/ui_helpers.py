"""Reusable Streamlit UI helpers for the explainer app."""

from __future__ import annotations

import streamlit as st

from components.app_data import PAGES, SAMPLE_RUNS


def init_state():
    """Initialize app state."""
    if "tracker_runs" not in st.session_state:
        st.session_state.tracker_runs = [dict(run) for run in SAMPLE_RUNS]


def apply_global_styles():
    """Apply light visual refinements."""
    st.markdown(
        """
        <style>
        .lesson-meta {
            color: #5f6368;
            font-size: 0.95rem;
            margin-bottom: 0.75rem;
        }
        .quiet-note {
            color: #4b5563;
            font-size: 0.95rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_by_id(page_id: int) -> dict:
    """Return page metadata."""
    return next(page for page in PAGES if page["id"] == page_id)


def render_sidebar(current_page_id: int):
    """Render the page list in the sidebar."""
    with st.sidebar:
        st.header("Explainer Path")
        st.caption("Evaluation, tracking, and observability for AI engineering systems.")
        st.divider()
        for page in PAGES:
            label = page["short_title"]
            if page["id"] == current_page_id:
                label = f"{label} - current"
            st.page_link(page["page"], label=label, icon=page["icon"])


def render_page_header(page_id: int):
    """Render common page intro content."""
    page = page_by_id(page_id)
    apply_global_styles()
    render_sidebar(page_id)

    st.title(page["title"])
    st.markdown(
        f"<div class='lesson-meta'>Source: {page['deck_source']}</div>",
        unsafe_allow_html=True,
    )

    st.header("Lesson Brief")
    why_col, concept_col = st.columns(2)
    with why_col:
        st.subheader("Why this matters")
        st.write(page["why_it_matters"])
    with concept_col:
        st.subheader("Concept")
        st.write(page["concept"])

    with st.expander("Mental model", expanded=True):
        st.write(page["mental_model"])

    pitfall_col, practice_col = st.columns(2)
    with pitfall_col:
        with st.expander("Common pitfall", expanded=True):
            st.write(page["common_pitfall"])
    with practice_col:
        with st.expander("How this shows up in real work", expanded=True):
            st.write(page["real_work"])

    return page


def render_navigation(page_id: int):
    """Render previous and next links."""
    previous_page = page_by_id(page_id - 1) if page_id > 1 else None
    next_page = page_by_id(page_id + 1) if page_id < len(PAGES) else None

    st.divider()
    left, right = st.columns(2)
    with left:
        if previous_page:
            st.page_link(previous_page["page"], label=f"Back: {previous_page['short_title']}", icon=":material/arrow_back:")
    with right:
        if next_page:
            st.page_link(next_page["page"], label=f"Next: {next_page['short_title']}", icon=":material/arrow_forward:")
        else:
            st.success("End of the explainer path.")


def metric_card(label: str, value: str, note: str | None = None):
    """Render a compact metric display."""
    st.metric(label, value)
    if note:
        st.caption(note)
