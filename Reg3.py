'''3) Faça um algoritmo para cadastrar até 20 produtos de uma loja com os seguintes dados: código, descrição, estoque mínimo, estoque atual e preço. Mostrar todos os dados dos produtos que contenham o estoque atual menor que o estoque mínimo, para efetuar compra. '''
from random import randint


itens = ['Camiseta', 'Bermuda', 'Calça', 'Tenis', 'Carteira',
         'Toalha', 'Relógio', 'Casaco', 'Chinelo', 'Meia']

produtos = []
necessario = []


class Produto:
    def __init__(self, codigo, descricao, estoqMin, estoqAt, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.estoqMin = estoqMin
        self.estoqAt = estoqAt
        self.preco = preco

    def estoque(self, prod):
        for prod in produtos:
            if prod.estoqAt < prod.estoqMin:
                necessario.append(prod)

    def __repr__(self):
        return str(self.__dict__)


for i in range(len(itens)):
    codigo = i+1
    descricao = itens[i]
    estoqMin = 40
    estoqAt = randint(0, 100)
    preco = randint(50, 190)

    prod = Produto(codigo, descricao, estoqMin, estoqAt, preco)
    produtos.append(prod)

prod.estoque(prod)

for prod in necessario:
    print(f'{prod}\n')
