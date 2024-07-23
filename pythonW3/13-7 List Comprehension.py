# List Comprehension
nomes = ["Murilo", "Enzo", "Hugo", "Maira", "Mario", "Tere"]
nomesComLetra_A = []

for nome in nomes:
    if 'a' in nome:
        nomesComLetra_A.append(nome)
print(nomesComLetra_A)
nomesComLetra_A.clear()

nomesComLetra_A = [x for x in nomes if 'a' in x]
print(nomesComLetra_A)

de1ate10 = [x for x in range(1,11)]
print(de1ate10)

print('Imprime ate 10, mas armazena até 5')
ate5 = [x for x in range(1,11) if x < 6]
[print(x) for x in ate5]