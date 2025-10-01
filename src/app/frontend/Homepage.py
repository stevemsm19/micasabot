import streamlit as st

import time

from app.frontend.config.setttings import get_settings

settings = get_settings()

def render_intro():
    st.title("MiCasa Bot 🏠")
    st.info(
        "Puedes hacer preguntas sobre **adquisición de vivienda en Colombia**, como:\n"
        "- Conceptos clave (leasing habitacional, crédito hipotecario, etc.)\n"
        "- Beneficios y subsidios disponibles\n"
        "- Requisitos, tipos de vivienda, y más\n\n"
        "📄 También puedes subir **tus propios documentos** (PDF o TXT), y MiCasaBot te ayudará a responder preguntas basadas en su contenido.",
        icon="ℹ️"
    )

def upload_sidebar_docs():
    with st.sidebar:
        st.subheader("Tus documentos")
        documents = st.file_uploader(
            label="Haz click en 'Browse files' para subir tus archivos .pdf y/o .txt",
            type=["pdf", "txt"],
            accept_multiple_files=True
        )
        if st.button("Cargar Documentos"):
            if documents:
                show_temporary_message("Documentos cargados correctamente.", "success")
            else:
                show_temporary_message("Por favor, sube al menos un archivo antes de continuar.", "error")

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

def generate_bot_response():
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Procesando..."):
                placeholder = st.empty()
                full_response = "Test." 
                placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

def show_temporary_message(content: str, message_type: str, duration: int = 2):
    msg = st.empty()

    if message_type == "success":
        msg.success(content, icon="✅")
    elif message_type == "error":
        msg.error(content,icon="❌")
    else:
        msg.write(content)

    time.sleep(duration)
    msg.empty()

def main():
    render_intro()
    upload_sidebar_docs()
    
    init_chat()
    display_chat_history()

    prompt = handle_user_input()
    if prompt:
        generate_bot_response()

if __name__ == "__main__":
    main()
