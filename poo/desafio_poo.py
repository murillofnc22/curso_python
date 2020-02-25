from datetime import datetime
from functools import reduce


class Compra(object):
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


MaiorIdade = 18


class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome

        return f'Nome: {self.nome} - Idade: {self.idade}'

    def isAdulto(self):
        return (self.idade or 0) > MaiorIdade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        return None if not self.compras else sorted(self.compras, key=lambda compra: compra.data)[-1].data

    def total_compras(self):
        return reduce(lambda c1, c2: c1 + c2, (compra.valor for compra in self.compras))


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


def main():
    juracy = Cliente('Juracy Filho', 44)
    leo = Vendedor('Leonardo Leitão', 36, 1000)
    compra1 = Compra(leo, datetime.now(), 512)
    compra2 = Compra(leo, datetime(2018, 6, 4), 256)
    juracy.registrar_compra(compra1)
    juracy.registrar_compra(compra2)

    print(f'Cliente: {juracy}', '(adulto)' if juracy.isAdulto() else '')
    print(f'Vendedor: {leo}')
    print(f'Total: {juracy.total_compras()} em {len(juracy.compras)} compras.')
    print(f'Última compra: {juracy.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
