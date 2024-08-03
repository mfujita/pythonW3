# Read Files
f = open('demofile.txt','r')
print(f.read())

# Read Only Parts of the File
# Imprima 5 caracteres
print('5 caracteres')
f = open('demofile.txt','r')
print(f.read(5))

# Read Lines → retorna uma linha
print(' --- Imprime uma linha!')
f = open('demofile.txt','r')
print(f.readline())

print(' *** Lendo 2 linhas consecutivas')
f = open('demofile.txt','r')
print(f.readline())
print(f.readline())

print('  \'\'\' Imprimindo linha a linha')
f = open('demofile.txt','r')
for linha in f:
    print(linha)

# Close Files
print('   +++ É uma boa prática fechar o recurso que acessa o arquivo.')
f = open('demofile.txt','r')
print(f.readline())
f.close()