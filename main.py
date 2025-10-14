from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI(title="API Hora de Brasília")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Hora de Brasília!"}

@app.get("/hora")
def get_brasilia_time():
    brasilia_tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"data_hora_brasilia": data_hora}

@app.get("/tot")
def get_brasilia_time():
    brasilia_tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"Bem-vindo à API Hora de Brasília!\n Data_hora_brasilia": data_hora}
