# Differences → diferenças discretas significam subtrair 2 elementos sucessivos. Exemplo:
# [1,2,3,4] → [2-1, 3-2, 4,3] = [1,1,1]
# Use comando diff()
import numpy as np
array1 = np.array([5, 12, 16, 28])
diferencas = np.diff(array1)
print(diferencas) # [7 4 12]
# fazendo uma vez a operação é n-1 sendo n o número de elementos

# o parâmetro n indica quantas vezes a operação deve ser feita sucessivamente
array2=np.array([13, 21, 34, 46, 57, 62, 74, 88, 95])
diferencasNvezes=np.diff(array2,3)
print('9 elementos, 3 operações → retorna um array de 6 elementos')
print(diferencasNvezes)