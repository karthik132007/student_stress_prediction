from pathlib import Path
import pickle
import numpy as np

class ModelLoadError(Exception):
    pass

def load_model():
    model_path = Path(__file__).resolve().parent / "model.pkl"
    if not model_path.exists():
        raise ModelLoadError("model.pkl not found next to main.py. Commit it to the repo or generate it during build.")
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
    except ModuleNotFoundError as e:
        # This commonly happens when numpy / sklearn versions mismatch the pickle
        raise ModelLoadError(
            "Failed to load model.pkl due to environment mismatch. "
            "Make sure numpy and scikit-learn versions match the training environment. "
            "Pin versions in requirements.txt (see requirements.fixed.txt)."
        ) from e
    return model

def predict_label(model, features_1d):
    # Ensure 2D shape (1, n_features)
    x = np.asarray(features_1d, dtype=float).reshape(1, -1)
    y = model.predict(x)
    # Cast numpy scalar/array to Python int
    try:
        return int(y[0])
    except Exception:
        try:
            return int(y.item())
        except Exception:
            return int(y)
