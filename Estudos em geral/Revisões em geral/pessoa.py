from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def apresentar(self):
        return f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos'
    
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\n'

@dataclass(init=False)
class Funcionario(Pessoa):
    cargo: str
    _salario: float

    def __init__(
            self, 
            nome: str, 
            idade: int, 
            cargo: str, 
            salario: float
            ):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        base = super().apresentar()
        return f'{base}, meu cargo é {self.cargo}'

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        if valor < 1000:
            raise ValueError('O salário deve ser maior que 1000!')
        self._salario = valor
    
    def __str__(self):
        base = super().__str__()
        return f'{base}Cargo: {self.cargo}\nSalário: R${self.salario:.2f}'

class Gerente(Funcionario):

    def apresentar(self):
        base = super().apresentar()
        return f'{base} e atualmente, sou responsável por todo Setor.'
    
    def aumentar_salario(self, percentual=5):
        self.salario += self.salario * (percentual / 100)
    
    def __str__(self):
        base = super().__str__()
        return base

g = Gerente("Gustavo", 28, "Gerente", 12000)
print(g.apresentar())
print(g)
g.aumentar_salario(10)
print(f"Novo salário: R${g.salario:.2f}")
print(isinstance(g, Funcionario))