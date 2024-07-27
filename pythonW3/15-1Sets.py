# Sets
# Sets não têm ordem (não são acessados por índice), não permite mudança dos valores dos elementos e não permite valores duplicados.
# São caracterizadas por {}.
# True e 1 são equivalentes. Portando, somente um deles será exibido.
balaioDeGato = {True, 1}
print(balaioDeGato) # imprime {True}

# False e 0 são equivalentes. Portando, somente um deles será exibido.
bagunca = {0, False}
print(bagunca)

# len → tamanho do set
queijos = {'mussarela','provolone','parmesão','brie','gorgonzola'}
print('len → ', len(queijos))

# sets podem conter elementos de tipos distintos
temDeTudo = {'Python',10,True,3.14, tuple(('vermelho','verde','azul'))}
print(temDeTudo)
# sets não armazenam lists
#temDeTudo = {['vermelho','verde','azul'],['a','b','c']}

# type() → definição do objeto
print(type(temDeTudo))

# Construtor
carros= set(('uno','gol','fox'))
print('carros é do tipo ',type(carros))
