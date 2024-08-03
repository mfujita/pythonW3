# File Write/Create
import datetime
# Para escrever em um arquivo, pode-se acrescentar textos a um arquivo existe ou criar um arquivo
'''
"a" append
"w" write
'''
fileName = 'myNewFile.txt'
f = open(fileName,'w')
f.write('This text is my first text stored in a file.')
f.close()

print('   +++ Imprimindo o contéudo do meu primeiro arquivo criado')
f=open(fileName)
print(f.readline())
f.close()

print('   $$$ O atributo w cria um novo arquivo. Portanto, se um arquivo com o mesmo nome de arquivo existe, será sobrescrito.')
f = open(fileName,'w')
f.write('A new text overwritting a previous file.')
f.close()

f = open(fileName,'r')
print(f.readline())
f.close()

# Create a New File
'''
"x" cria um novo arquivo. Retorna erro se o erro existe.
"a" acrescenta conteúdos ao arquivo existente. Cria o arquivo caso não exista
"w" escreve um novo arquivo
'''

# f = open('arquivoVazio.txt','x') # cria um arquivo vazio
# f.close()

# Crie um arquivo com uma unica linha. Em seguida acrescente novas linhas.
f = open('arquivoVariasLinhas.txt','w')
f.write('Hoje é dia 02/08/2024')
f.close()

f = open('arquivoVariasLinhas.txt','a')
data1 = datetime.datetime(2024,8,2)
f.write('\nÉ uma sexta-feira.')
diaDoAno = data1.strftime('%j')
f.write(f'\n{diaDoAno}º dia do ano.')
f.write('\nOs meninos vieram comigo para casa.')
f.write('\nComecei a usar a pomada Trok-G para combater a dermatite de contato.')
f.write('\nEnzo está se recuperando dos vômitos e diarreias que o enfraqueceram.')
f.close()


