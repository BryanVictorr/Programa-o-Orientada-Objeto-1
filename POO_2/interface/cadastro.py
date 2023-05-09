class Cadastro():

    __slots__ = ['_lista_de_pessoas']

    def __init__(self):
        self._lista_de_pessoas = []

    def cadastro(self, pessoa):
        verificar = self.busca(pessoa.cpf)

        if(verificar == None):
            self._lista_de_pessoas.append(pessoa)
            return True
        else:
            return False

    def busca(self, cpf):
        for lista in self._lista_de_pessoas:
            if lista.cpf == cpf:
                return lista

        return None