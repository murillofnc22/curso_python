class EvolucaoHumana(object):
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'


if __name__ == '__main__':
    jose = EvolucaoHumana('José')
    grokn = EvolucaoHumana('Grokn')
    grokn.das_cavernas()

    print(f'EvolucaoHumana.especie: {EvolucaoHumana.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')

    EvolucaoHumana.especie = 'Homo Sapiens Sapiens'
    print(f'EvolucaoHumana.especie: {EvolucaoHumana.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')
