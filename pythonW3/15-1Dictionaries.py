# Dictionaries
# A partir da versão 3.7 os dictionaries são ordenados. Versão anteriores não são ordenadas.
# Dictionaries são envolvidos por chaves. Tanto as chaves quanto os valores textuais são envolvidos por aspas.

myDict = {
    "nome" : "Murilo",
    "sobrenome" : "Fujita",
    "profissão" : "developer"
}
print(myDict)
print(myDict["nome"])
print(myDict["sobrenome"])
print(myDict["profissão"])

# Não ter order significa que não pode ser acessado por um índice.
# Quando um dictionary tiver chaves duplicadas, o último valor correspondente a esta chave será armazenada porque os valores anteriores serão sobrescritos.
myDict2 = {
    "nome" : "Murilo",
    "sobrenome" : "Fujita",
    "profissao" : "professor",
    "profissao" : "developer"
}
print('myDict2 → ', myDict2)
print('myDict2["profissao"] → ', myDict2["profissao"])

# len() # imprime o número de chaves do dictionary
print('len(myDict) → ', len(myDict))
print('len(myDict2) → ', len(myDict2))

# Data Types
carros = {
    "fabricante" : "Honda",
    "eletrico" : True,
    "anoFabricacao" : 2024,
    "cores" : ['preto', 'cinza', 'azul metálico']
}
print(carros)

# type
print('type(carros) → ', type(carros))

# The dict() Constructor
computer = dict(fabricante = 'Intel', modelo = 'i7', geracao=14)
print('type(computer) → ', type(computer))
