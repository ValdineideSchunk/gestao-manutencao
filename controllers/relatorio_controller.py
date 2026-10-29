
from flask import Blueprint, render_template

from models.relatorio import (
    relatorio_custo_por_equipamento,
    relatorio_historico_manutencoes
)


relatorio_bp = Blueprint("relatorios", __name__)


@relatorio_bp.route("/relatorios")
def listar():
    custos = relatorio_custo_por_equipamento()
    historico = relatorio_historico_manutencoes()

    return render_template(
        "relatorios.html",
        custos=custos,
        historico=historico
    )
