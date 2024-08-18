# Set Operations
# Na matemática um conjunto é uma coleção de elementos distintos.
# As operações são interseção, união e difereça.

# Create Sets in NumPy → unique()
# Para tornar-se um conjunto é preciso recorrer à definição: os elementos são distintos em array unidimensional.
import numpy as np
array1=np.array([1,2,3,4,4,2,5,6,3,1,5])
distintos=np.unique(array1)
print('Valores distintos em um array', distintos) # [1 2 3 4 5 6]

# Finding Union
# O método ubion1d() encontra os valores distintos em 2 arrays unidimensionais
array2=np.array([1,2,3,4,5])
array3=np.array([3,4,5,6,7])
arraySet=np.union1d(array2,array3)
print('Valores distintos em 2 arrays unindos em 1 array', arraySet) #  [1 2 3 4 5 6 7]

# Finding Intersection
# Para encontrar os valores comuns a mais de um array, use o método intersection1d()
array4=np.array([1,2,3,4,5])
array5=np.array([4,5,6])
intersecao=np.intersect1d(array4,array5)
print('Array com valores comuns a 2 arrays', intersecao) # [4 5]

# Finding Difference
# Encontra os valores que estão presente no array1, mas não no array2. setdiff1d()
array6=np.array([1,2,3,4,5])
array7=np.array([3,4,5,6])
diferenca=np.setdiff1d(array6, array7, assume_unique=True)
print('Array com valores presentes no array1, mas não no array2', diferenca) # [1 2]

# Finding Symmetric Difference → setxor1d()
# Devolver um array com valores que não estão presentes em ambos conjuntos
array8=np.array([1,2,3,4])
array9=np.array([3,4,5,6])
xor1D=np.setxor1d(array8,array9, assume_unique=True)
print('União de 2 array sem a interseção', xor1D) # [1 2 5 6]