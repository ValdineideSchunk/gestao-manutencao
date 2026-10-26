
import oracledb

# Dados de conexão fornecidos pela faculdade
USUARIO = "labdatabase"
SENHA = "lab@Database2025"
SERVIDOR = "localhost"
PORTA = 1521
SERVICE_NAME = "XEPDB1"

try:
    conexao = oracledb.connect(
        user=USUARIO,
        password=SENHA,
        dsn=f"{SERVIDOR}:{PORTA}/{SERVICE_NAME}"
    )

    cursor = conexao.cursor()
    cursor.execute("SELECT 'Conexao Oracle OK' FROM dual")

    resultado = cursor.fetchone()
    print(resultado[0])

    cursor.close()
    conexao.close()

except oracledb.Error as erro:
    print("Erro ao conectar ao Oracle:")
    print(erro)
