variavel="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(variavel)

nome='Murilo Fujita'
print(nome[0], nome[1], nome[2], nome[5])

print('Loops em strings')
for x in nome:
    print(x, end=' ')
    
print('Contagem de caracteres')
print(len(nome))
numero=1234
print(len(str(numero)))
print('Para contar a quantidade de algarismos, antes deve-se converter o número em string.')

print('Acusando True or False se uma subcadeia existe na cadeia de caracteres.')
afirmativa="Aprender Python para ter uma vida melhor!"
print("Tem vida? ","vida" in afirmativa)
print("tem erro? ","erro" in afirmativa)

print('Para inverter o resultado do bool, use NOT')
print("Tem vida? ","vida" not in afirmativa)
print("tem erro? ","erro" not in afirmativa)