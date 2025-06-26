# 📆 Roteiro de Projetos Pré-Django (Python + Git)

**Objetivo:** Consolidar lógica, POO, organização de repositório e preparação para uso do framework Django.

**Total de projetos:** 4  
**Tempo estimado:** 3 a 4 semanas (1 por semana)

---

## 🔹 Projeto 1: Sistema de Biblioteca

**Descrição:** Aplicativo de terminal para gestão de livros, usuários e empréstimos.

### Funcionalidades obrigatórias:
- Classe `Livro`: título, autor, disponível (bool)
- Classe `Usuario`: nome, id, livros emprestados
- Classe `Emprestimo`: id do usuário, livro emprestado, data de devolução
- Listar livros, emprestar e devolver

### Desafio extra:
- Impedir empréstimo caso o usuário já tenha 3 livros em mãos

### Git:
- Crie branch `feature/biblioteca`
- README com instruções de uso no terminal

---

## 🔹 Projeto 2: Gestor de Despesas Pessoais

**Descrição:** Controle básico de gastos mensais categorizados.

### Funcionalidades obrigatórias:
- Inserir despesas com: data, valor, categoria, descrição
- Visualizar totais por categoria
- Calcular total gasto no mês

### Desafio extra:
- Exportar relatório para `.csv` com a biblioteca `csv`

### Git:
- Branch `feature/despesas`
- README com imagem de exemplo do terminal

---

## 🔹 Projeto 3: Sistema de Vendas com Estoque

**Descrição:** Simula uma loja simples com controle de estoque e vendas.

### Funcionalidades obrigatórias:
- Classe `Produto`: nome, preço, estoque
- Classe `Venda`: produto, quantidade, data
- Cadastro de novos produtos
- Atualiza estoque após venda

### Desafio extra:
- Carrinho de compras com múltiplos produtos

### Git:
- Branch `feature/estoque`
- README com instruções e imagem da lógica de carrinho

---

## 🔹 Projeto 4: Simulador de API Local (sem framework)

**Descrição:** Sistema que simula chamadas de API via terminal e responde em formato JSON.

### Funcionalidades obrigatórias:
- CRUD completo de `Produto` e `Cliente`
- Comandos simulados: `GET`, `POST`, `PUT`, `DELETE`
- Exibir resultados com `json.dumps()`

### Desafio extra:
- Persistir os dados em `.json` ou com `pickle`

### Git:
- Branch `feature/api-simulada`
- README com prints ou GIFs da execução

---

## 📊 Regras gerais para os 4 projetos:

- Utilize **GitHub** com README bem feito
- Cada funcionalidade extra pode ter sua **própria branch**
- Use **.gitignore** e arquivos organizados
- Exporte prints ou gravações da execução

---

Finalizados os 4 projetos, você estará 100% pronto para iniciar com o **framework Django**, criando projetos reais com banco de dados, views, templates e API REST.

Se quiser, posso montar o cronograma do módulo Django a seguir. Deseja isso?

