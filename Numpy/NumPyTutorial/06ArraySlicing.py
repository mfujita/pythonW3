# Array Slicing → pegar os elementos a partir de um índice até outro índice
# [start:end]
# [start:end:step]
# A omissão do valor inicial indica o índice 0
# A omissão do valor final indica toda dimensão do array
# A omissão do passo indica 1
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[1:5]) # [2 3 4 5] → inclui o índice inicial e exlui o índice final

print(array1[4:]) # [ 5  6  7  8  9 10] → a partir do índice 4 até o final

print(array1[:4]) # [1 2 3 4] → o elemento de índice 4 não foi incluído

# Negative Slicing
print(array1[-3:-1]) # [8 9] → o último elemento (-1) não foi incluído

# STEP
print(array1[1:5:2]) # [2 4]

print(array1[::2]) # [1 3 5 7 9] → a partir do 1º elemento pulando de 2 em 2

# Slicing 2-D Arrays
array2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array2D[1, 1:4]) # [7 8 9]

print(array2D[0:2, 2]) # [3 8]

print(array2D[0:2, 1:4])
'''
[[2 3 4]
 [7 8 9]]
'''