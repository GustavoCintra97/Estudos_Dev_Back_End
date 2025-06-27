from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int

    def __str__(self):
        return f"\n{self.nomeFormatado()} (Preço: R${self.preco:.2f}, Estoque: {self.estoque:.2f})"
    
    def nomeFormatado(self):
        return self.nome.capitalize()