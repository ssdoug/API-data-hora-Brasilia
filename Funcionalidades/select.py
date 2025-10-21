import mysql.connector

def get_dados_mysql():
    try:
        # 🔧 Ajuste suas credenciais de conexão
        conexao = mysql.connector.connect(
            host="SRVORACLEBR59.CITELSOFTWARE.COM.BR",
            user="converte_realindustria",
            password="converte13347",
            database="CONVERTE",
            port=59007  # o parâmetro deve ser inteiro, não string
        )

        cursor = conexao.cursor(dictionary=True)
        query = "SELECT ITE_DESITE FROM CADITE WHERE ITE_CODITE = %s;"
        cursor.execute(query, ('00810',))  # evita SQL injection e melhora performance
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()

        #retorna resultado legível
        return {
            "status": "ok",
            "resultado": resultado  # já vem como lista de dicionários
        }
    
#    except mysql.connector.Error as err:
 #       return {
  #          "status": "erro",
   #         "mensagem": f"Erro no MySQL: {err}"
    #    }
     #   return {"status": "ok", "resultado": f"{resultado}"}

    except Exception as e:
       return {"status": "erro","mensagem": f"resultado da query: {str(e)}"}
    


#    except Exception as e:
#        return {
#            "status": "erro",
#            "mensagem": f"Erro geral: {str(e)}"
#        }
