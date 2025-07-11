class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    def insereEndereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    
    def listaEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} / {self.estado} FOI APAGADO')
