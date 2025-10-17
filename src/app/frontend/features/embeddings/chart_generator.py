import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from typing import Any, Dict

from sklearn.manifold import TSNE

from app.frontend.features.embeddings.clustering import apply_kmeans, get_clusters
from app.frontend.features.embeddings.anomalies import apply_isolation_forest


def generate_chart(
    response: Dict[str, Any],
    perplexity: int,
    n_clusters: int,
    show_clusters: bool,
    show_anomalies: bool,
) -> go.Figure:
    if response is None or response.get("total_embeddings") == 0:
        return None

    doc_embeddings = np.array(response["embeddings"])
    metadatas = response["metadatas"]

    tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity)
    embeddings_2d = tsne.fit_transform(doc_embeddings)

    df = pd.DataFrame(
        {
            "x": embeddings_2d[:, 0],
            "y": embeddings_2d[:, 1],
            "source": [m.get("source") for m in metadatas],
            "page": [m.get("page") for m in metadatas],
        }
    )

    if show_clusters:
        model = apply_kmeans(doc_embeddings, n_clusters)
        df["cluster"] = get_clusters(model, doc_embeddings)
        fig = px.scatter(
            df,
            x="x",
            y="y",
            color="cluster",
            hover_data={
                "source": True,
                "x": False,
                "y": False,
                "cluster": True,
                "page": True,
            },
            color_continuous_scale="viridis",
            title="Clusters visualizados con t-SNE (K-Means)",
        )

    elif show_anomalies:
        df["anomaly"] = apply_isolation_forest(doc_embeddings)
        fig = px.scatter(
            df,
            x="x",
            y="y",
            color="anomaly",
            color_discrete_map={"Normal": "blue", "Anomaly": "red"},
            hover_data={
                "source": True,
                "x": False,
                "y": False,
                "anomaly": True,
                "page": True,
            },
            title="Anomalías detectadas con Isolation Forest (t-SNE)",
        )

    else:
        fig = px.scatter(
            df,
            x="x",
            y="y",
            hover_data={"source": True, "x": False, "y": False, "page": True},
            title="Visualización t-SNE (sin clustering ni anomalías)",
        )

    return fig
