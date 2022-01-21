class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(self.pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def __pode_sacar(self, valor_sacar):
        valor_disponivel_saque = (self.__saldo + self.limite)
        return valor_sacar <= valor_disponivel_saque

    def transferir(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.saca(valor)


    #Getters e Setters
    @property
    def saldo(self):
        return self.__saldo

    property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
