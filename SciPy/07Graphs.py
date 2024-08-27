# Graphs → são estruturas essenciais de estrtura de dados.
# SciPy fornece o módulo scipy.sparse.csgraph para trabalhar com tais estrturas de dados.

# Matriz de adjacência
# Adjacência é uam matriz nxn sendo que n é o número de elementos em cada grafo.
# Os valores representam a conexão entre os elementos.

# Connected Components
# Encontre todos os componentes conectados com o método connected_components()
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy. sparse import csr_matrix
array1= np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
connected=csr_matrix(array1)
print(connected_components(connected)) # (1, array([0, 0, 0]))

array2= np.array([
    [0,1,2],
    [1,0,1],
    [2,1,0]
])
connected=csr_matrix(array2)
print(connected_components(connected)) # (1, array([0, 0, 0]))

# Dijkstra → encontra o caminho mais curto no grafo de um elemento para outro. Os argumentos são:
'''
1. return_predecessors → True para retornar todo caminho transversal. Caso não, use False.
2. indices → índice do elemento para retornar todos os caminhos de um elemento apenas.
3. limit → peso máximo do caminoh
'''
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csc_matrix

array3=([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
arrayDijkstra=csr_matrix(array3)
print('Dijkstra')
print(dijkstra(arrayDijkstra, return_predecessors=True, indices=0)) # (array([0., 1., 2.]), array([-9999,     0,     0]))

# Floyd Warshall → enconra o menor caminho entre todos os pares de elementos.
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

array4=np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
arrayFloyd=csr_matrix(array4)
print('floyd_warshall')
print(floyd_warshall(arrayFloyd, return_predecessors=True))
'''
(array([[0., 1., 2.],
       [1., 0., 3.],
       [2., 3., 0.]]), 
 array([[-9999,     0,     0],
       [    1, -9999,     0],
       [    2,     0, -9999]]))
'''

# Bellman Ford
# O métodos bellman_ford() também encontra o caminho mais curto entre todos os pares dos elementos, mas este método pode manipular com pesos negativos.
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

array5 = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

bellman = csr_matrix(array5)
print('bellman')
print(bellman_ford(bellman, return_predecessors=True, indices=0))
# (array([ 0., -1.,  2.]), array([-9999,     0,     0]))

# Depth First Order
# O método depth_first_order() retorna a primeira profundidade transversal de um nó. Argumentos:
'''
1. o grafo
2. o elemento inicial que atravessa o grafo
'''
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

array6 = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

depth = csr_matrix(array6)
print('depth_first_order')
print(depth_first_order(depth, 1))
# (array([1, 0, 3, 2]), array([    1, -9999,     1,     0]))

# Breadth First Order
# O método breadth_first_order() retorna a primeira travessia em largura de um nó. Argumentos:
# 1. o graph
# 2. o elemento inicial que atravessa o grafo

import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

array7 = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

breadth = csr_matrix(array7)
print('breadth_first_order')
print(breadth_first_order(breadth, 1))
# (array([1, 0, 2, 3]), array([    1, -9999,     1,     1]))