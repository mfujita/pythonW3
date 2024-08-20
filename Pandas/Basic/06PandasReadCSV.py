# Pandas Read CSV
'''
Uma forma de armazenar grandes massas de dados é empregar arquivos CSV.
Este arquivos são do tipo texto plano.
'''
import pandas as pd
df1=pd.read_csv('C:\\apagar\\Mencoes2.csv')
print(df1)

print('usando to_string()')
print(df1.to_string()) # imprime o DataFrame completo

# Quando o DataFrame tem um tamanho expressivo, são impressas as 5 primeiras linhas, um pontilhado para indicar a descontinuidade e as 5 últimas linhas.

# max_rows → esta opção exibe o número máximo de linhas a ser impressa. Use pd.options.display.max_rows
print('Máximo de linhas', pd.options.display.max_rows)

# Para mudar a configuração da quantidade de linhas, atribua um valor ao que antes era usado como get.
pd.options.display.max_rows=20
dfLimited=pd.read_csv('C:\\apagar\\Mencoes2.csv')
print(dfLimited)
