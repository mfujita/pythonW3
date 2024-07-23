# Tuplas são indexadas
tupla1 = ("Mike", 5421, True)
print(tupla1)
print(tupla1[0])
print(tupla1[1])
print(tupla1[2])

# Tuplas permitem valores repetidos
nomes = ['bia','ana', 'tati', 'elen', 'ana']
print(nomes)

# Tendo apenas um item na tupla, é necessário adicionar uma vírgula
exemplo1 = ("um",)
exemplo2 = ("dois")
print("exemplo1", type(exemplo1), " exemplo2 ", type(exemplo2))

# Construtor
novaTupla = tuple(("um", "dois", "tres"))
print(novaTupla, type(novaTupla))