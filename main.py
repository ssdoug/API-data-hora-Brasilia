from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import pytz
from Funcionalidades import dtahora

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
def read_root_():
    return dtahora.read_root()

@app.get("/hora")
def get_hora():
    return dtahora.get_brasilia_time()

@app.get("/full")
def read_full():
    return dtahora.get_brasilia_time_full()

@app.get("/test")
def get_teste():
    return dtahora.get_test()