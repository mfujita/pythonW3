# Remove Set Items
# Comandos remove() e discard()
versions = {'Jelly Bean', 'KitKat', 'Lollipop', 'Marshmallow', 'Nougat', 'Oreo'}
versions.remove('Jelly Bean')
print(versions)

# usar remove() quando o elemento não existe lança um erro 
# versions.remove('Jujuba')
# print(versions)

# discard
versions.discard('Marshmallow')
print(versions)
# usar discard() referindo a um elemento que não existe não lança um erro
versions.discard('quebra-queixo')
print(versions)

# pop() remove um elemento de forma aleatória
versions.pop()
print('depois do pop()', versions)

# clear() esvazia o set
versions.clear()
print('depois do clear() → imprimirá o TIPO do nome da estrutura de dados: \'set()\'', versions)

# del → a variável deixa de ser definida
del versions
# print(versions) # erro

