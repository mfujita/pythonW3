# Array Join → concanate()
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([6,5,4])
unidos = np.concatenate((array1, array2))
print(unidos) # [1 2 3 6 5 4]

# Unindo 2 arrays2D no eixo 1
array3 = np.array([[1,2],[3,4]])
array4 = np.array([[5,6],[7,8]])
axis1 = np.concatenate((array3,array4),axis=1)
print('axis = 1')
print(axis1)
'''
[[1 2 5 6]
 [3 4 7 8]]
'''

# Joining Arrays Using Stack Functions → similar ao concatenate, porém stacking é feito ao longo de um novo eixo
array5 = np.array([1,2,3])
array6 = np.array([4,5,6])
empilhado = np.stack((array5, array6), axis=0)
print('stack((arr, arr), axis=0)')
print(empilhado)
'''
[[1 2 3]
 [4 5 6]]
'''

empilhado2 = np.stack((array5, array6), axis=1)
print('stack((arr,arr),axis=1)')
print(empilhado2)
'''
[[1 4]
 [2 5]
 [3 6]]
'''

# Stacking Along Rows → empilha ao longo das linhas
array7 = np.array([1,2,3])
array8 = np.array([4,5,6])
empilhadoAoLongoDaLinha = np.hstack((array7, array8))
print('hstack')
print(empilhadoAoLongoDaLinha) # [1 2 3 4 5 6]

# Stacking Along Columns → empilha ao longo das colunas
empilhadoAoLongoDeColunas = np.vstack((array7, array8))
print('vstack')
print(empilhadoAoLongoDeColunas)
'''
[[1 2 3]
 [4 5 6]]
'''

# Stacking Along Height (depth) → dstack: empilha ao longo da altura que é o mesmo que profundidade
stackHeight = np.dstack((array7,array8))
print('dstack')
print(stackHeight)
'''
[[[1 4]
  [2 5]
  [3 6]]]
'''