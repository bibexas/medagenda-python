from flask import Flask, jsonify, request
from src.base_dados import adicionar_paciente, criar_tabela, listar_pacientes as listar_pacientes_db
from src.modelo.Paciente_model import Paciente

app = Flask(__name__)

@app.get('/')
def inicio():
    return "Bem-vindo à aplicação MedAgenda!"


criar_tabela()

@app.get("/pacientes")
def listar_pacientes():
    dados = [paciente.para_dicionario_paciente() for paciente in listar_pacientes_db()]
    return jsonify(dados), 200

@app.post("/pacientes")
def criar_paciente():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"error": "Dados inválidos"}), 400
    try:
        p = Paciente.de_dicionario(dados)
        adicionar_paciente(p)
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Dados inválidos"}), 400
    return jsonify(p.para_dicionario_paciente()), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
