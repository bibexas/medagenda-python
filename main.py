import json
from src.modelo.Paciente_model import Paciente
from src.modelo.Medico_model import Medico
from src.modelo.Consulta_model import Consulta
from pathlib import Path




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



def registar_paciente(id_paciente, nome, idade, genero, contacto):      #id será == a numero de sns
    paciente = Paciente(id_paciente=id_paciente, nome=nome, idade=idade, genero=genero, contacto=contacto)
    path_data["paciente"].append(paciente.para_dicionario()) #add to json file

    with open(dados, "w", encoding="utf-8") as f:
        json.dump(path_data, f, ensure_ascii=False, indent=4)

    return paciente

def registar_medico(id_medico, nome, especialidade, contacto):        #id será == a numero de sns
    id_medico = len(path_data["medico"]) + 1
    medico = Medico(id_medico=id_medico, nome=nome, especialidade=especialidade, contacto=contacto)
    path_data["medico"].append(medico.para_dicionario())
    with open(dados, "w", encoding="utf-8") as f:
        json.dump(path_data, f, ensure_ascii=False, indent=4)
    return medico

def registar_consulta(paciente, medico, data_consulta, hora, motivo):
    id_consulta = len(path_data["consulta"]) + 1
    consulta = Consulta(id_consulta, buscar_paciente_por_nome(paciente.nome), buscar_medico_por_nome(medico.nome), data_consulta, hora, motivo)
    path_data["consulta"].append(consulta.para_dicionario())
    with open(dados, "w", encoding="utf-8") as f:
        json.dump(path_data, f, ensure_ascii=False, indent=4)
    return consulta

def buscar_paciente_por_nome(nome):
    for paciente in path_data["paciente"]:
        if paciente["nome"] == nome:
            return Paciente.de_dicionario(paciente)
    return None

def buscar_medico_por_nome(nome):
    for medico in path_data["medico"]:
        if medico["nome"] == nome:
            return Medico.de_dicionario(medico)
    return None

paciente4 = Paciente(id_paciente=4, nome="João gomes", idade=30, genero="Masculino", contacto="912345678")
registar_paciente(paciente4.id_paciente, paciente4.nome, paciente4.idade, paciente4.genero, paciente4.contacto)
#menu principal
while True:
    print("\nMenu Principal:")
    print("1. Registar Paciente")
    print("2. Registar Médico")
    print("3. Registar Consulta")
    print("4. Listar Pacientes")
    print("5. Listar Médicos")
    print("6. Listar Consultas")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_paciente = int(input("ID do Paciente: "))
        nome = input("Nome do Paciente: ")
        idade = int(input("Idade do Paciente: "))
        genero = input("Gênero do Paciente: ")
        contacto = input("Contacto do Paciente: ")
        paciente = registar_paciente(id_paciente, nome, idade, genero, contacto)
        print(f"Paciente {paciente.nome} registado com sucesso!")

    elif opcao == "2":
        id_medico = int(input("ID do Médico: "))
        nome = input("Nome do Médico: ")
        especialidade = input("Especialidade do Médico: ")
        contacto = input("Contacto do Médico: ")
        medico = registar_medico(id_medico, nome, especialidade, contacto)
        print(f"Médico {medico.nome} registado com sucesso!")

    elif opcao == "3":
        nome_paciente = input("Nome do Paciente para a Consulta: ")
        paciente = buscar_paciente_por_nome(nome_paciente)
        if not paciente:
            print(f"Paciente {nome_paciente} não encontrado.")
            continue

        nome_medico = input("Nome do Médico para a Consulta: ")
        medico = buscar_medico_por_nome(nome_medico)
        if not medico:
            print(f"Médico {nome_medico} não encontrado.")
            continue

        data_consulta = input("Data da Consulta (DD-MM-YYYY): ")
        hora = input("Hora da Consulta (HH:MM): ")
        motivo = input("Motivo da Consulta: ")

        consulta = registar_consulta(paciente, medico, data_consulta, hora, motivo)
        print(f"Consulta registada com sucesso para o paciente {paciente.nome} com o médico {medico.nome}.")

    elif opcao == "4":
        print("\nLista de Pacientes:")
        for paciente in path_data["paciente"]:
            print(f"  - {paciente['nome']} (ID: {paciente['id_paciente']})")
        print(f"Total de Pacientes: {len(path_data['paciente'])}")

    elif opcao == "5":
        print("\nLista de Médicos:")
        for medico in path_data["medico"]:
            print(f"  - {medico['nome']} (ID: {medico['id_medico']})")
        print(f"Total de Médicos: {len(path_data['medico'])}")

    elif opcao == "6":
        print("\nLista de Consultas:")
        for consulta in path_data["consulta"]:
            print(f"  - Consulta ID: {consulta['id_consulta']}, Paciente: {consulta['nome_paciente']}, Médico ID: {consulta['id_medico']}, Data: {consulta['data_consulta']}, Hora: {consulta['hora']}, Motivo: {consulta['motivo']}")
        print(f"Total de Consultas: {len(path_data['consulta'])}")

    elif opcao == "7":
        print("A sair...")
        break

    else:
        print("Opção inválida. Tente novamente.")