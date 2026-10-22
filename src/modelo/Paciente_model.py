
from src.modelo.Utilizador_model import Utilizador

class Paciente(Utilizador):
    def __init__(self, id_paciente, nome, idade, genero, contacto):
        self.id_paciente = id_paciente
        super().__init__(id_paciente, nome)
        self.idade = idade
        self.genero = genero
        self.contacto = contacto

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do paciente deve ser um inteiro positivo.")
        self._id_paciente = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Nome do paciente deve ser uma string não vazia.")
        self._nome = value

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Idade do paciente deve ser um inteiro não negativo.")
        self._idade = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Gênero do paciente deve ser uma string não vazia.")
        self._genero = value

    @property
    def contacto(self):
        return self._contacto

    @contacto.setter
    def contacto(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Contacto do paciente deve ser uma string não vazia.")
        self._contacto = value

    def resumo(self):
        return f"ID: {self.id_paciente}, Nome: {self.nome}, Idade: {self.idade}, Gênero: {self.genero}, Contacto: {self.contacto}"