import mysql.connector


# --- Função 3: SELECT no MySQL ---
def get_dados_mysql():
    try:
        # 🔧 Ajuste suas credenciais abaixo
        conexao = mysql.connector.connect(
            host="SRVORACLEBR59.CITELSOFTWARE.COM.BR:59007",
            user="converte_realindustria",
            password="converte13347",
            database="CONVERTE"
        )

        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT ITE_DESITE FROM CADITE WHERE ITE_CODITE = '00810';")
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()

        return {"status": "ok", "resultado": f"{resultado}"}
    except Exception as e:
        return {"status": "erro","mensagem": f"{str(e)}"}