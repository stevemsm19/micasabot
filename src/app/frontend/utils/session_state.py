import streamlit as st

def apply_session_states(defaults: dict):
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

def handle_page_change(current_page, reset_fn=None):
    if st.session_state.last_page != current_page:
        if reset_fn:
            reset_fn()
        st.session_state.last_page = current_page