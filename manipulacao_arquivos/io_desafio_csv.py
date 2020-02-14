import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('utf-8')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://www.geoservicos.ibge.gov.br/geoserver/wms?service=WFS&version=1.0.0&request=GetFeature&typeName=CGEO:RedeUrbanaSintese_Regic2007&outputFormat=CSV')
