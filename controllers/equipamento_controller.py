
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from models.equipamento import (
    listar_equipamentos,
    buscar_equipamento,
    cadastrar_equipamento,
    atualizar_equipamento,
    excluir_equipamento
)

equipamento_bp = Blueprint("equipamentos", __name__)


# LISTAR EQUIPAMENTOS
@equipamento_bp.route("/equipamentos")
def listar():
    equipamentos = listar_equipamentos()

    return render_template(
        "equipamentos.html",
        equipamentos=equipamentos,
        equipamento_edicao=None
    )


# LISTAR EQUIPAMENTOS PARA REMOÇÃO
@equipamento_bp.route("/equipamentos/remover")
def remover_lista():
    equipamentos = listar_equipamentos()

    return render_template(
        "remover_equipamentos.html",
        equipamentos=equipamentos
    )


# LISTAR EQUIPAMENTOS PARA ATUALIZAÇÃO
@equipamento_bp.route("/equipamentos/atualizar")
def atualizar_lista():
    equipamentos = listar_equipamentos()

    return render_template(
        "atualizar_equipamentos.html",
        equipamentos=equipamentos
    )


# CADASTRAR OU ATUALIZAR EQUIPAMENTO
@equipamento_bp.route("/equipamentos/salvar", methods=["POST"])
def salvar():
    id_equipamento = request.form.get("id_equipamento", "").strip()
    nome = request.form.get("nome", "").strip()
    modelo = request.form.get("modelo", "").strip()
    numero_serie = request.form.get("numero_serie", "").strip()
    status = request.form.get("status", "").strip()

    if not nome or not modelo or not numero_serie:
        flash("Preencha todos os campos obrigatórios.", "erro")
        return redirect(url_for("equipamentos.listar"))

    if status not in ("DISPONIVEL", "EM_MANUTENCAO", "INATIVO"):
        flash("Selecione um status válido.", "erro")
        return redirect(url_for("equipamentos.listar"))

    try:
        if id_equipamento:
            id_equipamento = int(id_equipamento)

            alterados = atualizar_equipamento(
                id_equipamento,
                nome,
                modelo,
                numero_serie,
                status
            )

            if alterados:
                return redirect(
                    url_for(
                        "equipamentos.atualizacao_concluida",
                        id_equipamento=id_equipamento
                    )
                )
            else:
                flash("Equipamento não encontrado.", "erro")

        else:
            cadastrar_equipamento(
                nome,
                modelo,
                numero_serie,
                status
            )

            return redirect(
                url_for("equipamentos.cadastro_concluido")
            )

    except Exception as erro:
        print("ERRO AO SALVAR EQUIPAMENTO:", repr(erro))

        if "ORA-00001" in str(erro):
            flash("Esse número de série já está cadastrado.", "erro")
        else:
            flash("Não foi possível salvar o equipamento.", "erro")

    return redirect(url_for("equipamentos.listar"))


# TELA DE CONFIRMAÇÃO DO CADASTRO
@equipamento_bp.route("/equipamentos/cadastro-concluido")
def cadastro_concluido():
    return render_template("equipamento_cadastrado.html")


# EDITAR EQUIPAMENTO
@equipamento_bp.route("/equipamentos/editar/<int:id_equipamento>")
def editar(id_equipamento):
    equipamento = buscar_equipamento(id_equipamento)

    if equipamento is None:
        flash("Equipamento não encontrado.", "erro")
        return redirect(url_for("equipamentos.listar"))

    equipamentos = listar_equipamentos()

    return render_template(
        "equipamentos.html",
        equipamentos=equipamentos,
        equipamento_edicao=equipamento
    )


# EXIBIR EQUIPAMENTO APÓS ATUALIZAÇÃO
@equipamento_bp.route(
    "/equipamentos/atualizacao-concluida/<int:id_equipamento>"
)
def atualizacao_concluida(id_equipamento):
    equipamento = buscar_equipamento(id_equipamento)

    if equipamento is None:
        flash("Equipamento não encontrado.", "erro")
        return redirect(url_for("equipamentos.atualizar_lista"))

    return render_template(
        "equipamento_atualizado.html",
        equipamento=equipamento
    )


# TELA DE CONFIRMAÇÃO DA EXCLUSÃO
@equipamento_bp.route("/equipamentos/exclusao-concluida")
def exclusao_concluida():
    return render_template("equipamento_excluido.html")


# EXCLUIR EQUIPAMENTO
@equipamento_bp.route(
    "/equipamentos/excluir/<int:id_equipamento>",
    methods=["POST"]
)
def excluir(id_equipamento):
    try:
        excluidos = excluir_equipamento(id_equipamento)

        if excluidos:
            return redirect(
                url_for("equipamentos.exclusao_concluida")
            )
        else:
            flash("Equipamento não encontrado.", "erro")

    except Exception as erro:
        print("ERRO AO EXCLUIR EQUIPAMENTO:", repr(erro))

        if "ORA-02292" in str(erro):
            flash(
                "Não é possível excluir este equipamento porque "
                "existem manutenções vinculadas a ele.",
                "erro"
            )
        else:
            flash("Não foi possível excluir o equipamento.", "erro")

    return redirect(url_for("equipamentos.remover_lista"))
