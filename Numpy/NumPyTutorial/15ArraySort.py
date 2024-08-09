# Array Sort → os objetos ndarray são ordenados com o comando sort()
import numpy as np
array1=np.array([2,4,1,0,3])
print('sort', np.sort(array1))
print('original', array1)

arrayWords = np.array(['Murilo', 'Hugo', 'Enzo'])
sortedNames = np.sort(arrayWords)
print(sortedNames)

arrayBoolean = np.array([True, False, True, False])
boolSorted = np.sort(arrayBoolean)
print('bool ', boolSorted)

# Sorting a 2-D Array → As matrizes são independentes. Então os elementos de cada matriz são ordenados: mat1, mat2, mat3, ...
array2D = np.array([[3,1,4],[10,-7,3]])
sorted2D = np.sort(array2D)
print('2D\n', sorted2D)