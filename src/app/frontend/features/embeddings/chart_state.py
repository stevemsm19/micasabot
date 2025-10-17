import streamlit as st
from app.frontend.utils.session_state import apply_session_states, handle_page_change


def reset_visualization_state() -> None:
    st.session_state.display_initial_chart = True
    st.session_state.regenerate_chart = False
    st.session_state.displaying_chart = False
    st.session_state.show_clusters = False
    st.session_state.show_anomalies = False


def init_visualization_state() -> None:
    defaults = {
        "display_initial_chart": True,
        "regenerate_chart": False,
        "displaying_chart": False,
        "show_clusters": False,
        "show_anomalies": False,
    }
    apply_session_states(defaults)


def setup_page_state() -> None:
    handle_page_change("visualization", reset_visualization_state)
