# Array Split → operação contrária à operação de unir
# Joining une vários arrays em um enquanto que splitting quebra um array em múltiplos.
# array_split()
import numpy as np
array1 = np.array([1,2,3,4,5,6])
newArray1 = np.array_split(array1, 3)
print('array_split(arr,3)')
print(newArray1) # [array([1, 2]), array([3, 4]), array([5, 6])]

# Se o array tiver menos elementos do que a forma de fatiar, os elementos no final do array serão ajustados
ajustedArray = np.array_split(array1,4)
print('array_split(arr,4)')
print(ajustedArray) # [array([1, 2]), array([3, 4]), array([5]), array([6])]

# Split Into Arrays 
array1 = np.array([1,2,3,4,5,6])
array1Splitted = np.array_split(array1,3)
print('Acessando cada array pelo seu índice')
print(array1Splitted[0])
print(array1Splitted[1])
print(array1Splitted[2])

# Splitting 2-D Arrays
array2 = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
newArray2 = np.array_split(array2, 3)
print('array2D splitted')
print(newArray2)
'''
[array([[1, 2],[3, 4]]), 
 array([[5, 6],[7, 8]]),
 array([[ 9, 10], [11, 12]])]
'''

array3 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
newArray3 = np.array_split(array3, 3, axis=1)
print('array_split(arr, 3, axis=1)')
print(newArray3)
'''
[array([[ 1], [ 4], [ 7], [10], [13], [16]]),
 array([[ 2], [ 5], [ 8], [11], [14], [17]]),
 array([[ 3], [ 6], [ 9], [12], [15], [18]])]
'''

newArray3 = np.array_split(array3, 3, axis=0)
print('array_split(arr, 3, axis=0)') # axis = 0 → obtém a mesma quantidade de elementos do array original
print(newArray3)
'''
[array([[1, 2, 3], [4, 5, 6]]),
 array([[ 7,  8,  9], [10, 11, 12]]),
 array([[13, 14, 15], [16, 17, 18]])]
'''

array4 = np.array([[10,11,12,13], [14,15,16,17], [18,19,20,21], [22,23,24,25]])
newArray4 = np.array_split(array4,2, axis=0)
print('np.array_split(array4,2, axis=0)')
print(newArray4)
'''
[array([[10, 11, 12, 13], [14, 15, 16, 17]]),
 array([[18, 19, 20, 21], [22, 23, 24, 25]])]
'''

# hsplit faz a operação oposta ao hstack
array5 = np.array([[11,12,13],[14,15,16],[17,18,19],[20,21,22],[23,24,25],[26,27,28]])
newArray5 = np.hsplit(array5,3)
print('np.hsplit(array5,3)') # Divide um array em 3 arrays
print(newArray5)
'''
[array([[11], [14], [17], [20], [23], [26]]),
 array([[12], [15], [18], [21], [24], [27]]),
 array([[13], [16], [19], [22], [25], [28]])]
'''

newArray5 = np.vsplit(array5, 3)
print('np.vsplit(array5, 3)')
print(newArray5)
'''
[array([[11, 12, 13], [14, 15, 16]]),
 array([[17, 18, 19], [20, 21, 22]]),
 array([[23, 24, 25], [26, 27, 28]])]
'''

'''
dsplit only works on arrays of 3 or more dimensions # Não entendi como funciona dsplit
newArray5 = np.dsplit(array5,3)
print('np.dsplit(array5,3)')
print(newArray5)
'''

# Concluo que as operações array_split, hsplit e vsplit recebem como parãmetro um array e um número que determina em quantos arrays serão divididos.