class Carro:
    def __init__(self):
        pass
        # self.motor = Motor()
        # self.direcao = Direcao()

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0

class Direcao:
    def __init__(self):
        self.valor = 'Norte'

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'

    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'

    >>>motor = Motor()
    motor.velocidade
    0