import os
import re
from rich.console import Console
from produto import Produto
from estoque import Estoque
from gestao import Gestao
from typing import Callable, Optional
from textwrap import dedent

console = Console()

def inputStr(msg: str, condicao: Callable[[str], bool] = lambda x: x.strip() != "", erro: str = "\nEntrada inválida!") -> str:
    """
    Solicita uma entrada de string do usuário, com validação opcional.

    Args:
        msg (str): Mensagem exibida ao usuário.
        condicao (Callable[[str], bool], optional): Função que valida a string inserida.
        erro (str, optional): Mensagem exibida em caso de entrada inválida.

    Returns:
        str: String validada inserida pelo usuário.
    """
    return inputComParse(msg, str, erro, condicao)

def inputInt(msg: str, condicao: Optional[Callable[[int], bool]] = None, erro: str ="\nEntrada inválida!") -> int:
    """
    Solicita uma entrada de número inteiro do usuário, com validação opcional.

    Args:
        msg (str): Mensagem exibida ao usuário.
        condicao (Callable[[int], bool], optional): Função de validação.
        erro (str, optional): Mensagem em caso de erro.

    Returns:
        int: Valor inteiro validado.
    """
    return inputComParse(msg, int, erro, condicao)

def inputFloat(msg: str, condicao: Optional[Callable[[float], bool]] = None, erro: str ="\nValor inválido!") -> float:
    """
    Solicita uma entrada de número float do usuário, com validação opcional.

    Args:
        msg (str): Mensagem exibida ao usuário.
        condicao (Callable[[float], bool], optional): Função de validação.
        erro (str, optional): Mensagem em caso de erro.

    Returns:
        float: Valor float validado.
    """
    return inputComParse(msg, float, erro, condicao)

def cadastraProduto(estoqueProduto: Estoque) -> Produto:
    """
    Solicita os dados de um novo produto e o adiciona ao estoque informado.

    Args:
        estoqueProduto (Estoque): Estoque onde o produto será cadastrado.

    Returns:
        Produto: O produto criado e adicionado.
    """
    while True:
        nome = console.input("[bold dodger_blue2]Digite o nome do produto: [/bold dodger_blue2]").strip()
        if any(p.nome.strip().lower() == nome.lower() for p in estoqueProduto.produtos):
            console.print(f'Produto com nome "{nome}" já existe no estoque.', style="bold red")
        else:
            break
    preco = inputFloat(
        "Digite o preço do produto: ", 
        condicao=lambda x: x >= 0, 
        erro="O preço não pode ser negativo."
    )
    estoque = inputInt("Digite a quantidade de produtos em estoque: ", 
        condicao=lambda x: x >= 0, 
        erro="A quantidade não pode ser negativa."
    )

    novoProduto = Produto(
        nome=nome,
        preco=preco,
        estoque=estoque
    )
    estoqueProduto.produtos.append(novoProduto)
    console.print(f'\nO Produto "{novoProduto.nomeFormatado()}" foi adicionado ao estoque {estoqueProduto.nomeFormatado()}.', style="bold green")
    return novoProduto

def listarProdutos(estoqueProduto: Estoque):
    """
    Exibe todos os produtos cadastrados no estoque informado.

    Args:
        estoqueProduto (Estoque): Estoque cujos produtos serão listados.
    """
    console.print(f'\nLista de produtos do estoque "{estoqueProduto.nomeFormatado()}":\n', style="bold dodger_blue2")

    if not estoqueProduto.produtos:
        console.print("Nenhum produto cadastrado no estoque.\n", style="bold red")
        return

    for i, produto in enumerate(estoqueProduto.produtos, start=1):
        console.print(f"{i}. {produto}", style="bold dodger_blue2")

    console.print(f"\nTotal de produtos listados: {len(estoqueProduto.produtos)}", style="bold dodger_blue2")

def removerProduto(estoqueProduto: Estoque):
    """
    Remove um produto do estoque com base no nome informado pelo usuário.
    Caso mais de um produto com o mesmo nome seja encontrado, permite a escolha por índice.

    Args:
        estoqueProduto (Estoque): Estoque de onde o produto será removido.
    """
    nome = console.input("[bold dodger_blue2]Digite o nome do produto que deseja remover: [/bold dodger_blue2]").strip().lower()
    produtosEncontrados = [p for p in estoqueProduto.produtos if p.nome.strip().lower() == nome]

    if not produtosEncontrados:
        console.print(f'\nNenhum produto com o nome "{nome.capitalize()}" encontrado.', style="bold red")
        return

    if len(produtosEncontrados) == 1:
        produto = produtosEncontrados[0]
        estoqueProduto.produtos.remove(produto)
        console.print(f'\nO produto "{produto.nomeFormatado()}" foi removido.', style="bold green")
        return

    console.print("\nProdutos encontrados:", style="bold green")
    for i, p in enumerate(produtosEncontrados, 1):
        console.print(f"{i}. {p}", style="bold green")
    
    indice = inputInt(
        "Digite o número do produto que deseja remover: ", 
        condicao=lambda x: 1 <= x <= len(produtosEncontrados)
    )
    produtoRemover = produtosEncontrados[indice - 1]
    estoqueProduto.produtos.remove(produtoRemover)
    console.print(f'\nProduto "{produtoRemover.nomeFormatado()}" removido com sucesso.', style="bold green")

