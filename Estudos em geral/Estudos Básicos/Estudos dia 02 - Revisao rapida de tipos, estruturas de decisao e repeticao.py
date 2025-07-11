#1. Tipos Primitivos
##Exercício 1:

valor_str = "3.14"
# Converta para float e some 1.5
# Converta para int e subtraia 3

valor_float = float(valor_str) + 1.5
print(valor_float)

valor_int = int(valor_float) - 3
print(valor_int)

##Exercício 2:

idade = "25"
# Verifique se é numérico e converta para int
# Se não for, retorne "Erro: valor inválido"

if type(idade) == int:
    print("Valor inteiro!")
else:
    print("Erro, valor inválido!")

convertIdade = int(idade)
print(f"Agora o valor {convertIdade} é {type(convertIdade)}")

#2. Estruturas de Decisão
##Exercício 1 (IMC):

peso = 70 # kg
altura = 1.75 # m
# Classifique:
# < 18.5: "Abaixo do peso"
# 18.5-24.9: "Normal"
# 25-29.9: "Sobrepeso"
# >= 30: "Obesidade"

imc = peso / (altura * altura)

print(f"Seu IMC é de {imc:.2f}!")

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal.")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")

##Exercício 2 (Senha):

senha = "G0d0!971212"
# Valide:
# - Mínimo 8 caracteres
# - Pelo menos 1 maiúscula
# - Pelo menos 1 número
# Retorne True se válida, False se inválida

valida = (
    len(senha) >= 8 and
    any(c.isupper() for c in senha) and
    any(c.isdigit() for c in senha)
)
print(valida)

#3. Loops
##Exercício 1 (Fibonacci):

# Gere os primeiros 15 números da sequência usando while
# Sequência: 0, 1, 1, 2, 3, 5, 8...

a, b = 0, 1 
contador = 0

while contador < 15:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1


##Exercício 2 (Filtragem):

numeros = [12, 7, 24, 5, 31, 15]
# Crie:
# pares_quadrado = [n² para pares]
# impares_metade = [n/2 para ímpares]

paresQuadrado = [n**2 for n in numeros if n % 2 == 0]
imparesMetade = [n/2 for n in numeros if n % 2 != 0]
print(f"\n{paresQuadrado}")
print(imparesMetade)

#4. Listas e Dicionários
##Exercício 1 (Análise de Estoque):

estoque = [
{"produto": "Mouse", "preco": 45.90, "qtd": 120},
{"produto": "Teclado", "preco": 129.90, "qtd": 80},
{"produto": "Monitor", "preco": 899.90, "qtd": 25}
]
# Calcule:
# a) Valor total do estoque (preço * qtd)
# b) Produto mais caro
# c) Média de preços
total = sum(item["preco"] * item["qtd"] for item in estoque)
maisCaro = max(estoque, key=lambda x: x["preco"])["produto"]
media = sum(item["preco"] for item in estoque) / len(estoque)

print(f"\n{total}\n{maisCaro}\n{media:.2f}")


##Exercício 2 (Inversor de Dicionário):

dados = {"a": 1, "b": 2, "c": 3}
# Converta para: {1: "a", 2: "b", 3: "c"}

invertido = {valor: chave for chave, valor in dados.items()}
print(invertido)

#Desafio Integrado: Sistema de Biblioteca
"""
Implemente:
- Lista de dicionários: livros = [{"título": str, "autor": str, "emprestado": bool}]
- Menu com loop while:
1. Adicionar livro (input título/autor, emprestado=False)
2. Buscar por autor (exibir todos do autor)
3. Listar livros emprestados
4. Sair
- Valide inputs vazios!
"""

biblioteca = []

while True:
    print("\n1. Adicionar livro\n2. Buscar por autor\n3. Livros emprestados\n4. Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        if titulo and autor:
            biblioteca.append({"título": titulo, "autor": autor, "emprestado": False})
            print("✅ Livro adicionado!")
        else:
            print("❌ Título/autor inválidos")

    elif opcao == "2":
        autorBusca = input("Autor: ").strip()
        encontrados = [livro for livro in biblioteca if livro["autor"].lower() == autorBusca.lower()]
        for livro in encontrados:
            print(f"- {livro['título']}")

    elif opcao == "3":
        emprestados = [livro for livro in biblioteca if livro["emprestado"]]
        for livro in emprestados:
            print(f"- {livro['título']} ({livro['autor']})")

    elif opcao == "4":
        print("Saindo...")
        break