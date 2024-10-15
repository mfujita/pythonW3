import os

source=r'C:\Livros\arq2\trimmed'
destination=r'C:\Livros\arq2\trimmed\pronto'
for file in os.listdir(source):
    num=int(file.replace('pag','').replace('.jpg',''))
    newNumber=num-7
    os.rename(os.path.join(source, file), os.path.join(destination, 'pag'+str(newNumber)+'.jpg')) # Como renomear arquivos
    print(newNumber)