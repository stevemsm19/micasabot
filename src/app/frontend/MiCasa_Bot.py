import streamlit as st

from app.frontend.components.sidebar import handle_sidebar
from app.frontend.components.chat.chat_state import initialize_states, get_user_prompt
from app.frontend.components.chat.chat_ui import handle_chat_flow

def setup_app():
    st.set_page_config("MiCasa Bot")
    st.title("MiCasa Bot 💬")

def main():
    setup_app()
    initialize_states()

    user_prompt = get_user_prompt()
    num_results, similarity_threshold = handle_sidebar()

    handle_chat_flow(user_prompt, num_results, similarity_threshold)

if __name__ == "__main__":
    main()
