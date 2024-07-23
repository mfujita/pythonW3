# Remove List Items → remove()

fruits=["abacate","banana", "caqui"]
print(fruits)
fruits.remove("banana")
print(fruits)

# Quando há mais de uma ocorrência do que será removido, a primeira ocorrência é removida
nomes=['ana','bia','gabi','elen','bia','tati','bia']
print(nomes)
nomes.remove('bia')
print(nomes)

# Remove Specified Index → pop(index)
nomes=['ana','bia','gabi','elen','bia','tati','bia']
nomes.pop(2)
print(nomes)

# Na ausência de um índice do comando pop, o último elemento é eliminado
nomes.pop()
print(nomes)

# Apagar um List (fica inacessível. Qualquer comando chamando a list que sofre um del resulta em erro)
del nomes
# print(nomes)

# remover os itens da List, mas manter esta List em memória
lista = ["1",'2','3']
print(lista)
lista.clear()
print('Elementos da lista', lista)
