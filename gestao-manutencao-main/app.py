

from flask import Flask, render_template
from config import obter_conexao
from controllers.equipamento_controller import equipamento_bp
from controllers.tecnico_controller import tecnico_bp
from controllers.manutencao_controller import manutencao_bp
from controllers.relatorio_controller import relatorio_bp

app = Flask(__name__)
app.secret_key = "chave-academica-gestao-manutencao"

app.register_blueprint(equipamento_bp)
app.register_blueprint(tecnico_bp)
app.register_blueprint(manutencao_bp)
app.register_blueprint(relatorio_bp)



@app.route("/")
def inicio():
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT
                    (SELECT COUNT(*) FROM EQUIPAMENTO),
                    (SELECT COUNT(*) FROM TECNICO),
                    (SELECT COUNT(*) FROM MANUTENCAO)
                FROM dual
            """)

            equipamentos, tecnicos, manutencoes = cursor.fetchone()

    return render_template(
        "index.html",
        equipamentos=equipamentos,
        tecnicos=tecnicos,
        manutencoes=manutencoes
    )


if __name__ == "__main__":
    app.run(debug=True)
