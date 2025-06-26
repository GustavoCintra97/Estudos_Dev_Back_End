from aluno import Aluno
from turma import Turma

def inputStr(msg, condicao=None, erro="\nEntrada inválida!"):
    while True:
        try:
            palavra = input(msg)
            if condicao and not condicao(palavra):
                print(erro)
            else:
                return palavra
        except Exception:
            print("Erro ao ler a entrada.")

def inputInt(msg, condicao=None, erro="\nEntrada inválida!"):
    while True:
        try:
            valor = int(input(msg))
            if condicao and not condicao(valor):
                print(erro)
            else:
                return valor
        except ValueError:
            print("Digite um número inteiro.")

def inputFloat(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("\nNota inválida. Digite um número.\n")

def criarTurma() -> Turma:
    nome = input("\nDigite o nome da Turma: ")
    novaTurma = Turma(
        nomeTurma=nome,
        alunos = []
    )
    print(f"\nTurma {novaTurma.nomeTurma} criada!")
    return novaTurma

def adicionaAluno(turma: Turma) -> Aluno:
    nome = input("Digite o nome do aluno: ")
    notas = []
    idade = inputInt("Digite a idade do aluno: ")
    qtdNotas = inputInt(
        "Digite a quantidade de notas a serem adicionadas (5 no máximo): ",
        condicao=lambda x: 0 < x <= 5,
        erro="\nQuantidade inválida! Digite de 1 a 5.\n"
    )

    for n in range(qtdNotas):
        nota = inputFloat(f"\nDigite a {n + 1}ª nota: ")
        notas.append(nota)

    novoAluno = Aluno(
        nome=nome,
        idade=idade,
        nota=notas
    )
    turma.alunos.append(novoAluno)
    print(f"\nAluno {novoAluno.nome} adicionado a turma {turma.nomeTurma}.")
    return novoAluno

def listarAlunos(turma: Turma):
    print(f"\nLista de alunos da turma {turma.nomeTurma}:\n")
    for a in turma.alunos:
        print(a)

def removerAluno(turma: Turma):
    nome = input("Digite o nome do aluno que deseja remover: ").strip().lower()
    idade = inputInt("Digite a idade do aluno que deseja remover: ")
    for a in turma.alunos:
        if a.nome.strip().lower() == nome and a.idade == idade:
            turma.alunos.remove(a)
            print(f"\nO aluno {a.nome} foi removido da turma {turma.nomeTurma}.")
            return
    print(f'\nNenhum aluno encontrado com o nome "{nome}" e idade {idade} na turma {turma.nomeTurma}.')

def desejaContinuar():
    resposta = inputStr(
        'Deseja realizar outra operação? (Digite "S" ou "N"): ',
        condicao=lambda x: x.upper() in ['S', 'N'],
        erro="\nTente novamente!\n"
    )
    return resposta.upper() == "S"

def exibirMenu():
    print("\nMenu:")
    print("\n1. Adicionar aluno.\n2. Listar alunos.\n3. Remover aluno.\n4. Média geral da turma.\nDigite 0 para Sair.")
