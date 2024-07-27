# Dictionary Methods
# clear
# copy
# fromkeys → atribui o valor para cada chave
diaSemana = ['sexta', 'sabado', 'domingo']
saldo = 0
diaSemanaComSaldo = dict.fromkeys(diaSemana, saldo)
print('diaSemanaComSaldo → ', diaSemanaComSaldo, 'len → ', len(diaSemanaComSaldo))

letras = ('a', 'b', 'c')
numeros = (1,2,3)
dicionario = dict.fromkeys(letras, numeros)
print('dicionario → ', dicionario, 'len(dicionario) → ', len(dicionario))

# get
# items()
# keys()
# pop()
# popitem()
# setdefault()
professional = {
    'job' : 'developer',
    'salary' : '100k/year',
    'knowledges' : ['console', 'web', 'mobile']
}
result = professional.setdefault('local',"home office")
print(result) # key local não existia. Foi atribuída
newResult = professional.setdefault("job","enginner")
print(newResult) # key job existia. Está armazenada o valor padrão negando o novo valor atribuído.

# update()
# values()