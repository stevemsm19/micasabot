import streamlit as st

from app.frontend.components.sidebar import upload_documents_sidebar, handle_upload_button, set_variables_sidebar
from app.frontend.components.chat import init_chat, display_chat_history, handle_user_input, generate_agent_response

def main():
    st.set_page_config("MiCasa Bot", page_icon="💬")
    st.title("MiCasa Bot 💬")

    documents = upload_documents_sidebar()
    handle_upload_button(documents)

    init_chat()
    display_chat_history()

    num_results, similarity_threshold = set_variables_sidebar()
    prompt = handle_user_input()

    if prompt:
        generate_agent_response(prompt, num_results, similarity_threshold)

if __name__ == "__main__":
    main()
