# Gestor de Estoque com Descontos

Sistema de linha de comando em Python para gestão de múltiplos estoques e aplicação de descontos em produtos.

---

## 🛠️ Tecnologias

- **Python 3.10+**
- **rich** – formatação e cores no terminal
- **re** – validação de formatos com expressões regulares
- Estrutura modular: `produto`, `estoque`, `gestao`, `utils`, `main.py`

---

## 🚀 Como executar

```bash
git clone https://github.com/GustavoCintra97/Estudos_Dev_Back_End.git
cd Estudos_Dev_Back_End/Projetos/Projeto\ 2\ -\ Gestor\ de\ Estoque\ com\ Descontos
pip install rich
python main.py
```

---

## 🚩 Funcionalidades

- Criar e gerenciar vários estoques
- Cadastrar, listar e remover produtos
- Calcular estoque total
- Aplicar descontos válidos (formato `%`, ponto ou vírgula, sem preços negativos)
- Interface enriquecida com `rich`

---

## 🧩 Estrutura de arquivos

```
gestao.py       → classe `Gestao` para controlar disponíveis
estoque.py      → classe `Estoque` com attributes e método `nomeFormatado`
produto.py      → classe `Produto`
utils.py        → funções de entrada, menu, lógica central
main.py         → loop interativo, tratamento de exceções
```

---

## ⭐ Próximas melhorias (roadmap)

- **Persistência de dados**: salvar estoques em JSON/CSV
- **Testes unitários** com Pytest
- **APIs REST** com Flask ou Django
- **Docker** para ambiente executável
- **Tratamento de concorrência** para multi-usuários

---

## 📝 Contribuição

1. Faça um fork
2. Crie uma branch
3. Submeta PR