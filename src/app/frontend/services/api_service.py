import requests
from app.frontend.config.settings import get_settings
from app.frontend.utils.messages import show_temporary_message

settings = get_settings()

def upload_files(documents):
    if documents is not None:
        for doc in documents:
            file_payload = {"files": (doc.name, doc.getvalue(), doc.type)}
            try:
                response = requests.post(f"{settings.backend_api_base_url}{settings.documents_endpoint}", files=file_payload)
                if response.status_code != 200:
                    show_temporary_message(f"Error uploading {doc.name}: {response.text}", "error", 10)
                    return
            except Exception as e:
                show_temporary_message(f"Failed to connect to backend: {e}", "error")
                return
        show_temporary_message("Documentos cargados correctamente.", "success")

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
        if response.status_code == 200:
            return response.json(), None
        return None, f"❌ Error {response.status_code}: {response.text}"
    except requests.exceptions.RequestException as e:
        return None, f"⚠️ Error de conexión: {e}"
