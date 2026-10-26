
from config import obter_conexao

try:
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT 'Conexao OK' FROM dual")
            print(cursor.fetchone()[0])
except Exception as erro:
    print("Falha na conexão:", erro)
