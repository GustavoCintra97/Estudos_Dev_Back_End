from dataclasses import dataclass
from aluno import Aluno

@dataclass
class Turma:
    nomeTurma: str
    alunos: list[Aluno]

    def mediaGeral(self):
        contagem = 0
        soma = 0
        for i in self.alunos:
            for n in i.nota:
                contagem += 1
                soma += n
        media = soma / contagem if contagem > 0 else 0
        print(f"\nA média geral da turma é {media}.")
        return media