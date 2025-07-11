'''
public, protected, private
_ protected
__ private
'''
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados

    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def listaCliente(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagaCliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()

bd.inserirCliente(1, 'Gustavo')
bd.inserirCliente(2, 'Bernardo')
bd.dados = 'Outro valor'
print(bd.dados)
# bd.__dados = 'Outra Coisa'
# print(bd.__dados)
# print(bd._BaseDeDados__dados)
# bd.listaCliente()

# bd.inserirCliente(1, 'Gustavo')
# bd.inserirCliente(2, 'Bernardo')
# bd._dados = 'Outra Coisa'
# bd.listaCliente()

# bd.inserirCliente(1, 'Gustavo')
# bd.inserirCliente(2, 'Bernardo')
# bd.inserirCliente(3, 'Jhennifer')
# bd.dados = 'Outra coisa'
# bd.apagaCliente(2)