
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


# LISTAR MANUTENÇÕES
@manutencao_bp.route("/manutencoes")
def listar():
    return render_template(
        "manutencoes.html",
        manutencoes=listar_manutencoes(),
        equipamentos=listar_equipamentos(),
        tecnicos=listar_tecnicos(),
        manutencao_edicao=None
    )


# LISTAR MANUTENÇÕES PARA ATUALIZAÇÃO
@manutencao_bp.route("/manutencoes/atualizar")
def atualizar_lista():
    manutencoes = listar_manutencoes()

    return render_template(
        "atualizar_manutencoes.html",
        manutencoes=manutencoes
    )


# LISTAR MANUTENÇÕES PARA REMOÇÃO
@manutencao_bp.route("/manutencoes/remover")
def remover_lista():
    manutencoes = listar_manutencoes()

    return render_template(
        "remover_manutencoes.html",
        manutencoes=manutencoes
    )


# CADASTRAR OU ATUALIZAR MANUTENÇÃO
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
            id_manutencao = int(id_manutencao)

            alterados = atualizar_manutencao(
                id_manutencao,
                id_equipamento,
                id_tecnico,
                data_manutencao,
                descricao,
                custo
            )

            if alterados:
                return redirect(
                    url_for(
                        "manutencoes.atualizacao_concluida",
                        id_manutencao=id_manutencao
                    )
                )
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

            return redirect(
                url_for("manutencoes.cadastro_concluido")
            )

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


# TELA DE CONFIRMAÇÃO DO CADASTRO
@manutencao_bp.route("/manutencoes/cadastro-concluido")
def cadastro_concluido():
    return render_template("manutencao_cadastrada.html")


# TELA DE CONFIRMAÇÃO DA ATUALIZAÇÃO
@manutencao_bp.route("/manutencoes/atualizacao-concluida/<int:id_manutencao>")
def atualizacao_concluida(id_manutencao):
    manutencao = buscar_manutencao(id_manutencao)

    if manutencao is None:
        flash("Manutenção não encontrada.", "erro")
        return redirect(url_for("manutencoes.atualizar_lista"))

    # Busca os dados completos, incluindo os nomes do equipamento e técnico
    manutencoes = listar_manutencoes()

    manutencao_completa = next(
        (item for item in manutencoes if item[0] == id_manutencao),
        None
    )

    if manutencao_completa is None:
        flash("Não foi possível localizar os dados da manutenção.", "erro")
        return redirect(url_for("manutencoes.atualizar_lista"))

    return render_template(
        "manutencao_atualizada.html",
        manutencao=manutencao_completa
    )


# EDITAR MANUTENÇÃO
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


# TELA DE CONFIRMAÇÃO DA EXCLUSÃO
@manutencao_bp.route("/manutencoes/exclusao-concluida")
def exclusao_concluida():
    return render_template("manutencao_excluida.html")


# EXCLUIR MANUTENÇÃO
@manutencao_bp.route(
    "/manutencoes/excluir/<int:id_manutencao>",
    methods=["POST"]
)
def excluir(id_manutencao):
    try:
        excluidas = excluir_manutencao(id_manutencao)

        if excluidas:
            return redirect(
                url_for("manutencoes.exclusao_concluida")
            )
        else:
            flash("Manutenção não encontrada.", "erro")

    except Exception as erro:
        print("ERRO AO EXCLUIR MANUTENCAO:", repr(erro))
        flash("Não foi possível excluir a manutenção.", "erro")

    return redirect(url_for("manutencoes.remover_lista"))
