
from config import obter_conexao


def listar_tecnicos():
    """Retorna todos os técnicos cadastrados."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    ID_TECNICO,
                    NOME,
                    ESPECIALIDADE
                FROM TECNICO
                ORDER BY ID_TECNICO
            """)
            return cursor.fetchall()


def buscar_tecnico(id_tecnico):
    """Busca um técnico pelo identificador."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    ID_TECNICO,
                    NOME,
                    ESPECIALIDADE
                FROM TECNICO
                WHERE ID_TECNICO = :id
            """, {"id": id_tecnico})
            return cursor.fetchone()


def cadastrar_tecnico(nome, especialidade):
    """Insere um novo técnico."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                INSERT INTO TECNICO (
                    NOME,
                    ESPECIALIDADE
                )
                VALUES (
                    :nome,
                    :especialidade
                )
            """, {
                "nome": nome,
                "especialidade": especialidade
            })
        conexao.commit()


def atualizar_tecnico(id_tecnico, nome, especialidade):
    """Atualiza os dados de um técnico."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE TECNICO
                SET
                    NOME = :nome,
                    ESPECIALIDADE = :especialidade
                WHERE ID_TECNICO = :id
            """, {
                "id": id_tecnico,
                "nome": nome,
                "especialidade": especialidade
            })
            alterados = cursor.rowcount
        conexao.commit()

    return alterados


def excluir_tecnico(id_tecnico):
    """Exclui um técnico, respeitando as chaves estrangeiras."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                DELETE FROM TECNICO
                WHERE ID_TECNICO = :id
            """, {"id": id_tecnico})
            excluidos = cursor.rowcount
        conexao.commit()

    return excluidos