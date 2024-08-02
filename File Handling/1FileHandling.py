# File Handling
# open(filename, mode)
'''
"r" valor padrão. Abre o arquivo para leitura. Causa um erro se o arquivo não existe
"a" cria um arquivo para o append. Cria o arquivo se nçao existe
"w" modo para escrita. Cria o o arquivo se não existe
"x" modo de criação. Causa um erro se o arquivo existe

"t" Valor padrão. Modo texto
"b" Modo binário. (por exemplo, imagens)
'''

# Forma 1
# f = open("demofile")
# Forma 2
# f = open("demofile", "rt")
# As formas 1 e 2 têm o mesmo efeito