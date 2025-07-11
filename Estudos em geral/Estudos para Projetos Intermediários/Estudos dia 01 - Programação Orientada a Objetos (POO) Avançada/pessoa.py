from random import randint

class Pessoa:
    anoAtual = 2025
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self):
        print(self.anoAtual - self.idade)

    @classmethod
    def porAnoNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)

    @staticmethod
    def geraId():
        rand = randint(10000, 19999)
        return rand

# p1 = Pessoa.porAnoNascimento('Gustavo', 1997)
p1 = Pessoa('Gustavo', 28)
print(p1)
print(p1.nome, p1.idade)
p1.getAnoNascimento()
print(Pessoa.geraId())
print(p1.geraId())