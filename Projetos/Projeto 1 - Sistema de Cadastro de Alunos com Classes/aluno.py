from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    nota: list

    def __str__(self):
        media = sum(self.nota) / len(self.nota) if self.nota else 0
        return f"\n{self.nome} (Idade: {self.idade}, Média: {media:.2f})"