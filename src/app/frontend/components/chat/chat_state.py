import streamlit as st

def initialize_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "is_processing" not in st.session_state:
        st.session_state.is_processing = False

    if "selected_suggestion" not in st.session_state:
        st.session_state.selected_suggestion = None

    if "initial_question" not in st.session_state:
        st.session_state.initial_question = None

def get_user_prompt():
    prompt = None

    if st.session_state.selected_suggestion:
        st.session_state.is_processing = True
        prompt = st.session_state.selected_suggestion
        st.session_state.selected_suggestion = None

    elif st.session_state.initial_question:
        st.session_state.is_processing = True
        prompt = st.session_state.initial_question
        st.session_state.initial_question = None

    return prompt
