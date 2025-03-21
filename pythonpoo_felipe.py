class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_quantidade(self, quantidade):
        if self.quantidade + quantidade >= 0:
            self.quantidade += quantidade
        else:
            raise ValueError("Quantidade indisponível no estoque")

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Venda:
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos
    
    def registrar_venda(self):
        for produto, quantidade in self.produtos.items():
            if produto.quantidade >= quantidade:
                produto.atualizar_quantidade(-quantidade)
            else:
                raise ValueError(f"Quantidade insuficiente de {produto.nome} em estoque")

    def mostrar_detalhes_venda(self):
        detalhes = f"Cliente: {self.cliente.nome}\nProdutos comprados:\n"
        total = 0
        for produto, quantidade in self.produtos.items():
            subtotal = produto.preco * quantidade
            detalhes += f"{produto.nome} - {quantidade} X R$ {produto.preco:.2f} = R$ {subtotal:.2f}\n"
            total += subtotal
        detalhes += f"Total da venda: R$ {total:.2f}"
        return detalhes

class SistemaVendas:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.vendas = []

    def cadastrar_produto(self, nome, preco, quantidade):
        novo_produto = Produto(nome, preco, quantidade)
        self.produtos.append(novo_produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Preço: R$ {produto.preco:.2f}, Quantidade: {produto.quantidade}")

    def editar_produto(self, nome, novo_preco, nova_quantidade):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.preco = novo_preco
                produto.quantidade = nova_quantidade
                return
        raise ValueError("Produto não encontrado")

    def excluir_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                return
        raise ValueError("Produto não encontrado")

    def cadastrar_cliente(self, nome, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                raise ValueError("CPF já cadastrado")
        novo_cliente = Cliente(nome, cpf)
        self.clientes.append(novo_cliente)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}")

    def editar_cliente(self, cpf, novo_nome):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                cliente.nome = novo_nome
                return
        raise ValueError("Cliente não encontrado")

    def excluir_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                self.clientes.remove(cliente)
                return
        raise ValueError("Cliente não encontrado")

    def registrar_venda(self, cpf_cliente, produtos_comprados):
        cliente = next((c for c in self.clientes if c.cpf == cpf_cliente), None)
        if not cliente:
            raise ValueError("Cliente não encontrado")

        produtos = {}
        for nome, quantidade in produtos_comprados.items():
            produto_encontrado = next((p for p in self.produtos if p.nome == nome), None)
            if not produto_encontrado:
                raise ValueError(f"Produto {nome} não encontrado")
            produtos[produto_encontrado] = quantidade

        venda = Venda(cliente, produtos)
        venda.registrar_venda()
        self.vendas.append(venda)
        print("Venda registrada com sucesso")
        print(venda.mostrar_detalhes_venda())

    @staticmethod
    def menu():
        sistema = SistemaVendas()
        while True:
            print("\nMenu:")
            print("1 - Cadastrar produto")
            print("2 - Listar produtos")
            print("3 - Editar produto")
            print("4 - Excluir produto")
            print("5 - Cadastrar cliente")
            print("6 - Listar clientes")
            print("7 - Editar cliente")
            print("8 - Excluir cliente")
            print("9 - Registrar venda")
            print("10 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome do produto: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade disponível: "))
                sistema.cadastrar_produto(nome, preco, quantidade)
                print("Produto cadastrado com sucesso")
            
            elif opcao == "2":
                sistema.listar_produtos()
            
            elif opcao == "3":
                nome = input("Nome do produto a editar: ")
                preco = float(input("Novo preço: "))
                quantidade = int(input("Nova quantidade disponível: "))
                sistema.editar_produto(nome, preco, quantidade)
                print("Produto editado com sucesso")
            
            elif opcao == "4":
                nome = input("Nome do produto para excluir: ")
                sistema.excluir_produto(nome)
                print("Produto excluído")
            
            elif opcao == "5":
                nome = input("Nome do cliente: ")
                cpf = input("CPF do cliente: ")
                sistema.cadastrar_cliente(nome, cpf)
                print("Cliente cadastrado com sucesso")
            
            elif opcao == "6":
                sistema.listar_clientes()
            
            elif opcao == "7":
                cpf = input("CPF do cliente a editar: ")
                novo_nome = input("Novo nome: ")
                sistema.editar_cliente(cpf, novo_nome)
                print("Cliente editado com sucesso")
            
            elif opcao == "8":
                cpf = input("CPF do cliente para excluir: ")
                sistema.excluir_cliente(cpf)
                print("Cliente excluído")
            
            elif opcao == "9":
                cpf = input("CPF do cliente: ")
                produtos_comprados = {}
                while True:
                    nome_produto = input("Nome do produto (ou 'fim' para terminar): ")
                    if nome_produto.lower() == "fim":
                        break
                    quantidade = int(input("Quantidade: "))
                    produtos_comprados[nome_produto] = quantidade
                sistema.registrar_venda(cpf, produtos_comprados)
            
            elif opcao == "10":
                print("Saindo...")
                break
            
            else:
                print("Opção inválida, tente novamente")

if __name__ == "__main__":
    SistemaVendas.menu()
