# MedAgenda

## Objetivo da Aplicação: 
Aplicação para a gestão de consultas médicas num hospital/clínica. O objetivo principal é evitar sobreposições de horários e esquecimentos nas marcações, facilitando a gestão da agenda dos médicos.

## Elementos do Grupo:
Ana Gomes
Janaira Batista
Pedro Malheiro
Renato Duarte

## Atividade Captiulo 9 - Flask MedAgenda

# Instalar o Flask e o ambiente virtual
    python -m venv .venv       # só se faltar
    source .venv/Scripts/activate
    python -m pip show flask
    python -m pip install flask  # só se faltar

# Criação do ficheiro app.py

# Executar a aplicação
    No ficheiro app.py:
        python -m flask --app app:app run --debug
    Para fechar: CTRL + C 

# Na aplicação Bruno (histórico):
    127.0.0.1 - - [19/Nov/2026 12:06:15] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [19/Nov/2026 12:07:09] "GET /pacientes HTTP/1.1" 200 -
    127.0.0.1 - - [19/Nov/2026 12:07:54] "POST /pacientes HTTP/1.1" 400 -
    127.0.0.1 - - [19/Nov/2026 12:09:55] "POST /pacientes HTTP/1.1" 400 -
    127.0.0.1 - - [19/Nov/2026 12:13:59] "POST /pacientes HTTP/1.1" 201 -
    127.0.0.1 - - [19/Nov/2026 12:14:26] "GET /pacientes HTTP/1.1" 200 -
