import requests
import streamlit as st

from streamlit.runtime.uploaded_file_manager import UploadedFile

from typing import List, Optional, Tuple, Dict, Any

from app.frontend.utils.constants.endpoints import (
    DOCUMENTS_ENDPOINT,
    EMBEDDING_ENDPOINT,
    SEARCH_ENDPOINT,
)

from app.frontend.config.settings import get_settings

SETTINGS = get_settings()
base_url = f"http://{SETTINGS.api_host}:{SETTINGS.api_port}/"


def upload_files(
    documents: Optional[List[UploadedFile]],
) -> Tuple[Optional[str], Optional[str]]:
    if not documents:
        return None, "No hay documentos"

    with st.spinner("Cargando documentos...", show_time=True):
        file_payload = [("files", (doc.name, doc, doc.type)) for doc in documents]

        try:
            response = requests.post(
                f"{base_url}{DOCUMENTS_ENDPOINT}",
                files=file_payload,
            )
            if response.status_code != 200:
                return None, f"Error {response.status_code}: {response.text}"

            response_json = response.json()
            total_pages = response_json.get("total_pages")
            total_chunks = response_json.get("total_chunks")
            total_documents = len(documents)

            return (
                f"Se han cargado {total_documents} documentos, con un total de {total_pages} páginas "
                f"divididas en {total_chunks} chunks.",
                None,
            )

        except requests.exceptions.RequestException:
            return None, "Error de conexión"


def get_agent_response(
    prompt: str, num_results: int, similarity_threshold: float
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    payload = {
        "question": prompt,
        "num_results": num_results,
        "similarity_threshold": similarity_threshold,
    }

    try:
        response = requests.post(url=f"{base_url}{SEARCH_ENDPOINT}", json=payload)

        if response.status_code != 200:
            return None, f"Error {response.status_code}: {response.text}"

        return response.json(), None

    except requests.exceptions.RequestException:
        return None, "Error de conexión"


def get_embeddings() -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    try:
        response = requests.get(
            url=f"{base_url}{EMBEDDING_ENDPOINT}",
        )

        if response.status_code != 200:
            return None, f"Error {response.status_code}: {response.text}"

        return response.json(), None

    except requests.exceptions.RequestException:
        return None, "Error de conexión"
