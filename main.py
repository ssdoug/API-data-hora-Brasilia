from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from Funcionalidades import dtahora, ibge, select

app = FastAPI(title="API Hora de Brasília")

# Permitir acesso de qualquer origem (para desktop apps e testes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# api ENDPOINT:     

@app.get("/")
def read_root_():
    return dtahora.read_root()

@app.get("/hora")
def get_hora():
    return dtahora.get_brasilia_time()

@app.get("/full")
def read_full():
    return dtahora.get_brasilia_time_full()

#@app.get("/test")
#def get_teste():
#    return dtahora.get_test()


@app.get("/pop/{uf_codigo}")
def get_populacao_uf(uf_codigo: str):
    return ibge.get_populacao_uf(uf_codigo)

@app.get("/test")
def get_dados_mysql():
    return select.get_dados_mysql()