import streamlit as st

from app.frontend.components.sidebar import upload_documents_sidebar, handle_upload_button, set_variables_sidebar
from app.frontend.components.chat import initialize_state, get_user_prompt, display_chat_history, generate_agent_response, display_chat_intro

def main():
    st.set_page_config("MiCasa Bot")
    st.title("MiCasa Bot 💬")

    initialize_state()

    documents = upload_documents_sidebar()
    handle_upload_button(documents)
    num_results, similarity_threshold = set_variables_sidebar()

    user_prompt = get_user_prompt()

    if not user_prompt and not st.session_state.messages:
        display_chat_intro()
        st.stop()

    display_chat_history()

    prompt_input = st.chat_input(
        "Escribe tu pregunta aquí...",
        key="user_input",
        disabled=st.session_state.is_processing,
    )

    st.session_state.is_processing = True

    if prompt_input:
        user_prompt = prompt_input

    if user_prompt:
        generate_agent_response(user_prompt, num_results, similarity_threshold)


if __name__ == "__main__":
    main()
