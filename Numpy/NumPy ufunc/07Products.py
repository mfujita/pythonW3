# Products → produtório dos elementos → prod()
import numpy as np
array1=np.array([1,2,3,4,5])
products=np.prod(array1)
print(products) # 120

array2=np.array([1,2,3,4])
array3=np.array([5,6,7,8])
multBetween2arrays=np.prod([array2,array3])
print(multBetween2arrays) # 40320

# Product Over an Axis → retorna um array com a mesma quantidade de elementos dos arrays; Ex: 2 arrays, então um array com 2 elementos
array4=np.array([1,5,7,2])
array5=np.array([2,3,6,4])
onAxis=np.prod([array4, array5], axis=1)
print(onAxis) # [ 70 144]

# Cummulative Product → cumprod()
# [1,2,3] → [1, 1*2, 1*2*3]
array6=np.array([1,2,3,4,5,6,7,8])
acumulaProdutos=np.cumprod(array6)
print(acumulaProdutos) # [    1     2     6    24   120   720  5040 40320]