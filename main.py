from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

# Inicialização do app FastAPI
app = FastAPI(title="API de Previsão do Bitcoin com LSTM")

# Carregar modelo LSTM treinado
model = load_model("modelo_lstm.h5", compile=False)

# Escalador para normalização dos dados
scaler = MinMaxScaler(feature_range=(0, 1))

# Modelo de entrada manual via JSON
class PrevisaoRequest(BaseModel):
    historico: List[float]

@app.get("/")
def home():
    return {"mensagem": "API para previsão do preço do Bitcoin com LSTM está online."}

# Endpoint para entrada manual
@app.post("/prever")
def prever(request: PrevisaoRequest):
    dados = request.historico

    if len(dados) < 60:
        raise HTTPException(status_code=400, detail="São necessários ao menos 60 preços históricos.")

    try:
        dados_array = np.array(dados[-60:]).reshape(-1, 1)
        dados_normalizados = scaler.fit_transform(dados_array)
        entrada = np.reshape(dados_normalizados, (1, 60, 1))
        previsao_normalizada = model.predict(entrada)
        previsao = scaler.inverse_transform(previsao_normalizada)

        return {
            "preco_previsto": float(previsao[0][0])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint automático com yfinance
@app.post("/prever_auto")
def prever_auto():
    try:
        df = yf.download("BTC-USD", period="90d", interval="1d")

        if len(df) < 60:
            raise HTTPException(status_code=400, detail="Não há dados suficientes para prever (mínimo 60 dias).")

        fechamento = df["Close"].values[-60:]

        dados_array = np.array(fechamento).reshape(-1, 1)
        dados_normalizados = scaler.fit_transform(dados_array)
        entrada = np.reshape(dados_normalizados, (1, 60, 1))
        previsao_normalizada = model.predict(entrada)
        previsao = scaler.inverse_transform(previsao_normalizada)

        return {
            "preco_previsto": float(previsao[0][0]),
            "fonte": "Yahoo Finance",
            "dias_usados": 60
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))