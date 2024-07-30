# Scope
# Local Scope → vale somente dentro de uma função
# Function Inside Function → a variável declarada em uma função externa é acessada pela função interna.
def externa():
    x = 10
    def interna():
        print(x)
    interna()

externa()

# Global Scope → a variável é acessada tanto de dentro como de fora das funções. Basta declarar fora da função.
valor = 123
def umaFuncao():
    print(valor)

umaFuncao() # Chamou a função que imprime valor
print(valor) # Imprimiu valor que está declarada fora da função

# Não é recomendado. Se a variável global tiver o mesmo nome da variável local, terão tratamentos diferentes.
numero = 321
def novaFuncao():
    numero = 12
    print(numero)
novaFuncao()  # 12
print(numero) # 321

# A palavra global → permite que uma variável local torne-se global
def minhaFuncao():
    global contemAlgo
    contemAlgo = 50
minhaFuncao()
print(contemAlgo) # acessou a variável contemAlgo que está dentro de minhaFuncao() de fora da função.

# Se a variável for declarada como global de dentro de uma função, o valor sobrescreve a variável global.
guardaAlgo = 75
def testaFuncao():
    global guardaAlgo
    guardaAlgo = 120
    print(guardaAlgo) # 120
testaFuncao()
print(guardaAlgo) # 120

# Nonlocal Keyword → são usadas para funções aninhadas fazendo a variável ser acessível para a função externa
def deFora():
    nome = 'Tiburcio'
    def deDentro():
        nonlocal nome
        nome = 'Pierre'
    deDentro()
    return nome

print(deFora()) # Pierre