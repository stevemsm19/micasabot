import streamlit as st

def main():
    st.title("MiCasa Bot 🏠")
    st.info(
        "Puedes hacer preguntas sobre **adquisición de vivienda en Colombia**, como:\n"
        "- Conceptos clave (leasing habitacional, crédito hipotecario, etc.)\n"
        "- Beneficios y subsidios disponibles\n"
        "- Requisitos, tipos de vivienda, y más\n\n"
        "📄 También puedes subir **tus propios documentos** (PDF o TXT), y MiCasaBot te ayudará a responder preguntas basadas en su contenido.",
        icon="ℹ️"
    )

    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hola! ¿Como puedo ayudarte?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    with st.sidebar:
        st.subheader("Tus documentos")
        docs = st.file_uploader(
            label="Haz click en 'Browse files' para subir tus archivos .pdf y/o .txt",
            type=["pdf", "txt"],
            accept_multiple_files=True
        )

if __name__ == "__main__":
    main()
