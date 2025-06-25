#1 - Crie uma função que receba 3 números e retorne a média.
def media():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    media = (n1 + n2 + n3) / 3
    return print(f"\nA média dos números é {media:.1f}!")
media()

#2 - Função que recebe uma string e retorna a string invertida.
def inverter():
    palavra = input("\nDigite uma palavra: ")
    inverter = palavra[::-1]
    return print(f"\nA Palavra {palavra} invertida é {inverter}.")
inverter()

#3 - Função que calcula o fatorial de um número.
def fatorial():
    n = int(input("\nDigite o número para calculo de fatorial: "))
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return print(f"\nO Fatorial de {n} é {fat}.")
fatorial()

#4 - Função que verifica se um número é primo.
def veriPrimo():
    n = int(input("\nDigite o número a ser verificado: "))
    if n <= 1:
        return print(f"\nO número {n} não é primo!")
    for i in range (2, n):
        if n % i == 0:
            return print(f"\nO número {n} não é primo!")
    return print(f"\nO número {n} é primo!")
veriPrimo()

#5 Função que conta a quantidade de vogais em uma frase.
def contaVogal():
    palavra = input("\nDigite uma palavra: ").lower()
    vogal = "aeiou"
    contar = 0
    for l in palavra:
        if l in vogal:
            contar += 1
    return print(f"\nA Palavra {palavra} contém {contar} vogais.")
contaVogal()

#6 - Função que recebe dois números e retorna o maior.
def veriMaior():
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    maior = max(n1,n2)
    return print(f"\nO maior número é o {maior}.")
veriMaior()

#7 - Função que simula uma calculadora básica (soma, subtração, etc.).
def calculadoraBasica():
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print("\n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\nDigite 0 para sair")
    while True:
        opcao = int(input("\nDigite a opção para prosseguir: "))
        if opcao == 1:
            print(f"\nA Soma de {n1} + {n2} é {n1 + n2}.")
        elif opcao == 2:
            print(f"\nA Subtração de {n1} - {n2} é {n1 - n2}.")
        elif opcao == 3:
            print(f"\nA Multiplicação de {n1} x {n2} é {n1 * n2}.")
        elif opcao == 4:
            print(f"\nA Divisão de {n1} / {n2} é {n1 / n2:.1f}.")
        elif opcao == 0:
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida!")
calculadoraBasica()

#8 - Função que retorna a tabuada de um número.
def tabuada():
    n = int(input("\nDigite o número para calcular a tabuada: "))
    print(f"\nSegue abaixo a Tabuada do {n}:\n")
    for t in range(1, 11):
        print(f"{t} x {n} = {t * n}")
tabuada()

#9 - Função que recebe uma lista de números e retorna a soma dos pares.
def criaLista():
    listaTamanho = int(input("\nDigite a quantidade de números a serem listados: \n"))
    lista = []
    for n in range(listaTamanho):
        elemento = int(input(f"Digite o número {n + 1}: "))
        lista.append(elemento)
    return lista

lista = criaLista()

def listaSomaPar(lista):
    somaPar = 0
    for par in lista:
        if par % 2 == 0:
            somaPar += par
    return print(f"\nA soma dos pares da lista {lista} é igual a {somaPar}.")
listaSomaPar(lista)

#10 - Crie uma função que retorna True se uma palavra é palíndromo.
def verificaPalindromo():
    palavra = input("Digite a palavra para verificação: ").lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False
print(verificaPalindromo())