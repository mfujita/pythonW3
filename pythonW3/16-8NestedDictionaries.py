# Nested Dictionaries
familia = {
    "pai" : {
        'nome' : 'Murilo',
        'nascimento' : 1977
    },
    "filho1" : {
        'nome' : 'Enzo',
        'nascimento' : 2017,
    },
    'filho2' : {
        'nome' : 'Hugo',
        'nascimento' : 2019
    }
}
print(familia)

# Crie separadamento cada dictionary e junte-os em outro
print('crie separadamento cada dictionary e junte-os em outro')
pai = {
    'nome' : 'Murilo',
    'nascimento' : 1977
}
filho1 = {
    'nome' : 'Enzo',
    'nascimento' : 2017
}
filho2 = {
    'nome' : 'Hugo',
    'nascimento' : 2019
}
superTime = {
    "pai" : pai,
    "filho1" : filho1,
    'filho2' : filho2
}
print(superTime)

# para acessar um elemento dentro do dictionary que contém dictionaries
print(superTime['pai']['nome'])
print(superTime['filho1']['nascimento'])

# loop através do nested dictionaries
print('loop através do nested dictionaries')
for principal, chave in superTime.items():
    print(principal)
    for item in chave:
        print(f' {item:<15} {chave[item]:<15}')