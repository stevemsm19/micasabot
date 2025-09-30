import streamlit as st

def main():
    st.title("MiCasa Bot 🏠")

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