def desejaContinuar():
    """
    Pergunta ao usuário se deseja continuar usando o sistema.

    Returns:
        bool: True se o usuário deseja continuar, False caso contrário.
    """
    resposta = inputStr(
        'Deseja realizar outra operação? (Digite "S" ou "N"): ',
        condicao=lambda x: x.upper() in ['S', 'N'],
        erro="\nTente novamente!\n"
    )
    return resposta.upper() == "S"

def exibirMenu():
    """
    Exibe o menu principal de opções para o usuário.
    """
    console.print(dedent("""
    Menu:
    1. Criar novo estoque
    2. Selecionar estoque
    3. Cadastrar produto no estoque ativo
    4. Listar produtos do estoque ativo
    5. Remover produto do estoque ativo
    6. Exibir estoque total do estoque ativo
    7. Aplicar desconto em produto do estoque ativo
    0. Sair
    """), style="bold dodger_blue2")

def aplicaDesconto(produto: Produto) -> None:
    """
    Solicita ao usuário um desconto percentual e aplica ao produto selecionado,
    desde que o valor final não seja negativo.

    Args:
        produto (Produto): Produto que receberá o desconto.
    """
    padrao = re.compile(r'^\d+(\.\d+)?%?$')
    
    while True:
        desconto = console.input("[bold dodger_blue2]Digite o valor de desconto a ser aplicado (Exemplo: '5%'): [/bold dodger_blue2] ").strip()
        
        desconto_ajustado = desconto.replace(',', '.')
        
        if padrao.match(desconto_ajustado):
            valor = converteFloat(desconto_ajustado)
            if valor is not None:
                valorDesconto = produto.preco * valor
                novoPreco = produto.preco - valorDesconto

                if novoPreco < 0:
                    console.print(
                        f"Desconto inválido! O valor resultaria em preço negativo (R$ {novoPreco:.2f}).",
                        style="bold red"
                    )
                else:
                    produto.preco = novoPreco
                    console.print(
                        f"Foi aplicado {desconto} de desconto no produto '{produto.nomeFormatado()}'. "
                        f"Novo valor: R${produto.preco:.2f}",
                        style="bold green"
                    )
                    break
        else:
            console.print("Entrada inválida. Tente novamente com o formato '%'. Exemplo: 5, 5%, 5.5, 5.5%", style="bold red")

def converteFloat(porcentagem: str) -> Optional[float]:
    """
    Converte uma string com valor percentual para float.

    Args:
        porcentagem (str): Valor em formato percentual (ex: '10%').

    Returns:
        float: Valor decimal correspondente (ex: 0.1), ou None se inválido.
    """
    if not porcentagem:
        console.print("\nEntrada vazia. Digite algo como '5%' ou '5'.\n", style="bold red")
        return None
    try:
        valor = porcentagem.strip().strip('%')
        return float(valor) / 100
    except ValueError:
        console.print("\nDesconto inválido. Digite algo como '5%' ou '5'.\n", style="bold red")
        return None
    
def buscaProduto(estoqueProduto: Estoque) -> Optional[Produto]:
    """
    Busca um produto no estoque com base no nome informado pelo usuário.

    Args:
        estoqueProduto (Estoque): Estoque onde a busca será realizada.

    Returns:
        Produto | None: Produto encontrado ou None se não for encontrado.
    """
    nome = console.input("[bold dodger_blue2]Digite o nome do produto que deseja aplicar o desconto: [/bold dodger_blue2] ").strip().lower()
    for produto in estoqueProduto.produtos:
        if produto.nome.strip().lower() == nome:
            return produto
    console.print(f'\nNenhum produto encontrado com o nome "{nome.capitalize()}" no estoque "{estoqueProduto.nomeFormatado()}".', style="bold red")
    return None

def estoqueTotal(estoqueProduto: Estoque) -> int:
    """
    Calcula e exibe a quantidade total de itens em estoque.

    Args:
        estoqueProduto (Estoque): Estoque a ser analisado.

    Returns:
        int: Quantidade total de itens no estoque.
    """
    soma = 0
    for produto in estoqueProduto.produtos:
        soma += produto.estoque
    console.print(f"A quantidade total de produtos em estoque é {soma}.", style="bold dodger_blue2")
    return soma

