import streamlit as st
from app.frontend.services.api_service import get_agent_response
from app.frontend.utils.constants import CHAT_SUGGESTIONS

def init_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = [
        ]

def display_chat_intro():
    with st.container():
        st.chat_input("Escribe tu pregunta aquí...", key="initial_question")

        selected_suggestion = st.pills(
            label="Preguntas sugeridas",
            label_visibility="collapsed",
            options=CHAT_SUGGESTIONS,
            key="selected_suggestion",
        )

    if selected_suggestion:
        st.session_state.selected_suggestion = selected_suggestion

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def add_user_message(prompt: str):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

def generate_agent_response(prompt, num_results, similarity_threshold):
    
    add_user_message(prompt)

    if st.session_state.messages[-1]["role"] == "assistant":
        return

    with st.spinner("Procesando..."):
        response_data, error = get_agent_response(prompt, num_results, similarity_threshold)
        sources = []

        if error:
            answer = error
        else:
            answer = response_data.get("answer")
            context = response_data.get("context", [])
            for item in context:
                metadata = item["metadata"]
                sources.append(metadata["source"])

        sources = list(set(sources))

        if sources:
            sources_text = f"\n\n📚 **Fuentes utilizadas:** {', '.join(sources)}"
        else:
            sources_text = ""

        st.session_state.messages.append({
            "role": "assistant",
            "content": f"{answer}{sources_text}"
        })

    st.rerun()
