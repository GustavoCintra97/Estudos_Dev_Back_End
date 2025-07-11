from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Gustavo')
print(escritor.nome)

caneta = Caneta('Bic')
print(caneta.marca)

maquina = MaquinaDeEscrever()

# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor
# print(escritor)
print(caneta.marca)
maquina.escrever()