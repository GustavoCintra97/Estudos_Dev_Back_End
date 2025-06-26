import os
from aluno import Aluno
from turma import Turma
from functions import inputStr,inputInt, inputFloat, criarTurma, adicionaAluno, removerAluno, listarAlunos, desejaContinuar, exibirMenu

print("Olá! Bem-vindo ao Sistema de criação de turmas e verificação de médias de Gustavo!\nCrie sua Turma para iniciar!")

turma = criarTurma()

while True:
    exibirMenu()
    opcao = inputInt(
        "Digite a opção desejada: ",
        condicao=lambda x: 0 <= x <= 4,
        erro="\nTente novamente!\n"
    )

    if opcao == 0:
        print("Saindo...")
        break

    if opcao == 1:
        adicionaAluno(turma)
    elif opcao == 2:
        listarAlunos(turma)
    elif opcao == 3:
        removerAluno(turma)
    elif opcao == 4:
        turma.mediaGeral()

    if not desejaContinuar():
        print("Saindo...")
        break
    else:
        print("\nOK!\n")
        os.system("cls" if os.name == "nt" else "clear")
