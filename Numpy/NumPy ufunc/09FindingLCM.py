# Finding LCM (Lowest Common Multiple) → lcm
import numpy as np
num1=4
num2=6
myLCM=np.lcm(num1,num2)
print(myLCM)

print(np.lcm(13,17))
print(np.lcm(51,91))

# Finding LCM in Arrays → reduce()
# Encontra o MMC entre os elementos de um array
array1=np.array([3,6,9])
print('np.lcm.reduce(array1)')
print(np.lcm.reduce(array1))

# Crie um array com os elementos de 1 a 10 e obtenha o MMC destes valores
array2=np.arange(1,11)
print('np.lcm.reduce(array2)')
print(np.lcm.reduce(array2))