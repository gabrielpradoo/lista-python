'''1)Faça um algoritmo para cadastrar até 10 imóveis a serem alugados ou vendidos, contendo os seguintes dados: tipo(loja, apartamento, casa, quitinete), endereço, bairro, valor, situação(aluguel ou venda). Ao final, solicitar ao usuário a situação a ser pesquisada e mostrar todos os dados dos imóveis enquadrados na solicitação.'''

from random import randint

properties_list = []

stores = []
apartaments = []
houses = []
loftis = []

aluguel = []
venda = []

properties_types = ['loja', 'apartamento', 'casa', 'quitinete']
properties_sit = ['aluguel', 'venda']


class Imovel:
    def __init__(self, tipo, endereco, bairro, valor, situacao):
        self.tipo = tipo
        self.endereco = endereco
        self.bairro = bairro
        self.valor = valor
        self.situacao = situacao

    def Cadastrar(self, imovel, i):
        if self.tipo in properties_types:

            properties_list.append(f'{imovel}{i+1}')
            if self.tipo == 'loja':
                stores.append(f'{imovel}{len(stores)}')

            elif self.tipo == 'apartamento':
                apartaments.append(f'{imovel}{len(apartaments)}')

            elif self.tipo == 'casa':
                houses.append(f'{imovel}{len(houses)}')

            elif self.tipo == 'quitinete':
                loftis.append(f'{imovel}{len(loftis)}')

        else:
            print('Digite uma opção válida!')

        if self.situacao in properties_sit:
            if self.situacao == 'aluguel':
                e = 1
                aluguel.append(f'{imovel}{e}')
                e += 1
            elif self.situacao == 'venda':
                f = 1
                venda.append(f'{imovel}{f}')
                f += 1
        else:
            print('Digite uma opção válida!')

    def __repr__(self):
        return str(self.__dict__)


def Filtrar(situacao):
    if situacao == 'Aluguel':
        for i in range(0, len(aluguel)):
            print(f'{aluguel[i]}\n')
    if situacao == 'Venda':
        for i in range(0, len(venda)):
            print(f'{venda[i]}\n')


for i in range(10):

    rua = ['Frei Mariano', 'Nossa Senhora de Fátima', 'Do Carmo', 'São Pedro',
           'Nossa Senhora da Candelaria', 'Albuquerque', 'Porto Carreiro']

    bairro = ['Maria Leite', 'Centro', 'Universitário',
              'Previsul', 'Aeroporto', 'Nova Corumbá', 'Guanã']

    tipo = properties_types[randint(0, 3)]

    endereco = rua[randint(0, 6)]

    bairro = bairro[randint(0, 6)]

    situacao = properties_sit[randint(0, 1)]
    if situacao == 'aluguel':
        valor = (randint(500, 2000))
    elif situacao == 'venda':
        valor = (randint(50000, 300000))

    imovel = Imovel(tipo, endereco, bairro, valor, situacao)

    imovel.Cadastrar(imovel, i)


for i in range(len(properties_list)):
    print(f'{properties_list[i]}\n')


filtro = input('Deseja ver imóveis em qual situação? (Venda ou Aluguel)')

Filtrar(filtro)
