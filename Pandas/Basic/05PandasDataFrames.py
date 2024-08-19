# Pandas DataFrames
# What is a DataFrame?
# É uma estrutura 2D como uma matriz ou uma tabela composta de linhas e colunas

# Create a simple Pandas DataFrame:
import pandas as pd
dados = {
    "calorias" : [420, 380, 390],
    "duração" : [50,40,35]
}

# carregue as informações em um objeto dataFrame
df=pd.DataFrame(dados)
print(df)
'''
   calorias  duração
0       420       50
1       380       40
2       390       35
'''

# Locate Row → atributo loc retorna uma ou mais linhas específicas.
print('Imprime a primeira linha do DataFrame df. Retorna um Pada Series')
print(df.loc[0])
'''
calorias    420
duração      50
Name: 0, dtype: int64
'''

# Retornar as linhas com índices 0 e 1. Pelo fato de  usar [[]] o resultado é um Padas DataFrame.
print('Retornar as linhas com índices 0 e 1')
print(df.loc[[0,1]])
'''
   calorias  duração
0       420       50
1       380       40
'''

# Named Indexes → com o argumento index pode-se nomear seus próprios índices.
workout = {
    "calorias" : [400,500,450],
    "duração" : [40, 50, 45]
}
dfw=pd.DataFrame(workout,index=['dia 1', 'dia 2', 'dia 3'])
print(dfw)
'''
       calorias  duração
dia 1       400       40
dia 2       500       50
dia 3       450       45
'''
# Locate Named Indexes → combine loc com o nome atribuído à "chave"
print('combinação de loc com o nome do índice')
print(dfw.loc['dia 2'])
'''
calorias    500
duração      50
Name: dia 2, dtype: int64
'''

# Load Files Into a DataFrame → se os dados estão armazenados em um arquivo, Padas pode carregá-los em um DataFrame.
dffile=pd.read_csv('C:\\apagar\\Mencoes2.csv')
print('DataFrame carregado de um arquivo CSV')
print(dffile)