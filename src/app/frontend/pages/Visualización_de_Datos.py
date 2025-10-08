import numpy as np
import streamlit as st
import plotly.express as px

from sklearn.manifold import TSNE

from app.frontend.services.api_service import get_embeddings

st.set_page_config(page_title="Visualización")

st.title("Embeddings")

response, error = get_embeddings()

doc_embeddings = np.array(response["embeddings"])
metadatas = response["metadatas"]

tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(doc_embeddings)

import pandas as pd
df = pd.DataFrame({
    "x": embeddings_2d[:, 0],
    "y": embeddings_2d[:, 1],
    "source": [m.get("source") for m in metadatas]
})

fig = px.scatter(
    df,
    x="x",
    y="y",
    hover_data={"source": True, "x": False, "y": False},
    title="Embedding Projector 2D"
)

st.plotly_chart(fig, use_container_width=True)