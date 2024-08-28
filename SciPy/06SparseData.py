# Sparse Data
# What is Sparse Data
# Sparse Data é um conjunto de dados que apresenta uma grande quantidade de valores ausentes ou nulos. Exemplo de uma array esparso:
# [1, 0, 2, 0 , 0, 3, 0, 0, 0, 0, 0]
# Na computação científica quando lida-se com derivadas parciais em álgebra linear depara-se com dados esparsos.

# How to Work With Sparse Data
# SciPy tem um módulo, scipy.sparse que fornece funções para lidar com dados esparsos.
# Há primariamente 2 tipos de matrizes esparsas:
'''
CSC → Compressed Sparse Column. Para aritmética eficiente, rápida e rápido fatiamento de colunas.
CSR → Compressed Sparse Row. Para fatiamento rápido de linhas e para produto vetorial de matrizes.
'''
# CSR Matrix → scipy.sparse.csr_matrix()

import numpy as np
from scipy.sparse import csr_matrix
array1=np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print('csr_matrix(array1)')
print(csr_matrix(array1))
'''
<Compressed Sparse Row sparse matrix of dtype 'int32'
        with 3 stored elements and shape (1, 9)>
  Coords        Values
  (0, 5)        1
  (0, 6)        1
  (0, 8)        2
'''

# Sparse Matrix Methods
# Visualzando dados armazenados (não os items zero) com a propriedade data:

array2=np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print('csr_matrix(array2)')
print(csr_matrix(array2))
'''
<Compressed Sparse Row sparse matrix of dtype 'int32'
        with 3 stored elements and shape (3, 3)>     
  Coords        Values
  (1, 2)        1
  (2, 0)        1
  (2, 2)        2
'''

# Contando os valores diferentes de zero com o método count_nonzero()
print('Contando os valores diferentes de zero')
print(csr_matrix(array2).count_nonzero()) # 3

# Removendo os valores iguais a zero com o método eliminate_zeros()
print('Removendo valores diferente de zero')
withoutZero =csr_matrix(array2)
withoutZero.eliminate_zeros()
print(withoutZero) # Entendi que mostra os índices da matriz que os elementos são diferentes de zero.
'''
<Compressed Sparse Row sparse matrix of dtype 'int32'
        with 3 stored elements and shape (3, 3)>
  Coords        Values
  (1, 2)        1
  (2, 0)        1
  (2, 2)        2
'''

# Eliminando valores duplicados com o método sum_duplicates()
print('sum_duplicates()')
mat = csr_matrix(array2)
mat.sum_duplicates()
print(mat)

# Convertendo matriz do tipo CSR para CSC com o método tocsc()
print('tocsc()')
arrayCSC=csr_matrix(array2).tocsc()
print(arrayCSC)

# Matrizes esparsas suportam oprações como reshaping, summing, arithmetic broadcasting etc.

