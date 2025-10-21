import sidrapy  # biblioteca para consultas SIDRA
import pandas as pd

def get_populacao_uf(uf_codigo: str):
    """
    Retorna a população residente mais recente da UF (IBGE - SIDRA).
    Fonte: Tabela 6579 - Contas regionais.
    """
    df = sidrapy.get_table(
        table_code="6022",          # PIB e População por UF
        territorial_level="brasil",      # Nível 3 = Unidade da Federação
        ibge_territorial_code=uf_codigo,
        period="last",              # Último ano disponível
        variable="01"               # População residente
    )
    
    # Extrai dados principais
    nome_uf = df["D1N"].iloc[0]
    ano = df["D2N"].iloc[0]
    valor = df["V"].iloc[0]
    
    return {
        "uf": nome_uf,
        "ano": ano,
        "populacao_residente": int(float(valor))
    }

# Exemplo: Minas Gerais (código IBGE = 31)
resultado = get_populacao_uf("31")
print(resultado)


