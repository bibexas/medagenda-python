from contextlib import closing
from src.modelo.Paciente_model import Paciente
import sqlite3


def criar_tabela(caminho="dados/medagenda.db"):
    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute("""
                CREATE TABLE IF NOT EXISTS pacientes (
                    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    genero TEXT NOT NULL,
                    contacto TEXT NOT NULL
                )
            """)


def adicionar_paciente(paciente, caminho="dados/medagenda.db"):
    dados = paciente.para_dicionario_paciente()

    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute(
                "INSERT INTO pacientes (nome, idade, genero, contacto) VALUES (?, ?, ?, ?)",
                (dados["nome"], dados["idade"],
                 dados["genero"], dados["contacto"])
            )


def listar_pacientes(caminho="dados/medagenda.db"):
    with closing(sqlite3.connect(caminho)) as ligacao:
        linhas = ligacao.execute(
            "SELECT id_paciente, nome, idade, genero, contacto FROM pacientes"
        ).fetchall()

    return [Paciente(id_paciente, nome, idade, genero, contacto)
            for id_paciente, nome, idade, genero, contacto in linhas]
