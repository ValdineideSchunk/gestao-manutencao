from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.tecnico import (
    listar_tecnicos,
    buscar_tecnico,
    cadastrar_tecnico,
    atualizar_tecnico,
    excluir_tecnico
)

tecnico_bp = Blueprint("tecnicos", __name__)


@tecnico_bp.route("/tecnicos")
def listar():
    tecnicos = listar_tecnicos()

    return render_template(
        "tecnicos.html",
        tecnicos=tecnicos,
        tecnico_edicao=None
    )


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
            atualizar_tecnico(
                int(id_tecnico),
                nome,
                especialidade
            )
            flash("Técnico atualizado com sucesso!", "sucesso")
        else:
            cadastrar_tecnico(nome, especialidade)
            flash("Técnico cadastrado com sucesso!", "sucesso")

    except Exception as erro:
        print("ERRO AO SALVAR TECNICO:", repr(erro))
        flash("Não foi possível salvar o técnico.", "erro")

    return redirect(url_for("tecnicos.listar"))


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


@tecnico_bp.route("/tecnicos/excluir/<int:id_tecnico>", methods=["POST"])
def excluir(id_tecnico):
    try:
        excluidos = excluir_tecnico(id_tecnico)

        if excluidos:
            flash("Técnico excluído com sucesso!", "sucesso")
        else:
            flash("Técnico não encontrado.", "erro")

    except Exception as erro:
        print("ERRO AO EXCLUIR TECNICO:", repr(erro))

        if "ORA-02292" in str(erro):
            flash(
                "Este técnico possui manutenções vinculadas e não pode ser excluído.",
                "erro"
            )
        else:
            flash("Não foi possível excluir o técnico.", "erro")

    return redirect(url_for("tecnicos.listar"))