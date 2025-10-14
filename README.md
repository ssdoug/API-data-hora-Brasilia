# API Hora de Brasília

API simples em Python com FastAPI que retorna a data e hora atual de Brasília.

## Rotas

- `/` - Mensagem de boas-vindas
- `/hora` - Retorna a data e hora atual de Brasília

## Executando localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload