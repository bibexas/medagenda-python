def resumo_consulta(nome, duracao, estado):
    nome = nome.strip()

    if nome == "":
        nome = "Sem identificação"

    duracao = int(duracao)  # Convertendo a duração para inteiro

    if 15 <= duracao <= 120:
        valor_valido = True
    else: 
        valor_valido = False

    estado_aceite = estado in {"confirmada", "pendente"}

    return (nome, valor_valido, estado_aceite)

def desempacotar_tuple(tupla):
    nome, valor_valido, estado_aceite = tupla
    print(f"Identificação: {nome} | Valor válido: {valor_valido} | Estado aceite: {estado_aceite}")
