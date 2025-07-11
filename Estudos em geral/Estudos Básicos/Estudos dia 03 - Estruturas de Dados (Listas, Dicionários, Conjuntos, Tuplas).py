#1 - Peça 5 números ao usuário e armazene numa lista.
def criaLista():
    lista = []
    for i in range(5):
          n = int(input(f"Digite o número {i + 1}: "))
          lista.append(n)
    return lista
print(f"\nSua lista está criada: {criaLista()}\n")

#2 - Crie uma lista e remova todos os valores ímpares.
lista = criaLista()

def removeImpar(lista):
    listaPares = []
    for par in lista:
        if par % 2 == 0:
            listaPares.append(par)
    return print(f"\nSegue lista sem os números ímpares: {listaPares}\n")
removeImpar(lista)

#3 - Dado um dicionário com nome e idade, adicione novos pares e remova itens.
dct = {
    "nome" : "Gustavo",
    "idade" : 28
}
print(dct)

dct.update({
    "cidade" : "Mogi das Cruzes",
    "bairro" : "Jd ponte grande"
})
print(dct)

dct["cidade"] = "Suzano"
print(dct)

dct.pop("idade")
print(dct)

del dct["nome"]
print(dct)

#4 - Liste os nomes de uma lista de dicionários de alunos aprovados (média ≥ 6).
alunos = {
    "Gustavo": 7.5,
    "Jhennifer": 5.8,
    "Luis": 8.2,
    "Bernardo": 6.0,
    "Patricia": 4.5
}

aprovados = []

for nome, media in alunos.items():
    if media >= 6:
        aprovados.append(nome)

print("\nLista de aprovados:\n")
for nome in aprovados:
    print(nome)

#5 Crie um conjunto com as letras únicas de uma palavra.
def letrasUnicas():
    palavra = input("Digite a palavra para extrair o conjuntode letrar únicas: ")
    letras = set()
    for letra in palavra:
        letras.add(letra)
    return print(f"\nSegue o conjunto de letrar únicas da palavra {palavra}: {letras}")
letrasUnicas()

#6 - Some todos os valores de um dicionário.
dicio = {
    "Gustavo": 8,
    "Jhennifer": 6,
    "Luis": 4,
    "Bernardo": 9,
    "Patricia": 7
}

def somaValores(dct):
    soma = 0
    for nome, valor in dct.items():
        soma += valor
    return soma
print(f"\nA soma do valores do dicionário é: {somaValores(dicio)}")

#7 - Faça a união e interseção de dois conjuntos de números.
conjuntoUm = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
conjuntoDois = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

conjuntoUniao = conjuntoUm.union(conjuntoDois)
print(conjuntoUniao)

conjuntoInterseccao = conjuntoUm.intersection(conjuntoDois)
print(conjuntoInterseccao)

#8 - Peça notas e salve como tupla, depois exiba a média.
tupla = ()

def mediaTupla(tpl):
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    soma = 0
    novaTupla = tpl + (n1, n2, n3)
    for m in novaTupla:
        soma += m
    media = soma / 3
    return media
print(f"\nA média das notas é {mediaTupla(tupla):.1f}.")

#9 - Inverta uma lista sem usar métodos prontos.
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def inverteLista(l):
    listaInvertida = []
    for i in l:
        listaInvertida.insert(0, i)
    return listaInvertida
print(f"\nSegue a lista invertida: {inverteLista(lista)}")

#10 - Ordene uma lista de tuplas com nome e idade.
listaTuplas = [("Gustavo", 28), ("Bernardo", 3), ("Jhennifer", 27), ("Patricia", 53)]

def ordenaListaTupla(lt):
    listaOrdenada = sorted(lt, key=lambda tupla: tupla[1])
    return listaOrdenada
print(f"\nSegue a lista ordenada: {ordenaListaTupla(listaTuplas)}")