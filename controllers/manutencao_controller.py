
from datetime import date
from decimal import Decimal, InvalidOperation

from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.manutencao import (
    listar_manutencoes,
    buscar_manutencao,
    cadastrar_manutencao,
    atualizar_manutencao,
    excluir_manutencao
)

from models.equipamento import listar_equipamentos
from models.tecnico import listar_tecnicos

manutencao_bp = Blueprint("manutencoes", __name__)


@manutencao_bp.route("/manutencoes")
def listar():
    return render_template(
        "manutencoes.html",
        manutencoes=listar_manutencoes(),
        equipamentos=listar_equipamentos(),
        tecnicos=listar_tecnicos(),
        manutencao_edicao=None
    )


@manutencao_bp.route("/manutencoes/salvar", methods=["POST"])
def salvar():
    id_manutencao = request.form.get("id_manutencao", "").strip()
    id_equipamento = request.form.get("id_equipamento", "").strip()
    id_tecnico = request.form.get("id_tecnico", "").strip()
    data_manutencao = request.form.get("data_manutencao", "").strip()
    descricao = request.form.get("descricao", "").strip()
    custo_texto = request.form.get("custo", "").strip().replace(",", ".")

    if not all([
        id_equipamento,
        id_tecnico,
        data_manutencao,
        descricao,
        custo_texto
    ]):
        flash("Preencha todos os campos da manutenção.", "erro")
        return redirect(url_for("manutencoes.listar"))

    try:
        id_equipamento = int(id_equipamento)
        id_tecnico = int(id_tecnico)
        custo = Decimal(custo_texto)

        if not custo.is_finite() or custo < 0:
            raise ValueError("Custo inválido")

        date.fromisoformat(data_manutencao)

        if id_manutencao:
            alterados = atualizar_manutencao(
                int(id_manutencao),
                id_equipamento,
                id_tecnico,
                data_manutencao,
                descricao,
                custo
            )

            if alterados:
                flash("Manutenção atualizada com sucesso!", "sucesso")
            else:
                flash("Manutenção não encontrada.", "erro")
        else:
            cadastrar_manutencao(
                id_equipamento,
                id_tecnico,
                data_manutencao,
                descricao,
                custo
            )
            flash("Manutenção cadastrada com sucesso!", "sucesso")

    except (ValueError, InvalidOperation):
        flash("Verifique os IDs, a data e o custo informados.", "erro")
    except Exception as erro:
        print("ERRO AO SALVAR MANUTENCAO:", repr(erro))

        if "ORA-02291" in str(erro):
            flash("Selecione um equipamento e um técnico existentes.", "erro")
        elif "CK_MANUTENCAO_CUSTO" in str(erro):
            flash("O custo informado não atende à regra do banco.", "erro")
        else:
            flash("Não foi possível salvar a manutenção.", "erro")

    return redirect(url_for("manutencoes.listar"))


@manutencao_bp.route("/manutencoes/editar/<int:id_manutencao>")
def editar(id_manutencao):
    manutencao = buscar_manutencao(id_manutencao)

    if manutencao is None:
        flash("Manutenção não encontrada.", "erro")
        return redirect(url_for("manutencoes.listar"))

    return render_template(
        "manutencoes.html",
        manutencoes=listar_manutencoes(),
        equipamentos=listar_equipamentos(),
        tecnicos=listar_tecnicos(),
        manutencao_edicao=manutencao
    )


@manutencao_bp.route(
    "/manutencoes/excluir/<int:id_manutencao>",
    methods=["POST"]
)
def excluir(id_manutencao):
    try:
        excluidas = excluir_manutencao(id_manutencao)

        if excluidas:
            flash("Manutenção excluída com sucesso!", "sucesso")
        else:
            flash("Manutenção não encontrada.", "erro")

    except Exception as erro:
        print("ERRO AO EXCLUIR MANUTENCAO:", repr(erro))
        flash("Não foi possível excluir a manutenção.", "erro")

    return redirect(url_for("manutencoes.listar"))
