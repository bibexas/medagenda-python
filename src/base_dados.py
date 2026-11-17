from contextlib import closing
from src.modelo.Paciente_model import Paciente
import sqlite3

def criar_tabela(caminho="medagenda.db"):
    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute("""
                CREATE TABLE IF NOT EXISTS pacientes (
                    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
                    idade INTEGER NOT NULL,
                    genero TEXT NOT NULL,
                    contacto TEXT NOT NULL
                )
            """)

def adicionar_paciente(paciente, caminho="medagenda.db"):
    dados = paciente.para_dicionario_paciente()
 
    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute(
                "INSERT INTO pacientes (id_paciente, idade, genero, contacto) VALUES (?, ?, ?, ?)",
                (dados["id_paciente"], dados["idade"], dados["genero"], dados["contacto"])
            )
 
 
def listar_pacientes(caminho="medagenda.db"):
    with closing(sqlite3.connect(caminho)) as ligacao:
        linhas = ligacao.execute(
            "SELECT nome, idade FROM pacientes"
        ).fetchall()
 
    return [Paciente(nome, idade) for nome, idade in linhas]