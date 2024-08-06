# Array → o formato de um array é o número de elementos em cada dimensão
# o atributo shape retorna um tuple com as dimensões da matriz 
import numpy as np
array1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(array1.shape)
array2 = np.array([[1,2], [3,4], [5,6]])
print(array2.shape)
array3 = np.array([[1,2,3], [3,2,1], [1,3,2]])
print(array3.shape)
array4 = np.array([[0,1], [2,4], [5,4], [3,2]])
print(array4.shape)