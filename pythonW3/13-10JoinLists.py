# Join Two Lists - 3 formas

# 1º
num1=['um','dois','tres']
num2=['quatro','cinco','seis']
num3 = num1 + num2
print(num3)

# 2º
for n in num2:
    num1.append(n)
print(num1)

num1=['um','dois','tres']
#3º extend
num1.extend(num2)
print(num1)