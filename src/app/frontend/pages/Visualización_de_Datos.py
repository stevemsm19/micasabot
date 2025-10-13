import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from typing import Any, Dict, List

from sklearn.manifold import TSNE

from app.frontend.utils.messages import show_temporary_message
from app.frontend.utils.session_state import apply_session_states, handle_page_change
from app.frontend.services.api_service import get_embeddings

st.set_page_config(page_title="Visualización de Embeddings")
st.title("Embeddings Projector 2D")


def generate_chart(perplexity: int) -> go.Figure:

    response, error = get_embeddings()
    if response is None:
        show_temporary_message(error or "Error desconocido", "error")
        return

    doc_embeddings: np.ndarray = np.array(response["embeddings"])
    metadatas: List[Dict[str, Any]] = response["metadatas"]

    tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity)
    embeddings_2d: np.ndarray = tsne.fit_transform(doc_embeddings)

    df = pd.DataFrame(
        {
            "x": embeddings_2d[:, 0],
            "y": embeddings_2d[:, 1],
            "source": [m.get("source") for m in metadatas],
        }
    )

    fig = px.scatter(
        df, x="x", y="y", hover_data={"source": True, "x": False, "y": False}
    )
    return fig


def reset_visualization_state() -> None:
    st.session_state.display_initial_chart = True
    st.session_state.regenerate_chart = False
    st.session_state.displaying_chart = False


def init_visualization_state() -> None:
    defaults: dict[str, bool] = {
        "display_initial_chart": True,
        "regenerate_chart": False,
        "displaying_chart": False,
    }
    apply_session_states(defaults)


handle_page_change("visualization", reset_visualization_state)

with st.sidebar:
    st.subheader("Parámetros de visualización")
    st.caption("Ajusta cómo se proyectan los embeddings.")

    perplexity: int = st.slider(
        label="Perplexity",
        min_value=5,
        max_value=50,
        value=30,
        step=10,
        help="Define cuántos vecinos cercanos considera el algoritmo.",
    )

    st.session_state.regenerate_chart = st.button("Regenerar gráfico", type="primary")


def render_chart(perplexity: int) -> None:
    with st.spinner(f"Generando gráfico (perplexity: {perplexity})..."):
        fig: go.Figure = generate_chart(perplexity)
        st.plotly_chart(fig, use_container_width=True)


if st.session_state.display_initial_chart or st.session_state.regenerate_chart:
    render_chart(perplexity)
    st.session_state.display_initial_chart = False
    st.session_state.regenerate_chart = False
