# ufuncs intro → "universal functions" e operam com objetos ndarray.
# Why use ufuncs?
'''
São usadas para implementar vetorização em NumPy que é mais rápido do que iterar sobre elementos.
Fornecem transmissão e métodos adicionais como reduce, accumulate. Tem argumentos adicionais:
where → array de booleanos ou condições definindo onde as operações devem ser colocadas.
dtype → define o retorno do tipo dos elementos.
out → array de saída que retorna valor que deve ser copiado.
'''

# What is Vectorization?
# A conversão de instruções iterativas em operações baseadda em vetor é chamada de vetorização. 
# As CPUs atuais são otimizadas para estas operações.

# Faça a soma elemento a elemento das 2 listas e armazene em um terceiro array
array1=[1,2,3,4]
array2=[4,5,6,7]
arraySoma=[]
for i,j in zip(array1,array2):
    arraySoma.append(i+j)
print('zip')
print(arraySoma)

# O mesmo problema usando Numpy
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([4,5,6,7])
arraySoma=np.add(array1,array2)
print('np.add')
print(arraySoma)

