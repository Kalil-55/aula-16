#Vamos simular o comportamento de veículos. Você precisa criar uma classe base Veiculo e uma classe filha CarroEletrico. Crie a classe Veiculo com um método chamado acelerar. Este método deve imprimir a mensagem "O veículo está acelerando.". Crie uma classe CarroEletrico que herde de Veiculo. Na classe CarroEletrico, sobrescreva o método acelerar para que ele imprima uma mensagem mais específica, como "O carro elétrico está acelerando silenciosamente.". Crie uma instância de Veiculo e outra de CarroEletrico. Chame o método acelerar para cada uma e observe a diferença de comportamento.

class Veiculo:
    def __init__(self, cor:str, velocidade: int):
        self.cor = cor
        self.velocidade = velocidade
    def acelerar(self):
        print(f"O carro da cor {self.cor} está acelerando a {self.velocidade}km/h")

    
class CarroEletrico(Veiculo):
    def acelerar(self):
        print("O carro elétrico está acelerando silenciosamente.")

ato_veiculo = Veiculo("prata", 120)
ato_veiculo.acelerar()
ato_carro_eletrico = CarroEletrico("preto",150)
ato_carro_eletrico.acelerar()
