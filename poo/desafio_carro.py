
class Carro:
    def __init__(self, vel_maxima):
        self.vel_maxima = vel_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        self.velocidade_atual += delta
        return self.velocidade_atual if self.velocidade_atual <= self.vel_maxima else self.vel_maxima

    def frear(self, delta=5):
        self.velocidade_atual -= delta
        return 0 if self.velocidade_atual <= 0 else self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