def encerrar():
    """
    Exibe mensagem de encerramento e finaliza o programa.
    """
    console.print("Encerrando o programa. Obrigado por utilizar!", style="bold dodger_blue2")

def menuAplicarDesconto(estoque: Estoque):
    """
    Exibe o menu para buscar e aplicar desconto a um produto do estoque.

    Args:
        estoque (Estoque): Estoque onde está o produto.
    """
    if not estoque.produtos:
        console.print("Não há produtos cadastrados ainda.", style="bold red")
        return
    produto = buscaProduto(estoque)
    if produto:
        aplicaDesconto(produto)

def selecionarEstoque(estoque: Gestao) -> Estoque:
    """
    Permite ao usuário selecionar um dos estoques disponíveis.

    Args:
        estoque (Gestao): Instância com todos os estoques cadastrados.

    Returns:
        Estoque | None: Estoque selecionado ou None se nenhum estiver disponível.
    """
    if not estoque.estoques:
        console.print("Nenhum estoque cadastrado ainda.", style="bold red")
        return None

    console.print("\nEstoques disponíveis:", style="bold dodger_blue2")
    for i, e in enumerate(estoque.estoques, start=1): 
        console.print(f"{i}. {e.nomeFormatado()}", style="bold dodger_blue2")

    escolha = inputInt(
        "Digite o número do estoque que deseja selecionar: ",
        condicao=lambda x: 1 <= x <= len(estoque.estoques)
    )
    console.print(f'Estoque "{estoque.estoques[escolha - 1].nomeFormatado()}" selecionado.', style="bold green")
    return estoque.estoques[escolha - 1]

def criarEstoque(gestao: Gestao) -> Estoque:
    """
    Cria um novo estoque com o nome fornecido pelo usuário.

    Args:
        gestao (Gestao): Instância de gestão que armazena os estoques.

    Returns:
        Estoque: Estoque criado.
    """
    while True:
        nome = console.input("[bold dodger_blue2]\nDigite o nome do Estoque: [/bold dodger_blue2] ").strip()
        if nome:
            break
        console.print("Nome do estoque não pode estar vazio.", style="bold red")
    novoEstoque = Estoque(
        nomeEstoque=nome,
        produtos = []
    )
    gestao.estoques.append(novoEstoque)
    console.print(f"\nEstoque {novoEstoque.nomeFormatado()} criado!", style="bold green")
    return novoEstoque

def executarMenu(opcao: int, gestao: Gestao, estoqueAtivo: Estoque) -> Estoque:
    """
    Executa a opção do menu principal selecionada pelo usuário.

    Args:
        opcao (int): Número da opção selecionada.
        gestao (Gestao): Instância de gestão com os estoques.
        estoqueAtivo (Estoque): Estoque atualmente em uso.

    Returns:
        Estoque: Estoque atualizado (pode ser o mesmo ou um novo).
    """
    if opcao == 1:
        return criarEstoque(gestao)
    elif opcao == 2:
        console.print("")
        return selecionarEstoque(gestao)
    elif opcao in [3, 4, 5, 6, 7]:
        if not estoqueAtivo:
            console.print("Nenhum estoque selecionado. Use a opção 2 para selecionar.", style="bold red")
            return estoqueAtivo
        if opcao == 3:
            cadastraProduto(estoqueAtivo)
        elif opcao == 4:
            listarProdutos(estoqueAtivo)
        elif opcao == 5:
            removerProduto(estoqueAtivo)
        elif opcao == 6:
            estoqueTotal(estoqueAtivo)
        elif opcao == 7:
            menuAplicarDesconto(estoqueAtivo)
    return estoqueAtivo

def limparTela():
    """
    Limpa o terminal, utilizando o método do Rich ou o comando do sistema operacional.
    """
    try:
        console.clear()
    except Exception:
        os.system("cls" if os.name == "nt" else "clear")

def inputComParse(msg: str, tipo: Callable, erro: str, condicao: Optional[Callable] = None):
    """
    Solicita uma entrada do usuário, converte para o tipo especificado e valida opcionalmente.

    Args:
        msg (str): Mensagem exibida ao usuário.
        tipo (Callable): Função usada para converter a entrada (ex: int, float).
        erro (str): Mensagem de erro personalizada.
        condicao (Callable, optional): Função de validação da entrada.

    Returns:
        Valor convertido e validado (int, float, etc.).
    """
    while True:
        entrada = console.input(f"[bold dodger_blue2]{msg}[/bold dodger_blue2] ")

        if tipo in [float, int]:
            entrada = entrada.replace(',', '.')
        else:
            entrada = entrada.strip()

        try:
            valor = tipo(entrada)
            if condicao and not condicao(valor):
                console.print(erro, style="bold red")
            else:
                return valor
        except (ValueError, TypeError):
            console.print(erro, style="bold red")