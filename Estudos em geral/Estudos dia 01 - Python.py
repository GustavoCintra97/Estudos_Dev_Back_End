
# 1. Soma de dois números
def soma():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    return print(f"A soma de {a} + {b} é igual a {a + b}\n")
soma()

# 2. Número par ou ímpar
def parImpar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        return print(f"O número {numero} é par.\n")
    else:
        return print(f"O número {numero} é ímpar.\n")
parImpar()

#3. Maior de dois números
def maiorN():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    if a > b:
        return print(f"{a} é o maior número.\n")
    elif b > a:
        return print(f"{b} é o maior número.\n")
    else:
        return print("Os números são iguais.\n")
maiorN()

#4. Contagem de 1 a 10
def contagem():
    for i in range(1,11):
        print(i)
contagem()

#5. Tabuada do 7
def tabuadaSete():
    for i in range(1,11):
        print(f"{i} x 7 = {i * 7}")
tabuadaSete()

#6. Conversor de temperatura
def convertCelsiusFahrenheit():
    C = float(input("Digite quantos Graus C°: "))
    F = C * 1.8 + 32
    return print(f"Convertendo {C}° para Fahrenheit fica igual a {F}°\n")
convertCelsiusFahrenheit()

#7. Calculadora de média
def mediaAprova():
    n1 = float(input("Digite a primeira nota : "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nora: "))
    media = (n1 + n2 + n3) / 3
    if media >= 6:
        return print(f"O Aluno foi aprovado com a média {media}\n")
    else:
        return print(f"O Aluno foi reprovado com a média {media}\n")
mediaAprova()

#8. Verificador de senha
def verificaSenha():
    senha = 'G0d0!971212'
    s = input("Digite sua senha: ")
    while s != senha:
        print("Senha incorreta, digite novamente!\n")
        s = input("Digite sua senha: ")
    else:
        print("Senha correta! Bem Vindo\n")
verificaSenha()

#9. Contagem regressiva
def contagemRegressiva():
    for i in range(10, 0, -1):
        print(i)
contagemRegressiva()

#10. Soma dos números de 1 a 100
def somaCem():
    soma = 0
    for i in range(1, 101):
        soma += i
    return print(f"A soma dos números de 1 a 100 é igual a {soma}.\n")
somaCem()

#11. Contar vogais
def contaVogais():
    palavra = input("Digite uma palavra: ").lower()
    vogais = "aeiou"
    contagem = 0
    for letra in palavra:
        if letra in vogais:
            contagem += 1
    return print(f"A Palavra {palavra} contém {contagem} vogais.\n")
contaVogais()

#12. Verificar palíndromo
def verificaPalindromo():
    texto = input("Digite uma palavra: ").lower()
    if texto == texto[::-1]:
        print(f"A Palavra {texto} ao contrário fica {texto[::-1]}, ou seja, é um Palíndromo.\n")
    else:
        print(f"A Palavra {texto} ao contrário fica {texto[::-1]}, ou seja, não é um Palíndromo.\n")
verificaPalindromo()

#13. Fatorial de um número
def fatorial():
    n = int(input("Digite um número: "))
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return print(f"O fatorial de {n} é {fatorial}.\n")
fatorial()

#14. Números pares em uma lista
def listaPar():
    lista = []
    for _ in range(5):
        num = int(input("Digite um número: "))
        lista.append(num)
    listaPar = [n for n in lista if n % 2 == 0]
    return print(f"Lista de número pares digitados: {listaPar}\n")
listaPar()

#15. Cadastro simples
def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")
    return print(f"Olá {nome}, você tem {idade} anos e mora em {cidade}.\n")
cadastro()