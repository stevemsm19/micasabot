import streamlit as st
from app.frontend.services.api_service import get_agent_response

def init_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hola! ¿Como puedo ayudarte?"}
        ]

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    prompt = st.chat_input("Escribe tu pregunta aquí...", key="user_input")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    return prompt

def generate_agent_response(prompt, num_results, similarity_threshold):
    if st.session_state.messages[-1]["role"] == "assistant":
        return

    with st.chat_message("assistant"):
        with st.spinner("Procesando..."):
            response_data, error = get_agent_response(prompt, num_results, similarity_threshold)
            placeholder = st.empty()
            if error:
                placeholder.markdown(error)
                st.session_state.messages.append({"role": "assistant", "content": error})
            else:
                full_response = response_data.get("answer")
                placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
