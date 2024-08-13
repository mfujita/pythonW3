# Create Function
# How To Create Your Own ufunc
# Pra criar sua própria ufunc, você tem que definir uma função igual como você faz com funções normais em Python. Depois você adiciona sua biblioteca ufunc com o método frompyfunc()
# o método frompyfunc() tem os argumentos:
'''
function() →o nome da função
inputs() → o número de argumentos de entrada (array)
outputs() → o número de arrays de saída
'''
import numpy as np

def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4], [5,6,7,8]))

# Check if a Function is a ufunc
print(type(np.add)) # <class 'numpy.ufunc'>

# Verificando o tipo np.concatenate()
print(type(np.concatenate)) # <class 'numpy._ArrayFunctionDispatcher'>

# Como checar se a função é uma ufunc ou não:
import numpy as np
if type(np.add) == np.ufunc:
    print('add é uma ufunc')
else:
    print('dd não é uma ufunc')