
from config import obter_conexao


def listar_equipamentos():
    """Retorna todos os equipamentos cadastrados."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    ID_EQUIPAMENTO,
                    NOME,
                    MODELO,
                    NUMERO_SERIE,
                    STATUS
                FROM EQUIPAMENTO
                ORDER BY ID_EQUIPAMENTO
            """)

            return cursor.fetchall()


def buscar_equipamento(id_equipamento):
    """Busca um equipamento pelo identificador."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    ID_EQUIPAMENTO,
                    NOME,
                    MODELO,
                    NUMERO_SERIE,
                    STATUS
                FROM EQUIPAMENTO
                WHERE ID_EQUIPAMENTO = :id
            """, {"id": id_equipamento})

            return cursor.fetchone()


def cadastrar_equipamento(nome, modelo, numero_serie, status):
    """Insere um novo equipamento."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                INSERT INTO EQUIPAMENTO (
                    NOME,
                    MODELO,
                    NUMERO_SERIE,
                    STATUS
                )
                VALUES (
                    :nome,
                    :modelo,
                    :numero_serie,
                    :status
                )
            """, {
                "nome": nome,
                "modelo": modelo,
                "numero_serie": numero_serie,
                "status": status
            })

        conexao.commit()


def atualizar_equipamento(
    id_equipamento,
    nome,
    modelo,
    numero_serie,
    status
):
    """Atualiza os dados de um equipamento."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE EQUIPAMENTO
                SET
                    NOME = :nome,
                    MODELO = :modelo,
                    NUMERO_SERIE = :numero_serie,
                    STATUS = :status
                WHERE ID_EQUIPAMENTO = :id
            """, {
                "id": id_equipamento,
                "nome": nome,
                "modelo": modelo,
                "numero_serie": numero_serie,
                "status": status
            })

            alterados = cursor.rowcount

        conexao.commit()

    return alterados


def excluir_equipamento(id_equipamento):
    """Exclui um equipamento se não houver manutenção vinculada."""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                DELETE FROM EQUIPAMENTO
                WHERE ID_EQUIPAMENTO = :id
            """, {"id": id_equipamento})

            excluidos = cursor.rowcount

        conexao.commit()

    return excluidos
