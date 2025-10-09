
from app.frontend.utils.session_state import apply_session_states

def init_chat_state():
    defaults = {
        "messages": [],
        "selected_suggestion": None,
        "temp_user_input": None,
        "user_input": None,
        "is_processing_answer": False,
    }
    apply_session_states(defaults)