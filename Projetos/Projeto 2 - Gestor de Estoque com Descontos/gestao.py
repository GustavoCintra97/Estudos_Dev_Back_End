from dataclasses import dataclass
from estoque import Estoque

@dataclass
class Gestao:
    estoques: list[Estoque]

    def __str__(self):
        if not self.estoques:
            return f'Nenhum estoque cadastrado.'
        
        linhas = [f"Estoques cadastrados:"]
        for i, estoque in enumerate(self.estoques, 1):
            linhas.append(f"  {i}. {estoque.nomeFormatado()}")
        return "\n".join(linhas)