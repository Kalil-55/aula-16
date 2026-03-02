#Sua tarefa é criar um sistema simples de hierarquia de animais usando o conceito de herança. Crie uma classe base chamada Animal. Esta classe deve ter um construtor (__init__) que recebe o nome do animal e o armazena em um atributo self.nome. Adicione um método chamado comer à classe Animal. Este método deve simplesmente imprimir uma mensagem genérica, como "O animal está comendo.". Crie uma nova classe chamada Cachorro que herde da classe Animal. O construtor do Cachorro deve receber o nome e a raça. Ele deve chamar o construtor da classe Animal para inicializar o nome. Adicione um método latir à classe Cachorro. Este método deve imprimir uma mensagem como "Au au!". Crie uma instância da classe Cachorro e demonstre que ela pode usar tanto o método comer (herdado da classe Animal) quanto o método latir (próprio da classe Cachorro).

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f"O animal {self.nome} está comendo.")

class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.raça = raça

    def latir(self):
        print ("Au Au!")
    
atos_cachorro = Cachorro("Angu","Border collie")
atos_cachorro.comer()
atos_cachorro.latir()
