import streamlit as st

from app.frontend.utils.constants import CHAT_SUGGESTIONS

def display_chat_intro():
    with st.container():
        st.chat_input("Escribe tu pregunta aquí...", key="initial_question")

        selected_suggestion = st.pills(
            label="Preguntas sugeridas",
            label_visibility="collapsed",
            options=CHAT_SUGGESTIONS,
            key="selected_suggestion",
        )

    if selected_suggestion:
        st.session_state.selected_suggestion = selected_suggestion

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def add_user_message(prompt: str):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
