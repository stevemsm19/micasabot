from typing import Optional
import streamlit as st

from app.frontend.features.chat.agent_response_handler import generate_agent_response
from app.frontend.features.chat.user_prompt_handler import add_user_prompt
from app.frontend.utils.constants.chat_suggestions import CHAT_SUGGESTIONS


def display_chat_intro() -> None:
    with st.container():
        st.chat_input(
            "Escribe tu pregunta aquí...",
            key="temp_user_input",
            disabled=getattr(st.session_state, "is_processing_answer", False),
        )

        selected_suggestion: Optional[str] = st.pills(
            label="Preguntas sugeridas",
            label_visibility="collapsed",
            options=CHAT_SUGGESTIONS,
            key="selected_suggestion",
        )

    if selected_suggestion:
        st.session_state.selected_suggestion = selected_suggestion


def display_chat_history() -> None:
    for message in getattr(st.session_state, "messages", []):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_chat_flow(
    user_prompt: Optional[str],
    num_results: int,
    similarity_threshold: float,
) -> None:
    if not user_prompt and not getattr(st.session_state, "messages", []):
        display_chat_intro()
        st.stop()

    display_chat_history()

    st.chat_input(
        "Escribe tu pregunta aquí...",
        key="user_input",
        disabled=getattr(st.session_state, "is_processing_answer", False),
    )

    if user_prompt:
        add_user_prompt(user_prompt)
        generate_agent_response(user_prompt, num_results, similarity_threshold)
