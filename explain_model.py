from joblib import load

class PredictionModel:
    def __init__(self):
        self.shap_values= load("shap_values.joblib")
        self.X_sample_transformado = load("X_sample_transformado.joblib")

    def make_predictions():
        result = self.shap_values
        return result
    
    