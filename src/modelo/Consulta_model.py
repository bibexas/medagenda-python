
class Consulta:
    def __init__(self, id_consulta, id_paciente, nome_paciente, id_medico, data_consulta, hora, motivo):
        self.id_consulta = id_consulta
        self.id_paciente = id_paciente
        self.nome_paciente = nome_paciente
        self.id_medico = id_medico
        self.data_consulta = data_consulta
        self.hora = hora
        self.motivo = motivo

    @property
    def id_consulta(self):
        return self._id_consulta

    @id_consulta.setter
    def id_consulta(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID da consulta deve ser um inteiro positivo.")
        self._id_consulta = value

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do paciente deve ser um inteiro positivo.")
        self._id_paciente = value

    @property
    def id_medico(self):
        return self._id_medico

    @id_medico.setter
    def id_medico(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do médico deve ser um inteiro positivo.")
        self._id_medico = value

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Hora da consulta deve ser uma string não vazia.")
        self._hora = value

    @property
    def motivo(self):
        return self._motivo

    @motivo.setter
    def motivo(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Motivo da consulta deve ser uma string não vazia.")
        self._motivo = value

    @property
    def data_consulta(self):
        return self._data_consulta

    @data_consulta.setter
    def data_consulta(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Data da consulta deve ser uma string não vazia.")
        self._data_consulta = value

    @property
    def nome_paciente(self):
        return self._nome_paciente

    @nome_paciente.setter
    def nome_paciente(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Nome do paciente deve ser uma string não vazia.")
        self._nome_paciente = value

    #2. Criar Consulta com referências a um Paciente e a um Medico e atributo de data/hora. Implementar um método resumo() que consulte o estado. 
    def resumo(self):
        return f"Consulta ID: {self.id_consulta}, Paciente ID: {self.id_paciente}, Nome do Paciente: {self.nome_paciente}, Data da Consulta: {self.data_consulta}, Hora: {self.hora}, Motivo: {self.motivo}"

    @classmethod
    def de_dicionario(cls, dicionario):
        return cls(
            id_consulta=dicionario.get("id_consulta"),
            id_paciente=dicionario.get("id_paciente"),
            nome_paciente=dicionario.get("nome_paciente"),
            id_medico=dicionario.get("id_medico"),
            data_consulta=dicionario.get("data_consulta"),
            hora=dicionario.get("hora"),
            motivo=dicionario.get("motivo")
        )

    def para_dicionario(self):
        return {
            "id_consulta": self.id_consulta,
            "id_paciente": self.id_paciente,
            "nome_paciente": self.nome_paciente,
            "id_medico": self.id_medico,
            "data_consulta": self.data_consulta,
            "hora": self.hora,
            "motivo": self.motivo
        }

    def criarconsulta(self, paciente, medico, data_consulta, hora, motivo):
        self.id_paciente = paciente.id_paciente
        self.nome_paciente = paciente.nome
        self.id_medico = medico.id_medico
        self.data_consulta = data_consulta
        self.hora = hora
        self.motivo = motivo