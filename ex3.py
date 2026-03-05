#Sua tarefa é criar uma classe base ContaBancaria e uma subclasse ContaSalario. O objetivo é usar super() para garantir a correta inicialização da classe base e para estender o comportamento de um método. Crie a classe ContaBancaria com um construtor (__init__) que recebe e armazena o titular e o saldo em atributos. Adicione um método exibir_saldo que imprima o saldo atual da conta. Crie uma subclasse ContaSalario que herde de ContaBancaria. O construtor de ContaSalario deve receber o titular, o saldo e um limite_saque_diario. Ele deve usar super() para chamar o construtor de ContaBancaria, inicializando o titular e o saldo. Crie um método sacar na ContaSalario que, antes de realizar o saque, use super() para chamar o método exibir_saldo da superclasse, e depois realize o saque.

class ContaBancaria:
    def __init__(self, titular: str, saldo:int):
        self.titular = titular
        self.saldo = saldo
    def exibir_saldo(self):
        print(f"Senhor(a): {self.titular}, seu saldo é de R${self.saldo:.2f}")
              
class ContaSalario(ContaBancaria):
    def __init__(self, titular: str, saldo:int, limite_saque_diario:int):
        super().__init__(titular,saldo)
        self.limite_saque_diario = limite_saque_diario
        print(f"Parabéns senhor(a): {self.titular}, seu saldo é de {self.saldo} e o seu limite de saque diário é {self.limite_saque_diario}")
    
    def sacar(self, valor: int):
        if valor > self.limite_saque_diario:
            print("Saque excede o limite diário.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque realizado! Novo saldo: R${self.saldo:.2f}")


   

uso_conta_bancaria = ContaBancaria('Arnoldo', 13440)
uso_conta_bancaria.exibir_saldo() 
uso_conta_salario = ContaSalario('Xanderson', 4500, 1200)
uso_conta_salario.sacar(1000)

