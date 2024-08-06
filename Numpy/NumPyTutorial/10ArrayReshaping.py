# Array Reshaping → altera a dimensão do array ou altera o número de elementos de cada dimensão
# Reshape From 1-D to 2-D
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array1reshaped = array1.reshape(4,3)
print(array1reshaped)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''
# Observação: os valores na tuple do reshape devem ser compativeis com o novo tamanho da matriz

# Reshape From 1-D to 3-D
array3D = array1.reshape(2,3,2) # São 2 arrays que tem 3 arrays com 2 elementos cada um 
print('Array3D')
print(array3D)
'''
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
'''

# Returns Copy or View?
array2 = np.array([1,2,3,4,5,6,7,8])
print(array2.reshape(2,4).base) # [1 2 3 4 5 6 7 8] Portanto, é View

# Unknown Dimension
# Ao passar -1 para o Numpy, será calculado este número.
print('Unknown dimension')
array2unknownDim = array2.reshape(2,2,-1)
print(array2unknownDim)

test = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
unkDim = test.reshape(2,4,-1)
print('unknown')
print(unkDim)

mat3x3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
newMat3x3 = mat3x3.reshape(3,3,-1)
print('3x3')
print(newMat3x3)
'''
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]

 [[13 14]
  [15 16]
  [17 18]]]
'''

# Flattening the arrays → converte para array1-D
largeMat = np.array([[1,2,3],[4,5,6],[7,8,9]])
array1D = largeMat.reshape(-1)
print('array1D')
print(array1D)