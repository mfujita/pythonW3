# Numpy Random
# Generate Random Number (inteiro)
import numpy as np # exercício para criar um array
from numpy import random
aleatorio = random.randint(100)
print(aleatorio)

# Generate Random Number (real)
for i in range(5):
    randomFloat = random.rand()
    print(f'{randomFloat} {randomFloat:.2f}')

# Generate Random Array
arrayRandom = random.randint(10, size=4)
print(arrayRandom)

# Gerando um array 2D com 3 linhas e cada linha tem 5 valores aleatórios
array2D = random.randint(10,100, size=(3,5))
print('random.randint(100, size=(3,5)')
print(array2D)

# Gerar um array de float com 5 elementos
array1 = random.rand(5)
print(array1)
print('Imprindo o mesmo array com 2 casas decimais')
arrayCom2CasasDecimais = []
for i in array1:
    arrayCom2CasasDecimais.append(f'{i:.2f}')
print(arrayCom2CasasDecimais)


# Gerar um array2D com 3 linhas por 5 colunas
array2 = random.rand(3,5)
print('array2D com 3 linhas por 5 colunas')
print(array2)
print('O mesmo array sendo exibindo com 2 casas decimais')
print(np.around(array2, decimals=2))

# Generate Random Number From Array
# O método choice() gera número aleatório baseados no array de valores. Recebe como parãmetro um array e retorna um array um dos valores.
array3=random.choice([1,2,3,5])
print(array3)

# Praticando
for i in range(5):
    array4 = random.choice([12, 23, 34, 45, 56, 67, 78, 89, 94])
    print(array4)

# size() especifica o tamanho do array com os números aleatórios
array5=random.choice([1,3,5,7,9,15], size=(3,5)) # Imprime 3 arrays com 5 elementos tirados do array que está no parãmetro do método choice
print('size=(3,5)')
print(array5) 
'''
[[ 1  9  3  5  1]
 [ 7  9  7  7  3]
 [15  9  1  3  3]]
'''
