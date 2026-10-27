
import os
from pathlib import Path

import oracledb


USUARIO = "labdatabase"
SENHA = os.getenv("ORACLE_PASSWORD")
DSN = "localhost:1521/XEPDB1"

arquivo_sql = Path(__file__).parent / "sql" / "criar_tabelas.sql"


def executar_script():
    if not SENHA:
        print("Erro: configure a variável ORACLE_PASSWORD antes de executar.")
        return

    if not arquivo_sql.exists():
        print(f"Erro: arquivo SQL não encontrado: {arquivo_sql}")
        return

    try:
        script = arquivo_sql.read_text(encoding="utf-8")

        comandos = [
            comando.strip()
            for comando in script.split(";")
            if comando.strip()
        ]

        with oracledb.connect(
            user=USUARIO,
            password=SENHA,
            dsn=DSN
        ) as conexao:
            with conexao.cursor() as cursor:
                for numero, comando in enumerate(comandos, start=1):
                    try:
                        cursor.execute(comando)
                        print(f"Comando {numero} executado com sucesso.")
                    except oracledb.DatabaseError as erro:
                        print(f"Erro no comando {numero}:")
                        print(erro)
                        return

        print("\nEstrutura do banco criada com sucesso!")

    except Exception as erro:
        print("\nErro ao executar o script:")
        print(erro)


if __name__ == "__main__":
    executar_script()
