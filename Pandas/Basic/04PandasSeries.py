# Pandas Series
# What is a Series?
# Um Panda Series é como um uma coluna de uma tabela.
# é um array 1D com dados de de qualquer tipo.
import pandas as pd
coluna=[3,5,8,6,3]
myCol=pd.Series(coluna)
print(myCol) # 
'''
0    3
1    5
2    8
3    6
4    3
dtype: int64
'''

# Labels
# Se nada for especificado, os valores são identificados com seus índices. Primeiro → 0, segundo → 1 e assim por diante.
# Imprima o primeiro valor da série:
print('Primeiro valor', myCol[0])

# Create Labels
dias=[13,7,12]
mydf=pd.Series(dias, index=['Murilo','Enzo','Hugo'])
print(mydf)
'''
Murilo    13
Enzo       7
Hugo      12
dtype: int64
'''

# Quando os labels estão associados, você pode acessar um item através do label.
print(mydf['Murilo']) # 13

# Key/Value Objects as Series → ideia de um dicionário
distancias={'dia 1': 132, 'dia 2': 78, 'dia 3': 84, 'dia 4':93, 'dia 5':110}
distanciasDF=pd.Series(distancias)
print(distanciasDF)
'''
dia 1    132
dia 2     78
dia 3     84
dia 4     93
dia 5    110
dtype: int64
# As chaves do dicionário tornam-se labels.
'''

# Para selecionar alguns itens no dicionário use index e especifique apenas os itens serem incluídos na série.
# Exemplo: selecionando os itens 'dia 1' e 'dia 5' da série distanciasDF:
someDistances = pd.Series(distanciasDF, index=['dia 1', 'dia 5'])
print(someDistances)
'''
dia 1    132
dia 5    110
dtype: int64
'''

# DataFrames
# Data sets em Pandas são geralmente tabelas multidimensionais chamadas de DataFrames.
# Series é como uma coluna e dataFrames é a tabela inteira.
gastos = {
    'diasSemana' : ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'gastos' : [30, 25, 27, 22, 44]
}

gastosDF=pd.DataFrame(gastos)
print(gastosDF)
'''
  diasSemana  gastos
0    Segunda      30
1      Terça      25
2     Quarta      27
3     Quinta      22
4      Sexta      44
'''