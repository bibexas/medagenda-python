from src.modelo.Paciente_model import Paciente
from src.modelo.Medico_model import Medico
from src.modelo.Consulta_model import Consulta



#No main.py, criar um paciente, um médico e uma consulta; apresentar os dados associados.

## Criar um paciente
paciente1 = Paciente(id_paciente=1, nome="João Silva", idade=30, genero="Masculino", contacto="123456789")
print(paciente1.resumo())

## Criar um médico
medico1 = Medico(id_medico=1, nome="Dr. Maria Oliveira", especialidade="Cardiologia", contacto="987654321")
print(medico1.resumo())

## Criar uma consulta 
consulta1 = Consulta(id_consulta=1, id_paciente=1, id_medico=1, hora="09:00", data_consulta="2023-10-15", motivo="Consulta de rotina")
print(consulta1.resumo())
