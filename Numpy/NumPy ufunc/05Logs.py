# Logs → Calcula log de base 2 e base 10
# É possível usar o log em outras bases.
# Quando não puder calculado, será devolvido -inf ou inf.

# Log at Base 2
import numpy as np
array1=np.arange(1, 10)
print(np.log2(array1))
print('Log 2 de 1 a 9')
for n in array1:
    print(n, np.log2(n))

# Log at Base 10
array2=np.arange(1,11)
print(np.log10(array2))

# Natural Log, or Log at Base e
print('log na base e de 1 a 10')
print(np.log(array2))

# Log at Any Base
# Deve-se usar a função frompyfunc() e imbutir a função math.log com 2 parâmetros e um parâmetro de saída
from math import log
nplog=np.frompyfunc(log, 2,1)
print(nplog(100,15))
