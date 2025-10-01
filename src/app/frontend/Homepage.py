import streamlit as st

st.title("MiCasa Bot 🏠")
st.info(
    "Puedes hacer preguntas sobre **adquisición de vivienda en Colombia**, como:\n"
    "- Conceptos clave (leasing habitacional, crédito hipotecario, etc.)\n"
    "- Beneficios y subsidios disponibles\n"
    "- Requisitos, tipos de vivienda, y más\n\n"
    "📄 También puedes subir **tus propios documentos** (PDF o TXT), y MiCasaBot te ayudará a responder preguntas basadas en su contenido.",
    icon="ℹ️"
)

with st.sidebar:
    st.subheader("Tus documentos")
    docs = st.file_uploader(
        label="Haz click en 'Browse files' para subir tus archivos .pdf y/o .txt",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hola! ¿Como puedo ayudarte?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input()

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = "Test."
        placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)