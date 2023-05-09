
class Pessoa():

    __slots__ = ['_nome','_endereco','_cpf','_data']

    def __init__(self, nome, endereco, cpf, data):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._data = data

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @property
    def cpf(self):
        return self._cpf

    @property
    def data(self):
        return self._data

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco