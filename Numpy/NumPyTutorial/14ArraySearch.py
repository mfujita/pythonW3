# Array Search → Procurar um valor no array e retornar o índice. Comando where()
import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 4, 4])
posicao4 = np.where(array1 == 4) # (array([3, 5, 6], dtype=int64),)
print(posicao4)
print(f'O valor 4 aparece nas posições: {str(posicao4).replace('(array(','').replace(', dtype=int64),)','')}')

# Quais os índices que os valores são pares
indicesDosPares = np.where(array1%2==0)
print(indicesDosPares)
print(f'Os índices dos valores que são pares aparecem nas posições: {str(indicesDosPares).replace('(array(','').replace(', dtype=int64),)','')}')

# Quais os índices que os valores são ímpares
indicesDosImpares = np.where(array1%2==1)
print(indicesDosImpares)
print(f'Os índices dos valores que são pares aparecem nas posições: {str(indicesDosImpares).replace('(array(','').replace(', dtype=int64),)','')}')

# Search Sorted ? Aparetemente o número que é parâmetro é visto como o primeiro número imediatamente menor que um valor no array mantendo a ordem crescente 
array2 = np.array([6,5,4,7,8,9])
sorted6 = np.searchsorted(array2,6)
print(sorted6)
sorted7 = np.searchsorted(array2,7)
print(sorted7)
sorted8 = np.searchsorted(array2,8)
print(sorted8)
sorted9 = np.searchsorted(array2,9)
print(sorted9)

# Search From the Right Side # busca a posição para inserir do lado direito de um valor passado como parâmetro
array2 = np.array([6,7,8,9])
direita = np.searchsorted(array2, 5, side='right')
print('5 [6,7,8,9] side=right')
print(direita) # 0
direita = np.searchsorted(array2, 7, side='right')
print('7 [6,7,8,9] side=right')
print(direita) # 2

# Multiple Values
# encontre os índice para inserir os valores 2, 4 e 6 no array [1, 3, 5, 7]
array3 = np.array([1, 3, 5, 7])
multiplos = np.searchsorted(array3,[2,4,6])
print('multiplos: ', multiplos) # [1 2 3]
