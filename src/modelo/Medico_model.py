
from src.modelo.Utilizador_model import Utilizador

class Medico(Utilizador):
    category = "Medico"
    def __init__(self, id_medico, nome, especialidade, contacto):
        super().__init__(id_medico, nome)
        self.id_medico = id_medico
        self.especialidade = especialidade
        self.contacto = contacto

    @property
    def id_medico(self):
        return self._id_medico
    @id_medico.setter
    def id_medico(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do médico deve ser um inteiro positivo.")
        self._id_medico = value

    @property
    def especialidade(self):
        return self._especialidade
    @especialidade.setter
    def especialidade(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Especialidade do médico deve ser uma string não vazia.")
        self._especialidade = value

    @property
    def contacto(self):
        return self._contacto

    @contacto.setter
    def contacto(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Contacto do médico deve ser uma string não vazia.")
        self._contacto = value

    def resumo(self):
        return f"ID: {self.id_medico}, Nome: {self.nome}, Especialidade: {self.especialidade}, Contacto: {self.contacto}"


    @classmethod
    def de_dicionario(cls, dicionario):
        return cls(
            id_medico=dicionario.get("id_medico"),
            nome=dicionario.get("nome"),
            especialidade=dicionario.get("especialidade"),
            contacto=dicionario.get("contacto")
        )

    def para_dicionario(self):
        return {
            "id_medico": self.id_medico,
            "nome": self.nome,
            "especialidade": self.especialidade,
            "contacto": self.contacto
        }