# Sort List Alphanumerically
letras = ['bia','ana', 'tati', 'elen']
print(letras)
letras.sort()
print(letras)

# Sort List numerically
numeros = [5,2,8,4,7]
numeros.sort()
print(numeros)

# reverso
numeros.sort(reverse=True)
print(numeros)

# ordenando numeros proximos a um valor
def maisproximo(n):
    return abs(n - 10)

palpites = [3, 14, 8]
palpites.sort(key=maisproximo)
print(palpites)

# Case Insensitive Sort
nomes = ['Pamela', 'Gabriela', 'eloá', 'maria']
nomes.sort()
print(nomes)

nomes.sort(key = str.lower)
print(nomes)

# Reverse Order
nomes.reverse()
print(nomes)