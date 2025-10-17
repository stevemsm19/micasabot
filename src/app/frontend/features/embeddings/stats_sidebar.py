import streamlit as st

from typing import Any, Dict


def render_stats_sidebar(response: Dict[str, Any] | None) -> None:
    with st.sidebar:
        st.markdown("---")
        st.subheader("📊 Estadísticas generales")

        if not response:
            st.warning("No hay datos disponibles para mostrar estadísticas.")
            return

        total_embeddings = response.get("total_embeddings", 0)
        embedding_dim = response.get("embedding_dimension", 0)
        total_documents = response.get("total_documents", 0)

        st.metric("Total de Embeddings", total_embeddings)
        st.metric("Dimensión del Embedding", embedding_dim)
        st.metric("Total de Documentos", total_documents)
