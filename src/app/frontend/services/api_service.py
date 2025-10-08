import requests
import streamlit as st
from app.frontend.config.settings import get_settings

settings = get_settings()

def upload_files(documents):
    if documents is not None:
        with st.spinner("Cargando documentos...", show_time=True):
            for doc in documents:
                file_payload = {"files": (doc.name, doc.getvalue(), doc.type)}
                try:
                    response = requests.post(f"{settings.backend_api_base_url}{settings.documents_endpoint}", files=file_payload)               
                    if response.status_code != 200:
                        return None, f"Error {response.status_code}: {response.text}"
                    
                    return "Documentos cargados correctamente.", None
                
                except requests.exceptions.RequestException:
                    return None, "Error de conexión"

def get_agent_response(prompt, num_results, similarity_threshold):
    payload = {
        "question": prompt,
        "num_results": num_results,
        "similarity_threshold": similarity_threshold
    }

    try:
        response = requests.post(
            url=f"{settings.backend_api_base_url}{settings.search_endpoint}",
            json=payload
        )
        
        if response.status_code != 200:
            return None, f"Error {response.status_code}: {response.text}"
        
        return response.json(), None    
    
    except requests.exceptions.RequestException:
            return None, "Error de conexión"
