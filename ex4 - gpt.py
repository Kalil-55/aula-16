class Pedido:
    def __init__(self, nome_produto: str, preco: float):
        self.nome_produto = nome_produto
        self.preco = preco

    def processar_envio(self):
        print(f"Enviando pedido do produto {self.nome_produto}.")


class PedidoEletronico(Pedido):
    def __init__(self, nome_produto, preco, serial_number: int):
        super().__init__(nome_produto, preco)
        self.serial_number = serial_number

    def processar_envio(self):
        print(f"Adicionando seguro e número de série {self.serial_number} ao pacote.")


class PedidoRoupa(Pedido):
    def __init__(self, nome_produto, preco, tamanho: str):
        super().__init__(nome_produto, preco)
        self.tamanho = tamanho

    def processar_envio(self):
        print(f"Adicionando embalagem especial para vestuário. Tamanho - {self.tamanho}")


pedido1 = Pedido("colher", 55.2)
pedido2 = PedidoEletronico("faca", 30, 279773)
pedido3 = PedidoRoupa("camisa", 12, "G")

lista_pedidos = [pedido1, pedido2, pedido3]

for pedido in lista_pedidos:
    pedido.processar_envio()