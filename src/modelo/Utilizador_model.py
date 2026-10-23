
class Utilizador:
    category = "Utilizador"

    def __init__(self, id_utilizador, nome):
        self.id_utilizador = id_utilizador
        self.nome = nome

    @property
    def id_utilizador(self):
        return self._id_utilizador

    @id_utilizador.setter
    def id_utilizador(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do utilizador deve ser um inteiro positivo.")
        self._id_utilizador = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Nome do utilizador deve ser uma string não vazia.")
        self._nome = value