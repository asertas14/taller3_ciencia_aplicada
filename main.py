from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List

# Modelos
modelos = {
    "best": joblib.load('best_model.joblib'),
    "baseline": joblib.load('baseline_model.joblib')
}

shap_values = joblib.load("shap_values_best.joblib")
X_sample_transformado = joblib.load("X_sample_transformado_best.joblib") 

# Características para los modelos
model_features = ['Contract', 'PaymentMethod', 'OnlineSecurity', 'TechSupport', 'InternetService', 'DeviceProtection', 'OnlineBackup', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'Dependents', 'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']

app = FastAPI()

class DataModel(BaseModel):
    Contract: str
    PaymentMethod: str
    OnlineSecurity: str
    TechSupport: str
    InternetService: str
    DeviceProtection: str
    OnlineBackup: str
    StreamingTV: str
    StreamingMovies: str
    PaperlessBilling: str
    Dependents: str
    SeniorCitizen: int
    tenure: float
    MonthlyCharges: float
    TotalCharges: float

class PredictionRequest(BaseModel):
    datos: List[DataModel]

@app.post("/{model_version}/predict")
def make_predictions(model_version: str, request: PredictionRequest):
    if model_version not in modelos:
        raise HTTPException(status_code=400, detail="Modelo no válido")

    model = modelos[model_version]
    df = pd.DataFrame([x.dict() for x in request.datos])
    df = df[model_features]

    try:
        # Predicciones y probabilidades
        labels = model.predict(df)
        probabilities = model.predict_proba(df)[:, 1] if hasattr(model, 'predict_proba') else [None] * len(df)

        # Convertir a tipos nativos de Python
        labels = labels.tolist()
        probabilities = probabilities.tolist()

        # Empaquetar en un formato de respuesta
        response = [{"label": int(label), "probability": float(prob) if prob is not None else None} for label, prob in zip(labels, probabilities)]
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/{model_version}/explain")
def explain_predictions(model_version: str, request: PredictionRequest):
    from joblib import load
    if model_version not in modelos:
        raise HTTPException(status_code=400, detail="Modelo no válido")

    # Elegir el conjunto correcto de valores SHAP y datos transformados
    if model_version == "best":
        shap_values = shap_values
        X_sample_transformado = X_sample_transformado
        
    elif model_version == "baseline":
        shap_values = shap_values_base
        X_sample_transformado = X_sample_transformado_base
    else:
        raise HTTPException(status_code=400, detail="Modelo no reconocido")

    df = pd.DataFrame([x.dict() for x in request.datos])
    df = df[model_features]

    try:
    
        explanations = []
        for index, _ in df.iterrows():
            values = shap_values[index]
            importance = sorted(zip(model_features, values), key=lambda x: abs(x[1]), reverse=True)
            top_features = importance[:3]

            # Construir texto explicativo
            explanation_text = "Las principales características que influyeron en esta predicción son: "
            feature_explanations = []
            for feature, shap_value in top_features:
                direction = "aumentar" if shap_value > 0 else "disminuir"
                feature_explanations.append(f"{feature}, que tiende a {direction} la probabilidad de la clase positiva.")

            explanation = {
                "features": {feature: value for feature, value in top_features},
                "explanation": explanation_text + "; ".join(feature_explanations)
            }
            explanations.append(explanation)

        return explanations
        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def read_root():
    return { "message": "Hello world" }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
