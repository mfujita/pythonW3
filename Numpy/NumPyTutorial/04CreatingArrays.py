# Creating Arrays
import numpy as np

lista = [1,2,3,4,5]
tupla = (6,7,8,9)
conjunto = {10,11,12}
list2array = np.array(lista)
tuple2array = np.array(tupla)
set2array = np.array(conjunto)
print(f'{lista} {type(list2array)}')
print(f'{tupla} {type(tuple2array)}')
print(f'{conjunto} {type(set2array)}')

# Dimensions in Arrays
# Arrays aninhados → array que tem arrays como seus elementos
# 0-D Arrays ou escalares
array0D = np.array(10)
print(array0D)

# 1-D Arrays ou arrays unidimensionais
array1D = np.array([1,2,3,4])
print(array1D)

# 2-D Arrays que tem elementos do tipo 1-D Arrays. São matrizes
# importe o módulo numpy.mat que é para operações de matrizes.
array2D = np.array( [ [-3,-2,-1], [1,2,3]])
print(array2D)

# 3-D arrays são arrays que seus elementos são matrizes
array3D = np.array( [[[1,2,5],[3,7,8]], [[3,5,8],[1,8,2]]])
print(array3D)
print('1ª matriz de array3D →')
print(array3D[0])
print('2ª matriz de array3D →')
print(array3D[1])

# Check Number of Dimensions? → atributo ndmin
print(f'array0D → ', array0D.ndim)
print(f'array1D → ', array1D.ndim)
print(f'array2D → ', array2D.ndim)
print(f'array3D → ', array3D.ndim)

# Higher Dimensional Arrays → ndim
arrayHigher = np.array([1,2,3,4], ndmin=5)
print(arrayHigher)
print('Dimensão: ', arrayHigher.ndim)