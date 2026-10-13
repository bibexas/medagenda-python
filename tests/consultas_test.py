import unittest
from  src.consultas import resumo_consulta

class TestProjeto(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()

##python -m unittest discover -s tests -p "*_test.py"