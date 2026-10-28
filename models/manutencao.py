
from config import obter_conexao


def listar_manutencoes():
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    m.ID_MANUTENCAO,
                    m.ID_EQUIPAMENTO,
                    e.NOME,
                    m.ID_TECNICO,
                    t.NOME,
                    m.DATA_MANUTENCAO,
                    m.DESCRICAO,
                    m.CUSTO
                FROM MANUTENCAO m
                INNER JOIN EQUIPAMENTO e
                    ON e.ID_EQUIPAMENTO = m.ID_EQUIPAMENTO
                INNER JOIN TECNICO t
                    ON t.ID_TECNICO = m.ID_TECNICO
                ORDER BY m.DATA_MANUTENCAO DESC,
                         m.ID_MANUTENCAO DESC
            """)
            return cursor.fetchall()


def buscar_manutencao(id_manutencao):
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    ID_MANUTENCAO,
                    ID_EQUIPAMENTO,
                    ID_TECNICO,
                    DATA_MANUTENCAO,
                    DESCRICAO,
                    CUSTO
                FROM MANUTENCAO
                WHERE ID_MANUTENCAO = :id
            """, {"id": id_manutencao})
            return cursor.fetchone()


def cadastrar_manutencao(
    id_equipamento,
    id_tecnico,
    data_manutencao,
    descricao,
    custo
):
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                INSERT INTO MANUTENCAO (
                    ID_EQUIPAMENTO,
                    ID_TECNICO,
                    DATA_MANUTENCAO,
                    DESCRICAO,
                    CUSTO
                )
                VALUES (
                    :id_equipamento,
                    :id_tecnico,
                    TO_DATE(:data_manutencao, 'YYYY-MM-DD'),
                    :descricao,
                    :custo
                )
            """, {
                "id_equipamento": id_equipamento,
                "id_tecnico": id_tecnico,
                "data_manutencao": data_manutencao,
                "descricao": descricao,
                "custo": custo
            })
        conexao.commit()


def atualizar_manutencao(
    id_manutencao,
    id_equipamento,
    id_tecnico,
    data_manutencao,
    descricao,
    custo
):
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE MANUTENCAO
                SET
                    ID_EQUIPAMENTO = :id_equipamento,
                    ID_TECNICO = :id_tecnico,
                    DATA_MANUTENCAO =
                        TO_DATE(:data_manutencao, 'YYYY-MM-DD'),
                    DESCRICAO = :descricao,
                    CUSTO = :custo
                WHERE ID_MANUTENCAO = :id
            """, {
                "id": id_manutencao,
                "id_equipamento": id_equipamento,
                "id_tecnico": id_tecnico,
                "data_manutencao": data_manutencao,
                "descricao": descricao,
                "custo": custo
            })
            alterados = cursor.rowcount
        conexao.commit()
    return alterados


def excluir_manutencao(id_manutencao):
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                DELETE FROM MANUTENCAO
                WHERE ID_MANUTENCAO = :id
            """, {"id": id_manutencao})
            excluidos = cursor.rowcount
        conexao.commit()
    return excluidos
