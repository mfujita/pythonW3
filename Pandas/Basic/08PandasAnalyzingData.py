# Pandas - Analyzing Data
# Um dos métodos mais usados para visualizar rapidamente de um DataFrame é usar o método head().
# head() retorna o cabeçalho e um número específico de linhas iniciando da parte superior (topo).
import pandas as pd
df=pd.read_csv('C:\\github\\Pandas\\Basic\\data.csv')
print(df.head(7)) # Como mostra as 7 primeiras linhas, os índices variam de 0 a 6
# Por padrão o head() mostra 5 linhas

print('head  padrão')
print(df.head())

# tail() exibe as últimas linhas do DataFrame. O padrão é 5.
print('tail()')
print(df.tail())

# Info About the Data
# Use o método info() para obter informações sobre o data set.
print('info()')
print(df.info())