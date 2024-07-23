# Loop Lists
lista = ["um",'dois','tres']
for i in lista:
    print(i)
    
# Loop Through the Index Numbers
numeros = ['quatro', 'cinco', 'seis']
for i in range(len(numeros)):
    print(numeros[i])
    
# Using a While Loop
i=0
while i < len(numeros):
    print(numeros[i])
    i+=1
    
# Looping Using List Comprehension
[print(x) for x in lista]