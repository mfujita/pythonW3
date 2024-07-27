# Lambda
# Pequena função anônima
x = lambda a : a + 10
print(x(5))

x = lambda a,b: a*b
print(x(5,6))

soma = lambda a,b,c: a+b+c
print(soma(5,3,1))

def minhaFuncao(n):
    return lambda a : a * n

duplicador = minhaFuncao(3)
print(duplicador(10))

print('duplicador e triplicador')
def multiplicadora(n):
    return lambda x : x * n

calculo2 = multiplicadora(2)
calculo3 = multiplicadora(3)

print(calculo2(4))
print(calculo3(3))