import streamlit as st
from app.frontend.components.sidebar import upload_documents_sidebar, handle_upload_button, set_variables_sidebar
from app.frontend.components.chat import init_chat, display_chat_history, generate_agent_response, display_chat_intro

def main():
    st.set_page_config("MiCasa Bot", page_icon="💬")
    st.title("MiCasa Bot 💬")

    documents = upload_documents_sidebar()
    handle_upload_button(documents)
    
    num_results, similarity_threshold = set_variables_sidebar()

    init_chat()

    user_prompt = None

    if "selected_suggestion" in st.session_state and st.session_state.selected_suggestion:
        user_prompt = st.session_state.selected_suggestion
        st.session_state.selected_suggestion = None

    elif "initial_question" in st.session_state and st.session_state.initial_question:
        user_prompt = st.session_state.initial_question
        st.session_state.initial_question = None

    has_history = "messages" in st.session_state and len(st.session_state.messages) > 0
    if not user_prompt and not has_history:
        display_chat_intro()
        st.stop()

    display_chat_history()

    prompt_input = st.chat_input("Escribe tu pregunta aquí...", key="user_input")
    if prompt_input:
        user_prompt = prompt_input

    if user_prompt:
        generate_agent_response(user_prompt, num_results, similarity_threshold)

if __name__ == "__main__":
    main()
