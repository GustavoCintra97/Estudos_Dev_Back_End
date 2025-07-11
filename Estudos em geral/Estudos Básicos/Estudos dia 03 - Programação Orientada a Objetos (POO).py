from dataclasses import dataclass

#1 - Crie uma classe Pessoa com nome e idade.

@dataclass
class Pessoa:
    nome: str
    idade: int

#2 - Adicione um método falar() que exibe uma mensagem com o nome da pessoa.
    def falar(self):
        print(f"Olá, {self.nome}.")

p = Pessoa("Gustavo",28)
p.falar()

#3 - Crie uma classe ContaBancaria com depositar() e sacar().
#4 - Adicione verificação de saldo antes de sacar.
@dataclass
class ContaBancaria:
    saldo: float

    def depositar(self):
        valor = float(input("Digite o valor que deseja Depositar: "))
        self.saldo += valor
        print(f"Depósito realizado com sucesso! Saldo atual: {self.saldo}.")
        return self.saldo

    def sacar(self):
        valor = float(input("Digite o valor que deseja Sacar: "))
        while True:
            verifica = input(f'Seu saldo é de {self.saldo}, deseja sacar?\nDigite "S" para Sim e "N" para não: ').upper()
            if verifica == "S":
                self.saldo -= valor
                print(f"Saque realizado com sucesso! Saldo atual: {self.saldo}.")
                return self.saldo
            elif verifica == "N":
                print(f"Seu saldo continua o mesmo: {self.saldo}.")
                break
            else:
                print("Resposta inválida, tente novamente.")
    
    def exibir(self):
        print(f"Seu Saldo é de {self.saldo}.")

saldo = ContaBancaria(20000)
saldo.exibir()
saldo.depositar()
saldo.sacar()

#5 - Crie herança: Funcionario herda de Pessoa, com atributo salario.
@dataclass
class Funcionario(Pessoa):
    salario: float

fun = Funcionario("Gustavo", 28, 3200)
fun.falar()

#6 - Crie uma classe Produto com preço e nome, e método para aplicar desconto.
@dataclass
class Produto:
    nome: str
    preco: float

    def desconto(self):
        desconto = self.preco * 0.02
        precoDesc = self.preco - desconto
        print(f"Você obteve 20% de desconto, ficando um total de {precoDesc}.")
        return precoDesc

carrinho = Produto("Carrinho", 150)
carrinho.desconto()

#7 - Crie uma Loja com lista de produtos e método listar_produtos().
@dataclass
class Loja:
    nome: str
    produtos: list

    def adicionarProduto(self, produtos):
        self.produtos.append(produtos)
        print(f'\nO Produto "{produtos}" foi adicionado a loja {self.nome} com sucesso.')

    def listarProdutos(self):
        if not self.produtos:
            print(f'\nA loja {self.nome} não possui produtos cadastrados.')
            return

        print(f"\nLista de produtos da loja {self.nome}:")
        for p in self.produtos:
            print(f" - {p}")

loja = Loja("Cintra", [])

loja.adicionarProduto("Carrinho")
loja.adicionarProduto("Barquinho")
loja.adicionarProduto("Motinha")
loja.adicionarProduto("Bonequinho")
loja.adicionarProduto("Roupinha")

loja.listarProdutos()

#8 - Crie um sistema com Aluno e Curso, onde aluno se inscreve em cursos.
@dataclass
class Aluno:
    nome: str
    matricula: int
    cursos: list

    def matriculaCurso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            print(f"\n{self.nome} matriculado em {curso.nome}")
        else:
            print(f"\n{self.nome} já está matriculado em {curso.nome}")
    
    def listarCursos(self):
        if self.cursos:
            print(f"\nCursos de {self.nome}:")
            for curso in self.cursos:
                print(f"- {curso.nome}")
        else:
            print(f"\n{self.nome} não está matriculado em nenhum curso.")
@dataclass
class Curso:
    nome: str
    cargaHoraria: int
    alunos: list

    def adicionarAluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            print(f"\n{aluno.nome} adicionado ao curso {self.nome}")
        else:
            print(f"\n{aluno.nome} já está no curso {self.nome}")
    
    def listarAlunos(self):
        if self.alunos:
            print(f"\nAlunos do curso {self.nome}:")
            for aluno in self.alunos:
                print(f"- {aluno.nome}")
        else:
            print(f"\nNenhum aluno matriculado no curso {self.nome}.")

ber = Aluno("Bernardo", 3535,[])
gus = Aluno("Gustavo", 4646,[])
jhe = Aluno("Jhennifer", 2727,[])

cursoPython = Curso("Python",50,[])
cursoJava = Curso("Java",70,[])

ber.matriculaCurso(cursoPython)
gus.matriculaCurso(cursoPython)
jhe.matriculaCurso(cursoJava)

ber.listarCursos()
gus.listarCursos()
jhe.listarCursos()

cursoPython.adicionarAluno(ber)
cursoPython.adicionarAluno(gus)
cursoJava.adicionarAluno(jhe)

cursoPython.listarAlunos()
cursoJava.listarAlunos()

#9 - Crie uma classe Carro com velocidade e métodos acelerar() e frear().
@dataclass
class Carro:
    nome: str
    velocidade: int

    def acelerar(self):
        self.velocidade += 10
        print(f"\nVelocidade do veículo {self.nome} aumentada para {self.velocidade}km/h")
        return self.velocidade
    
    def frear(self):
        if self.velocidade == 0:
            print("\nSeu veículo está parado, acelere!")
        else:
            self.velocidade -= 10
            print(f"\nVelocidade do veículo {self.nome} reduzida para {self.velocidade}km/h")
            return self.velocidade

c = Carro("BMW",50)
c.acelerar()
c.acelerar()
c.frear()
c.frear()
c.frear()
c.frear()
c.acelerar()
c.acelerar()
c.acelerar()