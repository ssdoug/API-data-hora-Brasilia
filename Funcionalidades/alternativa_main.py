from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
def read_root():
    utilidades = dtahora()
    return utilidades.read_root()

@app.get("/hora")
def read_hora():
    utilidades = dtahora()
    return utilidades.get_brasilia_time()   

@app.get("/tot")
def read_tot():
    utilidades = dtahora()
    return utilidades.get_brasilia_time_full()