#1 - Solicite dois números e exiba o maior.

def maior():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    maior = max(n1, n2)
    return print(f"O maior número é o {maior}.")
maior()

#2 - Calcule o IMC a partir da altura e peso informados.

def imc():
    peso = float(input("Digite seu Peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura ** 2)
    return print(f"Seu IMC é {imc:.2f}.")
imc()

#3 - Peça um número e diga se ele é positivo, negativo ou zero.
def verificaNum():
    num = int(input("Digite um número: "))
    if num == 0:
        print(f"O número {num} é zero.")
    elif num > 0:
        print(f"O número {num} é positivo.")
    else:
        print(f"O número {num} é negativo.")
verificaNum()

#4 - Calcule a média de 3 notas e classifique como aprovado (≥ 6) ou reprovado.
def media():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    if media >= 6:
        print(f"A média do aluno é {media:.2f}, portanto, está aprovado!")
    else:
        print(f"A média do aluno é {media:.2f}, portanto, está reprovado!")
media()

#5 - Verifique se um número é múltiplo de 3 e 5 ao mesmo tempo.
def verificaMulti():
    n = int(input("Digite o número a ser verificado: "))
    if n % 3 == 0 and n % 5 == 0:
        print(f"O número {n} é multiplo de 3 e de 5.")
    elif n % 3 != 0 and n % 5 == 0:
        print(f"O número {n} é multiplo apenas de 5.")
    elif n % 3 == 0 and n % 5 != 0:
        print(f"O número {n} é multiplo apenas de 3.")
    else:
        print(f"O número {n} não é multiplo de 3 nem de 5.")
verificaMulti()

#6 - Liste os números pares de 1 a 100.
def numPar():
    for i in range(1,101):
        if i % 2 == 0:
            print(i)
numPar()

#7 - Crie uma contagem regressiva de 10 a 1 com while.

def contagemRegressiva():
    contagem = 10
    while contagem != 0:
        print(contagem)
        contagem -= 1
contagemRegressiva()

#8 - Calcule a soma de todos os múltiplos de 7 entre 1 e 500.

def somaMultiSete():
    soma = 0
    for i in range(1,501):
        if i % 7 == 0:
            soma += i
    return print(soma)
somaMultiSete()

#9 - Dada uma idade, diga em qual faixa etária está (criança, jovem, adulto, idoso).

def faixaEtaria():
    idade = int(input("Digite sua idade: "))
    if idade < 15:
        print('Você está na faixa etária "Criança"')
    elif 15 <= idade <= 21:
        print('Você está na faixa etária "Jovem"')
    elif 21 < idade < 60:
        print('Você está na faixa etária "Adulto"')
    else:
        print('Você está na faixa etária "Idoso"')
faixaEtaria()

#10 - Simule um menu com 3 opções e repita até o usuário digitar “0” para sair.

def menu():
    print("\n1.Nome\n2.Idade\n3.Cidade\nDigite 0 para sair")
    while True:
        opcao = int(input("\nInsira a opção desejada: "))
        if opcao == 1:
            print("\nSelecionou a opção nome.")
        elif opcao == 2:
            print("\nSelecionou a opção idade.")
        elif opcao == 3:
            print("\nSelecionou a opção cidade.")
        elif opcao == 0:
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida!")
menu()