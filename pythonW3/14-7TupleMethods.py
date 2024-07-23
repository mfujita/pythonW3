# Tuple Methods
# count() → contagem de um ocorrência
t1 = ("um", "dois", "tres","quatro", "um","cinco","um","tres")
print(t1.count("um"))

# add()
conjunto1 = {1,}
conjunto1.add(2)
print(conjunto1)

conjunto1.clear()
print('conjunto1', conjunto1)

conjunto2 = {1,2,3}
conjunto2copia = conjunto2.copy()
print('conjunto2copia', conjunto2copia)

conjunto3 = {2,3,4}
conjuntoDiferenca = conjunto2-conjunto3 # quais elementos são distintos no primeiro set em relação ao segundo set
print('conjuntoDiferenca', conjuntoDiferenca)

conjunto3 = {"Murilo", "Enzo", "Hugo"}
conjunto4 = {"Enzo", "Hugo", "Fujita"}
conjunto3.difference_update(conjunto4)
print('conjunto3', conjunto3)

conjunto4.discard("Fujita")
print('discard',conjunto4)

#intersection()
conjunto5 = {"Murilo", "Enzo", "Hugo"}
conjunto6 = {"Enzo", "Hugo", "Fujita"}
conjunto7 = conjunto5.intersection(conjunto6)
print('intersection', conjunto7)

#intersection_update
conjunto8 = {'Python','C#','Shell Script', 'javascript'}
conjunto9 = {'Python', 'java', 'C', 'C#'}
conjunto8.intersection_update(conjunto9)
print('intersection_update', conjunto8)

# isdisjoint()
conj10 = {1,2,3}
conj11 = {2,3,4}
print(conj10.isdisjoint(conj11)) # False = tem valores comuns. 
conj12 = {"amarelo","verde","vermelho"}
conj13 = {"roxo", "preto", "cinza"}
print(conj12.isdisjoint(conj13)) # True = Conjuntos têm valores distrintos

# issubset()
conjMaior = {1,2,3,4,5,6}
conjMenor = {4,5,6}
print(conjMenor.issubset(conjMaior)) # True = os elementos do conjunto menor estão contidos no conjunto maior

# pop()
conjMaior.pop() # remove um elemento aleatório
print('conjMaior',conjMaior)

# issuperset()
print(conjMaior.issuperset(conjMenor)) # True = os elementos do conjunto maior tem todos os elementos do conjunto menor

# remove()
conj1a10 = {1,2,3,4,5,6,7,8,9,10}
conj1a10.remove(10) # remove o elemento e não o índice. Seja explícito sobre quem deve ser removido.
print(conj1a10)

# symmetric_difference()
de1a5 = {1,2,3,4,5}
de3a7 = {3,4,5,6,7}
resultado = de1a5.symmetric_difference(de3a7) # Retorna em um novo set os elementos distintos dos 2 conjuntos.
print(resultado)

# symmetric_difference_update()
frutas1 = {'abacaxi','laranja','banana'}
frutas2= {'goiaba','banana','abacaxi'}
frutas1.symmetric_difference_update(frutas2) # Retorna os elementos distintos dos conjuntos1 e conjuntos2 atribuindo o resultado para conjunto1 
print(frutas1)

# union()
carro1 = {'civic','corolla', 'fusion'}
carro2 = {'gol','uno','fox'}
novosCarros = carro1.union(carro2)
print(novosCarros)

# update()
carro2.update(carro1) # Adiciona novos elementos vindos dos sets, lists, tuples ou qualquer outro iterável
print(carro2)
