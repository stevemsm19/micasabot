import numpy as np

from typing import Any

from sklearn.cluster import KMeans


def apply_kmeans(X: np.ndarray, n_clusters: int = 2) -> KMeans:
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(X)
    return model


def get_clusters(model: KMeans, X: np.ndarray) -> Any:
    return model.predict(X)
