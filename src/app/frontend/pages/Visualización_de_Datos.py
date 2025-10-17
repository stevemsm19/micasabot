import streamlit as st
import plotly.graph_objs as go

from typing import Any, Dict

from app.frontend.services.api_service import get_embeddings
from app.frontend.features.embeddings.chart_generator import generate_chart
from app.frontend.features.embeddings.chart_state import (
    init_visualization_state,
    setup_page_state,
)
from app.frontend.features.embeddings.stats_sidebar import render_stats_sidebar
from app.frontend.utils.messages import show_temporary_message

st.set_page_config(page_title="Visualización de Embeddings")
st.title("Embeddings Projector 2D")

init_visualization_state()
setup_page_state()


def on_toggle_clusters() -> None:
    if st.session_state.show_clusters:
        st.session_state.show_anomalies = False
    st.session_state.regenerate_chart = True


def on_toggle_anomalies() -> None:
    if st.session_state.show_anomalies:
        st.session_state.show_clusters = False
    st.session_state.regenerate_chart = True


with st.sidebar:
    st.subheader("Parámetros de visualización")
    perplexity = st.slider("Perplexity", 5, 50, 30, 10)
    n_clusters = st.slider(
        "Number of Clusters",
        min_value=2,
        max_value=30,
        value=5,
        step=1,
        disabled=not st.session_state.show_clusters,
        key="n_clusters",
    )
    show_clusters = st.checkbox(
        "Mostrar clusters con K-Means",
        key="show_clusters",
        on_change=on_toggle_clusters,
    )
    show_anomalies = st.checkbox(
        "Mostrar anomalías con Isolation Forest",
        key="show_anomalies",
        on_change=on_toggle_anomalies,
    )
    regenerate = st.button("Regenerar gráfico", type="primary")


def render_chart(
    response: Dict[str, Any], perplexity: int, show_clusters: bool, show_anomalies: bool
) -> None:
    with st.spinner("Generando gráfico..."):
        fig: go.Figure = generate_chart(
            response, perplexity, n_clusters, show_clusters, show_anomalies
        )
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            show_temporary_message(
                "No hay información para generar el gráfico", "error"
            )


if st.session_state.display_initial_chart or regenerate:

    response, error = get_embeddings()
    if response is None:
        show_temporary_message(error or "Error desconocido", "error")

    else:
        render_chart(response, perplexity, show_clusters, show_anomalies)
        render_stats_sidebar(response)
        st.session_state.display_initial_chart = False
        st.session_state.regenerate_chart = False
