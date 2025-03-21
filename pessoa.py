class produto:
   
    def __init__(self,nome,prc,qntd):
        self.nome = nome
        self.prc = prc
        self.qntd = qntd
   
    def atualizar_qntd_produto(self,qntd):
        if self.qntd + qntd >=0:
            self.qntd += qntd
        else:
            raise ValueError("Quantidade indisponivel no estoque")       
        
class cliente:
   
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        
class venda:
   
    def __init__(self,cliente,produtosc,qntdc):
        self.cliente = cliente
        self.produtosc = produtosc
        self.qntdc = qntdc       
   
    def registrar_venda(self):
        for produto,quantidade in self.produtosc.items():
            if produto.qtd_disponivel >= quantidade:
                produto.atualizar_qntd_produto(-quantidade)  
            else:
                raise ValueError(f"Quantidade insuficiente de {produto.nome} em estoque") 
    
    def mostrar_detalhes_vendas(self):
        detalhes = f"Cliente: {self.cliente.nome}\nProdutos comprados:\n" 
        total = 0
        for produto,quantidade in self.produtosc.items():
            subtotal = produto.prc * quantidade 
            detalhes += f"{produto.nome} - {quantidade} X R$ {produto.prc:.2f} = R${subtotal:.2f}\n"
            total += subtotal
            detalhes += f"Total da venda R${total:.2f}"
            return detalhes


class SistemaVendas:
    def __init__(self):
            self.produtos = []
            self.clientes = []
            self.vendas = []
        
    def cadastrar_produto(self,nome,prc,qntd):
            novo_produto = produto(nome,prc,qntd)
            self.produtos.append(novo_produto) 
        
    def listar_produtos(self):
            for produto in self.produtos:
                print(f"Nome: {produto.nome} Preço: R${produto.prc:.2f} Quantidade: {produto.qntd}")  
        
    def editar_produto(self, nome, novo_prc, nova_qntd):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.prc = novo_prc
                produto.qntd = nova_qntd
                return
        raise ValueError("Produto não encontrado")        
            
    def excluir_produto(self,nome):
            for produto in self.produtos:
                if produto.nome == nome:
                    self.produtos.remove(produto)
                    return
                raise ValueError("Produto não encontrado.")
        
    def cadastrar_cliente(self,nome,cpf):
            for cliente in self.clientes:
                if cliente.cpf == cpf:
                    raise ValueError("Cpf ja usado")
                novo_cliente = cliente(nome,cpf)
                self.clientes.append(novo_cliente)
                
    def listar__cliente(self):
            for cliente in self.clientes:
                print(f"Nome: {cliente.nome},CPF: {cliente.cpf}")
        
    def editar_cliente(self,cpf,novo_nome):
            for cliente in self.clientes:
                if cliente.cpf == cpf:
                    cliente.nome = novo_nome
                    return
                raise ValueError("Cliente não encontrado")
        
    def excluir_cliente(self,cpf):
            for cliente in self.clientes:
               if cliente.cpf == cpf:
                   self.clientes.remove(cliente)
                   return
               raise ValueError("Cliente não encontrado")                                    
        
    def registrar_venda(self,cpf_cliente,produtosc):
            cliente = None
            for c in self.clientes:
                if c.cpf == cpf_cliente:
                    cliente = c 
                    break
            if not cliente:
                    raise ValueError("Cliente não encontrado")
                
            produtos = {}
            for nome,quantidade in produtosc.items():
                    produto_encontrado = None
                    for p in self.produtos:
                        if p.nome == nome:
                            produto_encontrado = p
                            break
                        if not produto_encontrado:
                            raise ValueError(f"Produto {nome} não encontrado")
                        produtos[produto_encontrado] = quantidade
                
            venda = venda(cliente,produtos)
            venda.registrar_venda()
            self.vendas.append(venda)
            print("Venda Registrada com sucesso")
            print(venda.mostrar_detalhes_venda())
                
    def menu():
            sistema = SistemaVendas()
            while True:
                print("\nMenu:")
                print ("1 - cadastrar produto")          
                print ("2 - listar produto")  
                print ("3 - editar produto")   
                print ("4 - excluir produto")   
                print ("5 - Cadastrar cliente")   
                print ("6 - listar cliente")   
                print ("7 - editar cliente")   
                print ("8 - excluir cliente")       
                print ("9 - registrar venda")   
                print ("10 - sair ") 
                opcao = input("Escolha uma opcao = numero")  
            
                if opcao =="1":
                    nome = input("nome do produto:")    
                    preco = float(input("preço:"))
                    quantidade = int(input("Quantidade disponivel :"))
                    
                    sistema.cadastrar_produto(nome,preco,quantidade)
                    print ("Produtoc adastrado")
                
                elif opcao == "2":
                    sistema.listar_produtos()
                
                elif opcao== "3":
                    nome = input("nome do produto a editar:")    
                    preco = float(input("novo preço:"))
                    quantidade = int(input("nova quantidade disponivel :"))
                    
                    sistema.editar_produto(nome,preco,quantidade)
                    print ("Produto editado")   
                    
                elif opcao== "4":
                    nome = input("Nome do produto pra excluir")
                    sistema.excluir_produto(nome)
                    print ("produto apagado")
                
                elif opcao == "5":
                    nome = input("nome do cliente:")
                    cpf = input("cpf do cliente:")
                    sistema.cadastrar_cliente(nome,cpf)
                    print("cadastrado")
                
                elif opcao == "6":
                    sistema.listar__cliente()
                
                elif opcao == "7":
                    cpf = input("cpf do cliente a editar:")
                    
                    novo_nome = input("novo nome:")
                    sistema.editar_cliente(cpf,novo_nome)
                    print("cliente editado com sucesso")
                
                elif opcao == "8":
                    cpf = input("cpf do cliente para excluir")
                    sistema.excluir_cliente(cpf)
                    print("cliente excluido")   
                
                elif opcao == "9":
                    cpf = input ("cpf do cliente:")
                    produtos_comprados = {}
                    while True:
                        nome_produto = input("Nome do produto (ou 'fim' para terminar): ")
                        if nome_produto.lower() == "fim":
                            break
                        quantidade = int(input("Quantidade"))
                        produtos_comprados[nome_produto] = quantidade
                        sistema.registrar_venda(cpf,produtos_comprados)
                
                elif opcao== "10":
                    print ("saindo...")
                    break
               
                else: 
                    print("opção invalidad tente de 1 a 10")

if __name__ == "__main__":
    print("aaaaaaaaaaa")
    SistemaVendas.menu()
else:
    print("Bbbbbbbbbb")
    