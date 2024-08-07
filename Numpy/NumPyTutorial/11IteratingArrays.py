# Iterating Arrays → varrer elemento por elemento em um array
# Iterating 2-D Arrays
import numpy as np
array1 = np.array([[0,1,2], [7,8,9]])
for item in array1:
    print(item)

# Para exibir cada elemento (escalar), deve ter um laço de repetição para cada dimensão
for coluna in array1:
    for linha in coluna:
        print(linha)

# Iterating 3-D Arrays
print('Dimensão 3')
array2 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [1,4,7]]])
indice=1
for item in array2:
    print(f'Array {indice}')
    print(item)
    indice+=1
'''
Array 1
[[1 2 3]
 [4 5 6]]
Array 2
[[7 8 9]
 [1 4 7]]
'''

# Imprimindo os escalares do mesmo array (array2)
for dim1 in array2:
    for dim2 in dim1:
        for dim3 in dim2:
            print(dim3)

# Iterating Arrays Using nditer() → facilita a iteração para as aulas dimensionalidades
print('np.nditer(argument)')
for x in np.nditer(array2):
    print(x)

# Iterating Array With Different Data Types → op_dtypes modifica o tipo do dado enquanto realiza iteração
print('op_dtypes')
array3 = np.array([1,2,3])
for x in np.nditer(array3,flags=['buffered'], op_dtypes='S'):
    print(x)
'''
b'1'
b'2'
b'3'
'''

# Iterating With Different Step Size → filtragem durante a iteração
# Itere sobre os elementos do array2D de 2 em 2
print('De 2 em 2')
array4 = np.array([[0,2,4,6], [1,3,5,7]])
for x in np.nditer(array4[:, ::2]):
    print(x)
'''
0
4
1
5
'''

# Enumerated Iteration Using ndenumerate() → menciona o número da sequência relacionando o índice do elemento com o seu valor.
array5 = np.array([1,2,3])
for idx, x in np.ndenumerate(array5):
    print(idx, x)
'''
(0,) 1
(1,) 2
(2,) 3
'''

print('Usando ndenumerate em Array2D')
array6 = np.array([[1,2,3],[4,5,6]])
for idx, x in np.ndenumerate(array6):
    print(idx, x)
'''
(0, 0) 1
(0, 1) 2
(0, 2) 3
(1, 0) 4
(1, 1) 5
(1, 2) 6
'''