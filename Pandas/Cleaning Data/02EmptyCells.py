# Empty Cells
# Remove Rows → uma das formas de lidar com células vazias é remover linhas que contém células vazias.
# Remover algumas linhas que contém células vazias quando os data sets têm grandes volumes não impactam o resultado. 
import pandas as pd
df = pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\data.csv')
newDF=df.dropna() # Remove as linhas vazias
print(newDF.to_string()) # Não imprimiu as linhas 18, 22 e 28
# dropna() retorna um novo DataFrame conservando o original

# Para mudar o DataFrame original, use inplace = True
dfOriginal=pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\data.csv')
dfOriginal.dropna(inplace=True)
print('DataFrame original')
print(dfOriginal.to_string())

# Replace Empty Values
# Uma outra forma de lidar com células vazias é inserindo um novo valor.
# O método fillna() subustitui células vazias por um novo valor.

df=pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\data.csv')
df.fillna(130,inplace=True)
print(df.to_string())

# Replace Only For Specified Columns
# Para subsituir valores em um uma coluna, específique o nome da coluna
# O exemplo a seguir substitiu o alor nulo na coluna Calories por 130
df = pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\data.csv')
df["Calories"].fillna(130, inplace=True)
print(df.to_string())

'''
For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
'''

# Replace Using Mean, Median, or Mode
# Uma forma comum de subtituir valores de células vazias é calcular a média, a mediana ou a moda.
# Pandas usa mean(), median() e mode().
#  Neste exercício substitua as células vazias pela média

df=pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\data.csv')
media=df['Calories'].mean()
df['Calories'].fillna(media, inplace=True)
print(df.to_string())

# Substitua as células vazias pela mediana
df=pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\data.csv')
mediana=df['Calories'].median()
df['Calories'].fillna(mediana, inplace=True)
print(df.to_string())

# Substitua as células vazias pela moda
df=pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\data.csv')
moda=df['Calories'].mode()[0] # Pode ter mais de uma moda. Neste exemplo foi pega a 1ª moda.
df['Calories'].fillna(moda, inplace=True)
print(df.to_string())