class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def atualizar_quantidade(self,quantidade):
        if self.quantidade + quantidade >= 0:
            self.quantidade += quantidade
        else: 
            raise ValueError("Quantidade insuficiente")

class Cliente:  
    
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf  
    
class Venda:
            
