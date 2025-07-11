from classes4 import *

'''
Associação - Usa / Agregação - Tem / Composição - É dono / Herança - É
'''

c1 = Cliente('Gustavo', 28)
print(c1.nome)
c1.falar()
c1.comprar()
a1 = Aluno('Bernardo', 28)
print(a1.nome)
a1.falar()
a1.estudar()