
from config import obter_conexao


def relatorio_custo_por_equipamento():
    """
    Retorna a quantidade de manutenções e o custo total
    agrupados por equipamento.
    """
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    e.ID_EQUIPAMENTO,
                    e.NOME,
                    COUNT(m.ID_MANUTENCAO) AS QUANTIDADE_MANUTENCOES,
                    NVL(SUM(m.CUSTO), 0) AS CUSTO_TOTAL
                FROM EQUIPAMENTO e
                LEFT JOIN MANUTENCAO m
                    ON m.ID_EQUIPAMENTO = e.ID_EQUIPAMENTO
                GROUP BY
                    e.ID_EQUIPAMENTO,
                    e.NOME
                ORDER BY
                    CUSTO_TOTAL DESC,
                    e.NOME
            """)

            return cursor.fetchall()

def relatorio_historico_manutencoes():
    """
    Retorna o histórico detalhado de manutenções,
    incluindo os nomes dos equipamentos e técnicos.
    """
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    m.ID_MANUTENCAO,
                    m.DATA_MANUTENCAO,
                    e.NOME AS EQUIPAMENTO,
                    t.NOME AS TECNICO,
                    m.DESCRICAO,
                    m.CUSTO
                FROM MANUTENCAO m
                INNER JOIN EQUIPAMENTO e
                    ON e.ID_EQUIPAMENTO = m.ID_EQUIPAMENTO
                INNER JOIN TECNICO t
                    ON t.ID_TECNICO = m.ID_TECNICO
                ORDER BY
                    m.DATA_MANUTENCAO DESC,
                    m.ID_MANUTENCAO DESC
            """)

            return cursor.fetchall()
