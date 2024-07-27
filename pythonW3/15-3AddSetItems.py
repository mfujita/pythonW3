# Add Set Items
carros = set(('uno','gol','fox'))
carros.add('bmw')
for carro in carros:
    print(carro)

# Add Sets → update
com1digito = {1,2,3}
com2digitos = {10,20,30}
print('com1digito', com1digito)
print('com2digitos', com2digitos)
com1digito.update(com2digitos)
print('com1digito', com1digito)

# o comando update adiciona elementos de outras estruturas de dados
set1 = {1,2,3}
lista = ['x','y','z']
set1.update(lista)
print('set1', set1)
