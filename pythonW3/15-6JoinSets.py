# Join Sets
# union() e update() unem sets
# intersection() resulta na seleção dos valores duplicados
# difference() mantem os itens do primeiro set que não estão no segundo set.
# symmetric_difference() resulta nos itens não duplicados.

# union()
acucares1 = {'glicose', 'frutose'}
acucares2 = {'dextrose', 'sacarose', 'xarope glucose-frutose'}
diabetes = acucares1.union(acucares2)
print(diabetes)

# | é equivalente a union()

# union() é capaz de unir vários sets.
sul = {'RS', 'SC', 'PR'}
sudeste = {'SP', 'MG', 'RJ', 'ES'}
centrooeste = {'MT','MS', 'GO', 'DF'}
norte={'AC','AM','PA','TO', 'RO', 'RR'}
nordeste = {'AL', 'BA','MA','PI', 'CE', 'PB','PE','RN', 'SE'}
brasil = sudeste.union(sul,centrooeste, norte, nordeste)
print(brasil)

# Usando |
paisBrasil = sul | sudeste | centrooeste | norte | nordeste
print(paisBrasil)

# union() permite unir set e outras estruturas de dados
# | une apenas set e outros sets.

# update() insere os elementos do 2º conjunto ao 1º modificando o 1º set.
paises1 = {'Brasil','Chile','Argentina'}
paises2 = {'França', 'Alemanha', 'Itália'}
paises1.update(paises2)
print(paises1)

# Caso tenha elementos repetidos em um dos set ou comuns aos 2 sets, os itens duplicados são excluídos
paises1 = {'Brasil','Chile','Argentina', 'Brasil'}
paises2 = {'França', 'Alemanha', 'Itália'}
paises1.update(paises2)
print(paises1)

paises1 = {'Brasil','Chile','Argentina'}
paises2 = {'França', 'Alemanha', 'Itália', 'Brasil'}
paises1.update(paises2)
print(paises1)

# intersection() → resulta apenas nos duplicados
paises1 = {'Brasil','Chile','Argentina'}
paises2 = {'França', 'Alemanha', 'Itália', 'Brasil'}
comunsAosDois = paises1.intersection(paises2)
print(comunsAosDois)

# & é equivalente a intersection()
# intersection() pode ser usado entre um set e qualquer outras estrutura de dados
# & é exclusivo entre sets.

# intersection_update() → os elementos comuns sobrescrevem o 1º conjunto
# set1.intersection_updaet(set2) = set2.intersection_update(set1)
refeicao1 = {'churrasco', 'massas', 'rodízio japonês', 'lanche'}
refeicao2 = {'comida chinesa', 'churrasco', 'founde'}
refeicao2.intersection_update(refeicao1)
print(refeicao2)

# difference() → resulta nos itens do 1º set que não estão no 2º set
# set1.difference(set2) ≠ set2.difference(set1)
letras1 = {'a','b','c','d'}
letras2 = {'c','d','e'}
diferenca = letras2.difference(letras1)
print(diferenca)

# - é equivalente a difference()
# difference() pode ser usado entre set e outras estrturas de dados
# - é exclusivo entre sets.

# difference_update() → resulta nos elementos que estão set1, mas não no set2 e sobrescrevem o 1º conjunto
disciplinas1 = {'matemática', 'fisica', 'química', 'inglês'}
disciplinas2 = {'inglês', 'geografia', 'português'}
disciplinas1.difference_update(disciplinas2)
print(disciplinas1)

# symmetric_difference() → resulta nos elementos distintos do 1º e 2º conjuntos. Este resultado é atribuído a um novo set.
# set1.symmetric_difference(set2) = set2.symmetric_difference(set1)
languages1 = {'python', 'C#', 'php'}
languages2 = {'javascript', 'php', 'shell script'}
languageDistinct = languages2.symmetric_difference(languages1)
print(languageDistinct)

# ^ é equivalente a symmetric_difference()
# symmetric_difference() pode ser usado entre set e outras estruturas de dados
# ^é exclusivo entre sets

# symmetric_difference_update() → resulta nos elementos distintos do 1º e 2º conjuntos atualizando o 1º conjunto
languages1 = {'python', 'C#', 'php'}
languages2 = {'javascript', 'php', 'shell script'}
languages2.symmetric_difference_update(languages1)
print(languages2)