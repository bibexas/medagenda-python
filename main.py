import json
from src.modelo.Paciente_model import Paciente
from src.modelo.Medico_model import Medico
from src.modelo.Consulta_model import Consulta
from pathlib import Path



#No main.py, criar um paciente, um médico e uma consulta; apresentar os dados associados.

## Criar um paciente
paciente1 = Paciente(id_paciente=1, nome="João Silva", idade=30, genero="Masculino", contacto="123456789")
## Criar um médico
medico1 = Medico(id_medico=1, nome="Dr. Maria Oliveira", especialidade="Cardiologia", contacto="987654321")
## Criar uma consulta 
consulta1 = Consulta( id_consulta=1, id_paciente=1, nome_paciente="João Silva", id_medico=1, hora="10:00", data_consulta="2023-10-15", motivo="Consulta de rotina")
#consulta1.criarconsulta(paciente=paciente1, medico=medico1, data_consulta="2023-10-15", hora="10:00", motivo="Consulta de rotina")


dados = Path(__file__).parent / "dados.json"
if dados.exists():  # Verifica se o arquivo existe
    with open(dados, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()
else:
    conteudo = ""



path_data = json.loads(conteudo) if conteudo else {}    # Carrega os dados do arquivo JSON, se existir
if not isinstance(path_data, dict):
    raise ValueError("dados.json deve conter um objeto JSON.")


for categoria in ("paciente", "medico", "consulta"):  # Verifica se as categorias existem no dicionário, caso contrário, inicializa como listas vazias
    if categoria not in path_data:
        path_data[categoria] = []
    elif isinstance(path_data[categoria], dict):
        path_data[categoria] = [path_data[categoria]]


# Escrever os dados do paciente, médico e consulta no arquivo JSON.
def escrever_dados(paciente, medico, consulta): 
    registos = {        # Dicionário com os dados a serem escritos
        "paciente": (paciente.para_dicionario(), "id_paciente"),
        "medico": (medico.para_dicionario(), "id_medico"),
        "consulta": (consulta.para_dicionario(), "id_consulta"),
    }

    for categoria, (novo_registo, campo_id) in registos.items(): # Verifica se o registro já existe
        lista = path_data.setdefault(categoria, [])
        if not isinstance(lista, list):
            raise ValueError(f"'{categoria}' deve ser uma lista no dados.json.")

        registo_existente = next(
            (
                registo
                for registo in lista
                if registo.get(campo_id) == novo_registo[campo_id]
            ),
            None,
        )
        if registo_existente is None: # Adiciona o novo registro se não existir
            lista.append(novo_registo)
        else:
            registo_existente.update(novo_registo) # Atualiza o registro existente com os novos dados

    with dados.open("w", encoding="utf-8") as arquivo: # Escreve os dados atualizados no arquivo JSON
        json.dump(path_data, arquivo, indent=4, ensure_ascii=False)



paciente2 = Paciente(id_paciente=2, nome="Ana Costa", idade=25, genero="Feminino", contacto="987654321")
medico2 = Medico(id_medico=2, nome="Dr. Pedro Santos", especialidade="Dermatologia", contacto="123456789")
consulta2 = Consulta(id_consulta=2, id_paciente=2, nome_paciente="Ana Costa", id_medico=2, hora="14:30", data_consulta="2023-10-20", motivo="Consulta de pele")


escrever_dados(paciente2, medico2, consulta2)
escrever_dados(paciente1, medico1, consulta1)

#print json file content
#print pacientes
print("Pacientes:")
for paciente in path_data["paciente"]:
    print(f"  - {paciente['nome']} (ID: {paciente['id_paciente']})")

