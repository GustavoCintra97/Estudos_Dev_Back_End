from dataclasses import dataclass
from produto import Produto

@dataclass
class Estoque:
    nomeEstoque: str
    produtos: list[Produto]
    
    def __str__(self):
        if not self.produtos:
            return f'Estoque "{self.nomeFormatado()}" está vazio.'
        texto = f'Estoque "{self.nomeFormatado()}":\n'
        for i, produto in enumerate(self.produtos, 1):
            texto += f"  {i}. {produto}\n"
        return texto.strip()
    
    def nomeFormatado(self):
        return self.nomeEstoque.capitalize()