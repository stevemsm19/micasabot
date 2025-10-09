import streamlit as st

from app.frontend.features.chat.chat_sidebar import handle_sidebar
from app.frontend.features.chat.chat_state import init_chat_state
from app.frontend.features.chat.user_prompt_handler import get_user_prompt
from app.frontend.features.chat.chat_handler import handle_chat_flow
from app.frontend.utils.session_state import apply_session_states

def init_view_state():
    defaults = {
        "last_page": None,
    }
    apply_session_states(defaults)
    
def setup_app():
    st.set_page_config("MiCasa Bot")
    st.title("MiCasa Bot 💬")

    init_chat_state()
    init_view_state()

    current_page = "chat_bot"
    st.session_state.last_page = current_page

def main():
    setup_app()
    
    user_prompt = get_user_prompt()
    num_results, similarity_threshold = handle_sidebar()

    handle_chat_flow(user_prompt, num_results, similarity_threshold)

if __name__ == "__main__":
    main()
