import streamlit as st

def initialize_states():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "selected_suggestion" not in st.session_state:
        st.session_state.selected_suggestion = None

    if "temp_user_input" not in st.session_state:
        st.session_state.temp_user_input = None

    if "user_input" not in st.session_state:
        st.session_state.user_input = None
    
    if "is_processing_answer" not in st.session_state:
        st.session_state.is_processing_answer = False

def get_user_prompt():
    st.session_state.is_processing_answer = False
    prompt_sources = ["selected_suggestion", "temp_user_input", "user_input"]

    for key in prompt_sources:
        value = st.session_state.get(key)
        if value:
            st.session_state.is_processing_answer = True
            st.session_state[key] = None
            return value

    return None
