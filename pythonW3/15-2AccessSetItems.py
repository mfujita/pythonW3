# Access Set Items
carros = set(('uno','gol','fox'))
for carro in carros:
    print(carro, end=' ') # fox uno gol
print()
# Use in para saber se certo elemento pertence ao set
print('fox' in carros) # True
print('veraneio' in carros) # False