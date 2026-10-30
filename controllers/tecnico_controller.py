
from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.tecnico import (
    listar_tecnicos,
    buscar_tecnico,
    cadastrar_tecnico,
    atualizar_tecnico,
    excluir_tecnico
)

tecnico_bp = Blueprint("tecnicos", __name__)


# LISTAR TÉCNICOS
@tecnico_bp.route("/tecnicos")
def listar():
    tecnicos = listar_tecnicos()

    return render_template(
        "tecnicos.html",
        tecnicos=tecnicos,
        tecnico_edicao=None
    )


# LISTAR TÉCNICOS PARA ATUALIZAÇÃO
@tecnico_bp.route("/tecnicos/atualizar")
def atualizar_lista():
    tecnicos = listar_tecnicos()

    return render_template(
        "atualizar_tecnicos.html",
        tecnicos=tecnicos
    )


# LISTAR TÉCNICOS PARA REMOÇÃO
@tecnico_bp.route("/tecnicos/remover")
def remover_lista():
    tecnicos = listar_tecnicos()

    return render_template(
        "remover_tecnicos.html",
        tecnicos=tecnicos
    )


# CADASTRAR OU ATUALIZAR TÉCNICO
@tecnico_bp.route("/tecnicos/salvar", methods=["POST"])
def salvar():
    id_tecnico = request.form.get("id_tecnico", "").strip()
    nome = request.form.get("nome", "").strip()
    especialidade = request.form.get("especialidade", "").strip()

    if not nome or not especialidade:
        flash("Preencha o nome e a especialidade do técnico.", "erro")
        return redirect(url_for("tecnicos.listar"))

    try:
        if id_tecnico:
            id_tecnico = int(id_tecnico)

            alterados = atualizar_tecnico(
                id_tecnico,
                nome,
                especialidade
            )

            if alterados:
                return redirect(
                    url_for(
                        "tecnicos.atualizacao_concluida",
                        id_tecnico=id_tecnico
                    )
                )
            else:
                flash("Técnico não encontrado.", "erro")

        else:
            cadastrar_tecnico(nome, especialidade)

            return redirect(
                url_for("tecnicos.cadastro_concluido")
            )

    except Exception as erro:
        print("ERRO AO SALVAR TECNICO:", repr(erro))
        flash("Não foi possível salvar o técnico.", "erro")

    return redirect(url_for("tecnicos.listar"))


# TELA DE CONFIRMAÇÃO DO CADASTRO
@tecnico_bp.route("/tecnicos/cadastro-concluido")
def cadastro_concluido():
    return render_template("tecnico_cadastrado.html")


# TELA DE CONFIRMAÇÃO DA ATUALIZAÇÃO
@tecnico_bp.route("/tecnicos/atualizacao-concluida/<int:id_tecnico>")
def atualizacao_concluida(id_tecnico):
    tecnico = buscar_tecnico(id_tecnico)

    if tecnico is None:
        flash("Técnico não encontrado.", "erro")
        return redirect(url_for("tecnicos.atualizar_lista"))

    return render_template(
        "tecnico_atualizado.html",
        tecnico=tecnico
    )


# EDITAR TÉCNICO
@tecnico_bp.route("/tecnicos/editar/<int:id_tecnico>")
def editar(id_tecnico):
    tecnico = buscar_tecnico(id_tecnico)

    if tecnico is None:
        flash("Técnico não encontrado.", "erro")
        return redirect(url_for("tecnicos.listar"))

    tecnicos = listar_tecnicos()

    return render_template(
        "tecnicos.html",
        tecnicos=tecnicos,
        tecnico_edicao=tecnico
    )


# TELA DE CONFIRMAÇÃO DA EXCLUSÃO
@tecnico_bp.route("/tecnicos/exclusao-concluida")
def exclusao_concluida():
    return render_template("tecnico_excluido.html")


# EXCLUIR TÉCNICO
@tecnico_bp.route(
    "/tecnicos/excluir/<int:id_tecnico>",
    methods=["POST"]
)
def excluir(id_tecnico):
    try:
        excluidos = excluir_tecnico(id_tecnico)

        if excluidos:
            return redirect(
                url_for("tecnicos.exclusao_concluida")
            )
        else:
            flash("Técnico não encontrado.", "erro")

    except Exception as erro:
        print("ERRO AO EXCLUIR TECNICO:", repr(erro))

        if "ORA-02292" in str(erro):
            flash(
                "Este técnico possui manutenções vinculadas "
                "e não pode ser excluído.",
                "erro"
            )
        else:
            flash("Não foi possível excluir o técnico.", "erro")

    return redirect(url_for("tecnicos.remover_lista"))
