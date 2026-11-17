from src.modelo.Paciente_model import Paciente
from src.modelo.Utilizador_model import Utilizador
from src.base_dados import (criar_tabela, adicionar_paciente, listar_pacientes)

def demonstrar():
    criar_tabela()
    adicionar_paciente(Paciente(1, "Ana", 24, "F", "912345678"), Paciente(2, "Rui", 31, "M", "923456789"))
    listar_pacientes()

for paciente in listar_pacientes():
    print(paciente.resumo())
 
 
if __name__ == "__main__":
    demonstrar()