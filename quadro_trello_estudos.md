# 📘 Estudos para Projetos Intermediários – Python Back-End

Este guia contém os principais tópicos para dominar o nível intermediário de desenvolvimento back-end com Python, aplicando-os diretamente nos próximos projetos práticos.

---

## 1. Programação Orientada a Objetos (POO) Avançada

### ✅ Tópicos
- Encapsulamento com `@property`
- Herança e polimorfismo
- Composição vs Herança
- Métodos mágicos `__str__`, `__repr__`, `__eq__`, etc.

### 📚 Documentações e artigos
- [Python POO Avançada - DevMedia](https://www.devmedia.com.br/programacao-orientada-a-objetos-poo-com-python/32130)
- [POO em Python (com exemplos) – Hashtag Programação](https://www.hashtagtreinamentos.com/poo-python)

### 🎥 Videoaulas
- [Curso Completo de POO com Python – Otávio Miranda (YouTube)](https://www.youtube.com/watch?v=apACNr7DC_s&list=PLbIBj8vQhvm0HFOiLzQ4A6cN6z4N1mu5h)
- [POO com Python – Curso em Vídeo](https://www.youtube.com/watch?v=KfFv4U4oPFE)

---

## 2. Manipulação de Arquivos (CSV, JSON, TXT)

### ✅ Tópicos
- `open()`, leitura e escrita
- `with` context manager
- Módulo `json` para estrutura de dados
- Leitura/gravação de `.csv` com `csv` ou `pandas`

### 📚 Documentações
- [Trabalhando com arquivos no Python – W3Schools em PT](https://www.w3schools.com/python/python_file_handling.asp)
- [Leitura/Escrita JSON - Python Docs (traduzido)](https://docs.python.org/pt-br/3/library/json.html)

### 🎥 Videoaulas
- [Leitura e Escrita de Arquivos em Python – Curso em Vídeo](https://www.youtube.com/watch?v=Y5BvZoecvNw)
- [Como manipular arquivos em Python – Hashtag Programação](https://www.youtube.com/watch?v=yLzFfJ2_BSg)

---

## 3. Testes Automatizados (unitários e TDD)

### ✅ Tópicos
- `unittest`: testes unitários
- `pytest` (extra para testes mais limpos)
- Teste de funções puras
- Criação de testes por TDD

### 📚 Leitura
- [Testes unitários com unittest – DevMedia](https://www.devmedia.com.br/testes-unitarios-em-python/33645)
- [Documentação oficial unittest (pt-br)](https://docs.python.org/pt-br/3/library/unittest.html)

### 🎥 Videoaulas
- [Testes com unittest (CodeShow)](https://www.youtube.com/watch?v=QU2X1wP4bVE)
- [Testes Automatizados com Pytest – Hashtag Programação](https://www.youtube.com/watch?v=Qzf1a--rhp8)

---

## 4. Logs e Tratamento de Erros

### ✅ Tópicos
- Try/except estruturado
- Logging com `logging`
- Criação de arquivos `.log` com erros
- Níveis: DEBUG, INFO, WARNING, ERROR, CRITICAL

### 📚 Documentação
- [Logging em Python – DevMedia](https://www.devmedia.com.br/log-em-aplicacoes-python/40412)
- [Python Logging – Documentação oficial em português](https://docs.python.org/pt-br/3/howto/logging.html)

### 🎥 Videoaulas
- [Como usar LOGS em Python – Bruno Rocha](https://www.youtube.com/watch?v=1QLJmsMFFJ0)
- [Tratamento de Exceções com Try/Except – Curso em Vídeo](https://www.youtube.com/watch?v=F0mxfU9X3nU)

---

## 5. Modularização e Organização de Projetos

### ✅ Tópicos
- Separar código por responsabilidade: `main.py`, `utils.py`, `models/`, `services/`
- `__init__.py` e pacotes
- Reuso e manutenção

### 📚 Leitura
- [Estrutura de Projetos Python - Pythontips (em inglês)](https://pythontips.com/2013/07/28/structuring-your-project/)
- [Organização de projetos em Python – Hashtag](https://www.hashtagtreinamentos.com/organizar-projeto-python)

### 🎥 Videoaulas
- [Organizando projetos Python – Otávio Miranda](https://www.youtube.com/watch?v=I0q5MxfGop0)
- [Modularização e Pacotes – Curso em Vídeo](https://www.youtube.com/watch?v=nKxNEDboC6c)

---

## 6. Documentação com docstrings e README

### ✅ Tópicos
- Padrão Google ou reStructuredText (reST)
- Gerando documentação com `pydoc`
- Criando README.md claro e técnico

### 📚 Leitura
- [Guia de docstrings Google Style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- [Como escrever um bom README – Gist do GitHub](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

### 🎥 Videoaulas
- [Docstrings e documentação no Python – Código Fluente](https://www.youtube.com/watch?v=Q2FYm6-XdSg)
- [Como escrever um README no GitHub – Vida de Programador](https://www.youtube.com/watch?v=Q9PWVxWeYAo)

---

## 🛠️ Dica Extra – Ferramentas e Bibliotecas

- `rich`: interface colorida no terminal
- `pylint` e `flake8`: análise de qualidade de código
- `black`: formatação automática de código

### 🎥 Videoaulas
- [Como deixar o terminal bonito com rich – Filipe Deschamps](https://www.youtube.com/watch?v=U5Cw1x5tA1Q)
- [Como usar o Black, Flake8 e isort – Código Simples](https://www.youtube.com/watch?v=7ZGhT_8GEC8)

---

## 🔜 Próximo Projeto

**Gestor de Estoque com Persistência + Testes Automatizados**  
📦 Salvar produtos em `.json`  
🧪 Testes unitários com `unittest`  
📁 Organização modular completa  
📝 Registro de logs de erros

---

## ⏰ Sugestão de Estudo Diário (2h/dia)

| Dia | Tema | Ação |
|-----|------|------|
| 1 | POO avançada | Aula + 2 exemplos próprios |
| 2 | Arquivos | Aula + salvar produtos em `.json` |
| 3 | Logs e erros | Aula + gravar `.log` com erro |
| 4 | Testes | Aula + criar testes com `unittest` |
| 5 | Modularização | Refatorar projeto |
| 6 | Documentação | Escrever README + docstrings |
| 7 | Projeto final | Consolidar tudo e subir no GitHub |

