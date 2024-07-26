# Classes Objects
class firstClass:
    print('firstClass')
print(firstClass)

# Create Object
class secondClass:
    x = 10

objClass = secondClass()
print(objClass.x)

# A função __init__() atribui valores para as proprieddes dos objetos ou outras operações que necessárias quando o objeto está sendo criado.
# Atribua valores como nome e idade para a uma função da classe Pessoa
# __init__() é chamado sempre que classe cria um novo objeto.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Ela", 29)

print(f'{p1.nome} ({p1.idade})')
print('type ', type(({p1.idade})))

# A função __str()__() controla o que deve ser retornado quando o objeto é uma string.
# # Caso a função __str__() não seja configurada, a string do objeto é retornada.
class Pessoa2:
    def __init__(self, nome, sobrenome, numero):
        self.nome = nome
        self.sobrenome = sobrenome
        self.numero = numero
    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.numero})"
    
p2 = Pessoa2("Murilo", "Fujita", 10)
print(p2)

# Métodos dos objetos
class Pessoa3:
    def __init__(self,nomeAluno, n1, n2):
        self.nome = nomeAluno
        self.nota1 = n1
        self.nota2 = n2
    
    def calculaMedia(self):
        return (self.nota1 + self.nota2)/2

myObj = Pessoa3('Zezo', 6, 4)
print(f'{myObj.nome} média {myObj.calculaMedia()}')

# self é uma referência à instância de uma classe e é usada para acessar variáveis que pertençam à classe.
# Pode ser usado qualquer nome desde que seja o primeiro parãmetro
class Pessoa4:
    def __init__(coisa, nomeFabricante, nomeModelo):
        coisa.fabricante = nomeFabricante
        coisa.modelo = nomeModelo
    def imprimeFrase(coisa):
        print(coisa.fabricante + ' fabrica o modelo ' + coisa.modelo)

objPessoa4 = Pessoa4('Toyota','Corolla')
objPessoa4.imprimeFrase()

# Modificar as propriedades do objeto
class Pessoa5():
    def __init__(self, nome, idade):
        self.name = nome
        self.age = idade
    def imprime(self):
        print(f'{self.name} tem {self.idade}.')
objPessoa5 = Pessoa5('Nárnia', 23)
objPessoa5.age = 36
print(objPessoa5.age)

# Apagar a propriedade de um objeto
class Pessoa6:
    def __init__(self, carro, potencia):
        self.car = carro
        self.power = potencia

objPessoa6 = Pessoa6('Uno',54)
del objPessoa6.power
# print(objPessoa6.power) # Esta propriedade não está definido

del objPessoa6
# print(objPessoa6.car) # Este objeto não está definido

# Use pass quando a classe não tem conteúdo evitando alcançar um erro
class Pessoa7:
    pass

objPessoa7 = Pessoa7()