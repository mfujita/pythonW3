# Summations
# Addition → operação entre 2 argumentos. Retorna um array com mesmo shape dos arrays envolvidos.
# Summation → operação entre n elementos. Retorna um escalar.
import numpy as np
array1=np.array([11,22,33])
array2=np.array([3,2,1])
arrayAdd=np.add(array1,array2)
print('add',arrayAdd) # [14 24 34]

arraySummation=np.sum([array1,array2])
print('sum',arraySummation) # 72 

# Summation Over an Axis → Soma os números em cada eixo (linha). Retorna um array com a mesma quantidde de arrays envolvidos na operação. 
array3=np.array([1,3,5])
array4=np.array([2,4,6])
arrayAxis1=np.sum([array3,array4],axis=1)
print(arrayAxis1) # [ 9 12]

# Cummulative Sum → cumsum(array)
# faz operações de soma acumulando o próximo elemento
# [1,2,3,4] → [1, 1+2, 1+2+3, 1+2+3+4] = [1,3,6,10]
# retorna um array com o mesma shape do array
array5=np.array([10,20,30,40,50])
arrayCumsum=np.cumsum(array5)
print(arrayCumsum)