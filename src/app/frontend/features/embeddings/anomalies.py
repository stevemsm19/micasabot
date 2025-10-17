import numpy as np
from sklearn.ensemble import IsolationForest


def apply_isolation_forest(X: np.ndarray, contamination: float = 0.05) -> np.ndarray:
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(X)
    predictions = model.predict(X)
    labels = np.where(predictions == 1, "Normal", "Anomaly")
    return labels
