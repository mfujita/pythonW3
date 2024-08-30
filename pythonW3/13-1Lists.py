print('Lists são criadas usando colchetes!')
sentimentos=['Conquista','Vitória','Superação']
print(sentimentos)
print(sentimentos[0])
print(sentimentos[1])
print(sentimentos[2])
print('Tamanho da lista: ', len(sentimentos))

print('Lists permitem mistura de tipos de dados:')
print(['Python',10,True,2.54,False])
print("Independente do tipo dos elementos de uma list, o uso de type() sempre retorna 'List'.")
print(type([1,2,3]), type(["Um","dois","três"]))

print('Usndo um construtor:')
myList=list(("quatro", "cinco", "seis"))
print(myList, type(myList))

print()
print('LIST. Obedece uma ordem, permite mudança de valores e aceita valores duplicados.')
print('TUPLE. Obedece uma ordem, não aceita mudança de valores e aceita valores duplicados.')
print('SET. Não obedece uma ordem, não aceita mudança de valores (mas pode adicionar ou remover elementos), não são indexados e não admitem valores duplicados.')
print('DICTIONARY. Python 3.6- (não obedece ordem). Python 3.7+ (são ordenados). Permitem mudança de valores e não aceitam valores duplicados.')