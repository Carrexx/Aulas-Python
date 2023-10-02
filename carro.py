from distutils import core


class Carro():

    def _init_(self, cor, qt_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
        self.cor = cor
        self.qt_portas = qt_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        self.velocidade = velocidade

def abastecer(self, qtd_combustivel): #METODO DE ARGUMENTO
    self.qtd_combustivel += qtd_combustivel

def ligar(self):
    if self.is_ligado:
        print("O carro já está ligado")
    else:
        self.is_ligado = True
        print("O carro foi ligado")

def desligar(self):
    if self.is_ligado == False:
        print("O carro está desligado")
    else:
        self.is_ligado
        print("O carro foi ligado")

