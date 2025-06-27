import traceback
from rich.console import Console
from gestao import Gestao
from utils import (
    inputInt, desejaContinuar, exibirMenu, 
    encerrar, executarMenu, limparTela
)

console = Console()
gestao = Gestao(estoques=[])
estoqueAtivo = None

try:
    limparTela()
    console.print("Olá! Bem-vindo ao Sistema de gestão de estoque de Gustavo!", style="bold dodger_blue2")
    console.print()

    while True:
        limparTela()
        console.print("=" * 40, style="bold dodger_blue2")
        console.print("  Sistema de Gestão de Estoque - Gustavo", style="bold dodger_blue2")
        console.print("=" * 40, style="bold dodger_blue2")
        exibirMenu()
        opcao = inputInt(
            "Digite a opção desejada: ",
            condicao=lambda x: 0 <= x <= 7,
            erro="\nTente novamente!\n"
        )
        if opcao == 0:
            encerrar()
            break

        estoqueAtivo = executarMenu(opcao, gestao, estoqueAtivo)

        if not desejaContinuar():
            encerrar()
            break
        else:
            console.print("\nOK, retornando ao menu...\n", style="green")
except Exception as e:
    console.print(f"\n[bold red]Erro inesperado:[/bold red] {e}")
    traceback.print_exc()
    encerrar()