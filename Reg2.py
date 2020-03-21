'''2) Faça um algoritmo para ler os dados (nome, salário, estado civil, sexo, número de dependentes, cidade e estado de residência) dos funcionários de uma empresa e mostrar uma listagem de todos os dados dos funcionários(as) CASADOS(AS), residentes no RS e com SALÁRIO acima de R$ 1.500,00. Cadastrar no máximo 20 funcionários.'''
from random import randint

funcionarios = []
lista_esp = []

nomes = ['Alice', 'Miguel', 'Sophia', 'Arthur', 'Helena', 'Bernardo', 'Valentina', 'Heitor', 'Laura',
         'Davi', 'Isabella', 'Lorenzo', 'Manuela',	'Théo', 'Júlia', 'Pedro', 'Heloísa', 'Gabriel', 'Luiza', 'Enzo']

ufs = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE',
       'TO']

ec = ['Solteiro', 'Casado']

sexos = ['Masculino', 'Feminino']


class Funcionario:
    def __init__(self, nome, salario, estadoC, sexo, dependentes, cidade, uf):
        self.nome = nome
        self.salario = salario
        self.estadoC = estadoC
        self.sexo = sexo
        self.dependentes = dependentes
        self.cidade = cidade
        self.uf = uf

    def cadastro_esp(self, funcio):
        for funcio in funcionarios:
            if funcio.estadoC == 'Casado' and funcio.salario > 1500 and funcio.uf == 'RS' funcio.:
                lista_esp.append(funcio)

    def __repr__(self):
        return str(self.__dict__)


for i in range(len(nomes)):
    nome = nomes[randint(0, 19)]
    salario = (randint(850, 4000))
    estadoC = ec[randint(0, 1)]
    sexo = sexos[randint(0, 1)]
    dependentes = randint(0, 5)
    cidade = 'Qualquer uma'
    uf = ufs[randint(0, (len(ufs) - 1))]

    funcio = Funcionario(nome, salario, estadoC, sexo, dependentes, cidade, uf)
    funcionarios.append(funcio)

funcio.cadastro_esp(funcio)

for i in range(len(funcionarios)):
    print(f'{i+1} - {funcionarios[i]}\n')

print('\n\n\n')

for i in range(len(lista_esp)):
    print(f'{i+1} - {lista_esp[i]}\n')
