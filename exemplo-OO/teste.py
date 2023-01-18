
#Arquivo com uns códigos de teste

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular,
             "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("saldo é {}".format(conta["saldo"]))

#-----------------

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{:02d}/{:02d}/{}".format(self.dia,self.mes,self.ano))

#data = Data(1, 1, 2007)
#data.formatada()

# ---------------------
class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area
