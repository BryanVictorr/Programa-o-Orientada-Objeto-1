class Cliente():

    __slots__ = ['_nome','_cpf','_senha','_nascimento','_genero','_saldo']

    def __init__(self,nome, cpf, senha, nascimento, genero, saldo = 0.0):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self._nascimento = nascimento
        self._genero = genero
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def senha(self):
        return self._senha

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def genero(self):
        return self._genero

    @property
    def saldo(self):
        return (self._saldo)

    def deposito(self,valor):

        if(valor > 0.0):
            self._saldo += valor
            return self._saldo
        else:
            return False

    def saque(self, valor):

        if(valor <= self._saldo) and (valor > 0.0):
            self._saldo -= valor
            return self._saldo
        else:
            return -1

    def transfere(self, destino, valor):

        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            destino._saldo += valor
            return self._saldo, destino._saldo