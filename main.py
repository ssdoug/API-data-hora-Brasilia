from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI(title="API Hora de Brasília")

# Permitir acesso de qualquer origem (para desktop apps e testes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Hora de Brasília!"}

@app.get("/hora")
def get_brasilia_time():
    brasilia_tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"data_hora_brasilia": data_hora}

@app.get("/full")
def get_brasilia_time():
    brasilia_tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"message": data_hora}
