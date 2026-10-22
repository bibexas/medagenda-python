import unittest
from src.modelo.Consulta_model import Consulta
from src.modelo.Medico_model import Medico
from src.modelo.Paciente_model import Paciente
from  src.consultas import resumo_consulta

class TestProjeto(unittest.TestCase):
    #old code
    def test_caso_valido(self):
        resultado = resumo_consulta("Consulta A", 30, "confirmada")
        self.assertEqual(resultado, ("Consulta A", True, True))

    def test_nome_vazio(self):
        resultado = resumo_consulta("", 45, "pendente")
        self.assertEqual(resultado, ("Sem identificação", True, True))

    def test_duracao_invalida(self):
        resultado = resumo_consulta("Consulta C", 5, "confirmada")
        self.assertEqual(resultado, ("Consulta C", False, True))

    def test_estado_nao_aceite(self):
        resultado = resumo_consulta("Consulta D", 70, "cancelada")
        self.assertEqual(resultado, ("Consulta D", True, False))

    #new code
    #Teste 1: criação de uma consulta com paciente e médico válidos. 

    def test_criacao_consulta_valida(self):
        paciente = Paciente(id_paciente=1, nome="João Silva", idade=30, genero="Masculino", contacto="123456789")
        medico = Medico(id_medico=1, nome="Dr. Maria Oliveira", especialidade="Cardiologia", contacto="987654321")
        consulta = Consulta(id_consulta=1, id_paciente=paciente.id_paciente, id_medico=medico.id_medico, hora="09:00", data_consulta="2023-10-15", motivo="Consulta de rotina")
        
        self.assertEqual(consulta.id_consulta, 1)
        self.assertEqual(consulta.id_paciente, paciente.id_paciente)
        self.assertEqual(consulta.id_medico, medico.id_medico)
        self.assertEqual(consulta.hora, "09:00")
        self.assertEqual(consulta.data_consulta, "2023-10-15")
        self.assertEqual(consulta.motivo, "Consulta de rotina")

    # Teste 2: rejeição de um atributo inválido (nome do paciente vazio).

    def test_rejeita_nome_paciente_vazio(self):
        with self.assertRaises(ValueError):
            Paciente(
                id_paciente=1,
                nome="",
                idade=30,
                genero="Masculino",
                contacto="123456789",
            ) # if passes, means that there is an empty vallue



if __name__ == "__main__":
    unittest.main()

##python -m unittest discover -s tests -p "*_test.py"