from datetime import datetime
import pytz


def read_root():
    return {"message": "Bem-vindo à API Hora de Brasília!"}


def get_brasilia_time():
    brasilia_tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"data_hora_brasilia": data_hora}


def get_brasilia_time_full():
    brasilia_tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"Bem-vindo à API Hora de Brasília! Atual:": data_hora}
