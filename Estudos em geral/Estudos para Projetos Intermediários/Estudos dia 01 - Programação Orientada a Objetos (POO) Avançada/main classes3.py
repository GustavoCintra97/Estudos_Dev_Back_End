from classes3 import Cliente

c1 = Cliente('Gustavo', 28)
c1.insereEndereco('Mogi das Cruzes', 'SP')
print(c1.nome)
c1.listaEnderecos()
print()
del c1
print()

c2 = Cliente('Bernardo', 15)
c2.insereEndereco('Mogi das Cruzes', 'SP')
c2.insereEndereco('Rio De Janeiro', 'RJ')
print(c2.nome)
c2.listaEnderecos()
print()
del c2
print()

c3 = Cliente('Jhennifer', 27)
c3.insereEndereco('Mogi das Cruzes', 'SP')
c3.insereEndereco('Rio De Janeiro', 'RJ')
c3.insereEndereco('Minas Gerais', 'MG')
print(c3.nome)
c3.listaEnderecos()
print()
del c3
print()

print('#' * 50)