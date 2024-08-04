# Array Indexing
import numpy as np
array1 = np.array([0,1,2,3])
print(array1[2])

print('Operação através dos índices')
print(array1[1] + array1[3])

# Access 2-D Arrays
# Acesse o elemento da 1ª coluna, segunda coluna
array2D = np.array([[1,2,3,4],[3,6,8,4]])
print(array2D[0,1])

# Access 3-D Arrays
# Acesse o 3º elemento do segundo array do primeiro array
array3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array3D[0,1,2])
# 0 → é o array [1,2,3],[4,5,6]
# 1 → é o array [4,5,6]
# 2 → é o elemento 

# Negative Indexing → acessa a partir do final
arrayNeg = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('Último elemento da 2º dimensão → ', arrayNeg[-1,-1])
