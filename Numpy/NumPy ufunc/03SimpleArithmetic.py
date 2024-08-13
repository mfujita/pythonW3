# Simple Arithmetic
# Condições aritméticas → pode-se definir condições para as operações aritméticas → where()

# Addition
import numpy as np
array1=np.array([11,12,13,14])
array2=np.array([18,17,16,15])
arraySoma=np.add(array1,array2)
print(arraySoma)

# Subtraction
array3=np.array([10,20,30,40])
array4=np.array([5,8,14,25])
arrayMenos=np.subtract(array3,array4)
print(arrayMenos)

# Multiplication
array5=np.array([3,7,12,4])
array6=np.array([10,3,4,5])
arrayMult=np.multiply(array5, array6)
print(arrayMult)

# Divide
array7=np.array([60,45,30,20])
array8=np.array([12,15,3,4])
arrayDiv=np.divide(array7,array8)
print(arrayDiv)

# Power
array9=np.array([4,3,5,6])
array10=np.array([3,5,4,2])
arrayPot=np.power(array9,array10)
print(arrayPot)

# Remainder
# mod() 
# remainder() 
array11=np.array([42,37,23,18])
array12=np.array([6,9,7,4])
arrayRestoMod=np.mod(array11, array12)
print('array11 → ', array11)
print('array12 → ', array12)
print('arrayRestoMod → ', arrayRestoMod)

array13=np.array([42,37,23,18])
array14=np.array([6,9,7,4])
arrayRestoRemainder=np.remainder(array13, array14)
print('array13 → ', array13)
print('array14 → ', array14)
print('arrayRestoRemainder → ',arrayRestoRemainder)

# Quotient and Mod
# retornam os array que calculam o quociente e o mod → divmod()
array15=np.array([42,37,23,18])
array16=np.array([6,9,7,4])
arrayQuoMod=np.divmod(array15,array16)
print(arrayQuoMod)

# Absolute Values
array17=np.array([-5,-3,-1,-4,-2])
arrayAbs=np.absolute(array17)
print(arrayAbs)