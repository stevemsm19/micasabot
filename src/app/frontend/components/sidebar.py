import streamlit as st
from app.frontend.services.api_service import upload_files
from app.frontend.utils.messages import show_temporary_message

def upload_documents_sidebar():
    with st.sidebar:
        st.subheader("Tus documentos")
        documents = st.file_uploader(
            label="Haz click en 'Browse files' para subir tus archivos .pdf y/o .txt",
            type=["pdf", "txt"],
            accept_multiple_files=True
        )
        return documents

def handle_upload_button(documents):
    with st.sidebar:
        if st.button("Cargar Documentos", type="primary", disabled=st.session_state.is_processing_answer):
            if documents:
                response_data, error = upload_files(documents)

                if error:
                    return show_temporary_message(f"{error}", "error")

                show_temporary_message(response_data, "success")
            else:
                show_temporary_message("Por favor, sube al menos un archivo valido antes de continuar.", "error")

def set_variables_sidebar():
    with st.sidebar:
        st.markdown("---")
        st.subheader("Parámetros del Bot")
        st.caption("Estos valores se pasan al bot para ajustar cómo recupera y prioriza los documentos almacenados.")

        num_results = st.number_input(
            label="Número de resultados",
            min_value=1,
            max_value=20,
            value=3,
            step=1,
            help="Número de documentos más relevantes que el bot considerará en su respuesta.",
            disabled=st.session_state.is_processing_answer
        )

        similarity_threshold = st.slider(
            label="Umbral de similitud",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Nivel mínimo de similitud requerido entre la consulta y los documentos.",
            disabled=st.session_state.is_processing_answer
        )

        return num_results, similarity_threshold

def handle_sidebar():
    documents = upload_documents_sidebar()
    handle_upload_button(documents)
    return set_variables_sidebar()