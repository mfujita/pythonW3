# Polymorphism → muitas formas.
# Métodos, funções e operadores com o mesmo nome sendo executados em outras classes de forma diferente.

# 3 classes: Carro, Barco e Avião
class Carro:
    def __init__(self, brand, model):
        self.marca = brand
        self.modelo = model
    def mover(self):
        print('Dirija!')

class Barco:
    def __init__(self, brand, model):
        self.marca = brand
        self.modelo = model
    def mover(self):
        print('Navegue!')

class Aviao:
    def __init__(self, brand, model):
        self.marca = brand
        self.modelo = model
    def mover(self):
        print('Voe!')

objCarro = Carro('Toyota', 'Corolla')
objBarco = Barco('Rei do Pescado', 'Embarcação 3 pescadores')
objAviao = Aviao('Brigadeiro do Ar', 'Teco-teco')

for x in (objCarro, objBarco, objAviao):
    x.mover()
# O Polimorfismo permitiu usar o mesmo nome do método para as 3 classes

# Crie uma classe-pai e as classes-filhas adotarão polimorfismo.
# As classes Carro, Barco e Aviao herdarão da classe Veiculo
class Veiculo:
    def __init__(self, brand, model):
        self.marca = brand
        self.modelo = model
    def movimento(self):
        print('Trafeque pelas ruas.')

class Carro(Veiculo):
    pass

class Barco(Veiculo):
    def movimento(self):
        print('Navegue em alto mar!')

class Aviao(Veiculo):
    def movimento(self):
        print('Corte os céus!')

oCarro = Carro('Honda','Civic')
oBarco = Barco('Fragata Real', 'Timão sem rumo')
oAviao = Aviao('Bombardier','Turbo hélice')

for x in (oCarro, oBarco, oAviao):
    print(f'{x.marca:<20} - {x.modelo:<20}')
    x.movimento()

# Carro herdou o método movimento() da classe Veiculo.
# Barco e Aviao sobrescreveram o método movimento() da classe Veiculo.