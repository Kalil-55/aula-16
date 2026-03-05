#Sua tarefa é desenvolver um pequeno sistema de processamento de pedidos que lide com diferentes tipos de produtos, utilizando herança, sobrescrita, super() e polimorfismo. Crie uma classe base chamada Pedido. O construtor deve receber um nome_produto e um preco. Adicione um método processar_envio que imprima "Enviando pedido de produto genérico.". Crie duas subclasses de Pedido: PedidoEletronico e PedidoRoupa. Sobrescreva o método processar_envio em ambas as subclasses com mensagens mais específicas. Em PedidoEletronico, a mensagem deve ser print(f"Adicionando seguro e número de série {self.serial_number} ao pacote."). Em PedidoRoupa, a mensagem deve ser print(f"Adicionando embalagem especial para vestuário. Tamanho - {self.tamanho}"). Em ambas as subclasses, o construtor (__init__) deve usar super() para inicializar os atributos da classe base. Crie uma lista com instâncias de PedidoEletronico e PedidoRoupa. Use um loop for para iterar sobre a lista de pedidos e chame o método processar_envio para cada item. Isso demonstrará o polimorfismo, onde a mesma chamada de método tem comportamentos diferentes.

class Pedido:
    def __init__(self, nome_produto: str,preco:int):
        self.nome_produto = nome_produto
        self.preco = preco

    def Processar_envio(self, processar_o_envio: bool):
        self.processar_o_envio = processar_o_envio
        print("Enviando pedido de produto genérico {self.processar_o_envio}.")

class PedidoEletronico(Pedido):
    def
        
       