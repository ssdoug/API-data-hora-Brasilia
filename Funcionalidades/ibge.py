from fastapi import HTTPException
from datetime import datetime
import pytz
import sidrapy  # biblioteca para consultas SIDRA



def get_populacao_uf(uf_codigo: str):
    """
    Retorna a população estimada da unidade federativa (UF) cujo código é uf_codigo,
    ou de todo o Brasil (use “all” como uf_codigo).
    """
    try:
        # Exemplo de tabela: ‘6579’ é usada para estimativas de população (ano base)  
        # Ou você pode usar outra tabela conforme o que estiver disponível no SIDRA.
        # territorial_level = 3 (UF)
        # ibge_territorial_code = uf_codigo ou “all”
        df = sidrapy.get_table(
            table_code="6579",
            territorial_level="3",
            ibge_territorial_code=uf_codigo,
            period="last",  # último ano disponível
            variable="all"
        )
        # df é um DataFrame do pandas (ou similar) com as colunas retornadas
        # Vamos extrair o valor
        # Supondo que haja uma coluna “Valor” ou “value” ou algo parecido
        # e uma coluna “Ano”.
        # Isso pode variar de acordo com a tabela!

        # Vamos converter para dict
        rec = df.to_dict(orient="records")
        if not rec or len(rec) == 0:
            raise HTTPException(status_code=404, detail="Dados não encontrados para essa UF")

        # Pegamos o primeiro registro
        primeiro = rec[0]
        ano = primeiro.get("Ano") or primeiro.get("ano") or primeiro.get("PERÍODO") or primeiro.get("periodo")
        valor = primeiro.get("Valor") or primeiro.get("valor") or primeiro.get("OBSERVAÇÃO") or primeiro.get("Valor estimado")

        return {
            "uf": uf_codigo,
            "indicador": "populacao_estimada",
            "ano": ano,
            "valor": valor
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar SIDRA: {str(e)}")
