# Array Copy Vs View
# A "cópia" é um novo array enquanto que a "visão" é uma visualização de um certo array.
# Ao alterar os dados da cópia, não afeta o array original. Qualquer mudança no array original não afeta a cópia.
# Mudanças na visão afetam os dados do array original. Alterações no array original não afetam a visão. 
# COPY
import numpy as np
array1 = np.array([1,2,3,4,5])
arrayCopy = array1.copy()
array1[0] = 100
print(array1) # [100   2   3   4   5]
print(arrayCopy) # [1 2 3 4 5]

# VIEW
array2 = np.array([6,7,8,9,10])
arrayView = array2.view()
array2[0] = 15
print(array2) # [15  7  8  9 10]
print(arrayView) # [15  7  8  9 10]

# Make Changes in the VIEW:
arrayView[0] = 20
print(array2) # [20  7  8  9 10]
print(arrayView) # [20  7  8  9 10]

# Check if Array Owns its Data (Verifique se o Array possui seus dados)
# O comando base retorna None se possui os dados (copy). Retorna o objeto original se for view.
array3 = np.array([1,3,5,7,9])
array3Copy = array3.copy()
array3View = array3.view()
print(array3Copy.base) # None
print(array3View.base) # [1 3 5 7 9]
