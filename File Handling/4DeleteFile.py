# Delete File → precisa importar o módulo os e usar os.remove()
import os
# os.remove('arquivoVariasLinhas.txt')

# Uma boa prática é verificar se o arquivo antes de realizar a operação de apagar o arquivo
if os.path.exists('arquivoVariasLinhas.txt'):
    os.remove('arquivoVariasLinhas.txt')
else:
    print('Este arquivo não existe.')

# Delete Folder → os.rmdir()
# os.rmdir('diretorio') # Causa um erro por tentar apagar um diretório inexistente

# IMPORTANTE: somente diretórios vazios podem ser removidos