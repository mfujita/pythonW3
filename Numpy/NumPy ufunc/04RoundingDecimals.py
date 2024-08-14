# Rounding Decimals
'''
5 formas de arredondar usando NumPy:
- truncation
- fix
- rounding
- floor
- ceil
'''
# Truncation → Remove os números decimais retornando um float mais próximo de zero.
import numpy as np
array1=np.array([1.234, 2.689, -1.42, -3.78])
print('array original', array1)
array1truncated=np.trunc(array1)
print('trunc', array1truncated)

# fix
array1fix=np.fix(array1)
print('fix',array1fix)

# Rounding → arredonda para cima se o algarismo a ser descartado for >= 5
array1around = np.around(array1,1)
print('round', array1around)

# Floor → arredonda o inteiro para baixo
array1floor=np.floor(array1)
print('floor',array1floor)

# Ceil → arredonda o inteiro para cima
array1ceil=np.ceil(array1)
print('ceil', array1ceil)