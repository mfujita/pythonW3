# Data Types
''' Python
string  → textos
integer → números inteiros
float   → números reais
boolean → True or False
complex → os números complexos
'''

''' Numpy
i integer
b boolean
u unsigned integer
f float
c complex float
m timedelta
M datetime
O object
S string
U unicode string
V fixed chunk of memory for other type (void)
'''

# Checking the Data Type of an Array → dtype retorna o tipo do dado de um array
import numpy as np
array1 = np.array([1,2,3,4,5])
print(array1.dtype)

array2 = np.array(['Murilo','Enzo','Hugo'])
print(array2.dtype) # <U6

# Creating Arrays With a Defined Data Type → array() tem como argumento dtype para definir o tipo dos elementos
array3 = np.array([1,2,3,4], dtype='S')
print(f'array3: {array3} \ntype: {array3.dtype}')

array4 = np.array([1,2,3,4], dtype='i4')
print(array4)
print(array4.dtype)

# Converting Data Type on Existing Arrays → método astype() modifica o tipo de dados criando um NOVO array
array5=np.array([1.1, 2.2, 3.3, 4.4])
novoArray5 = array5.astype('i')
print(novoArray5)
print(novoArray5.dtype)

print('Modificando de inteiros para boolean')
array6 = np.array([1,0,10, 0, -1])
novoArray6 = array6.astype(bool)
print(novoArray6)
print(novoArray6.dtype)  # 0 → False. Qualquer número → True


