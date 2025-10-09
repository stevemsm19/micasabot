import os
import streamlit as st

from app.frontend.services.api_service import get_agent_response

def generate_agent_response(prompt, num_results, similarity_threshold):

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
            sources_clean = [os.path.splitext(source)[0] for source in sources]
            sources_text = f"\n\n📚 **Fuentes utilizadas:** {', '.join(sources_clean)}"
        else:
            sources_text = ""

        st.session_state.messages.append({
            "role": "assistant",
            "content": f"{answer}{sources_text}"
        })

    st.session_state.is_processing_answer = False
    st.rerun()
