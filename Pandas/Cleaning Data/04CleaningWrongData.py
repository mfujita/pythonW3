# Cleaning Wrong Data
# Um dado errado não limita a uma célula vazia ou formato errado, mas também um valor discrepante como 199 no lugar de 1.99.

# Replacing Values
import pandas as pd
df=pd.read_csv('wrongDate.csv')
df.loc[7,'Duration']=45
print(df.to_string())

# Para DataFrames pequenos pode-se substituir os poucos elementos com problemas um a um, mas torna-se difícil quando o volume é expressiva.
# Para estes casos pode-se criar regras para valores fora do limite.

print('Aplicação da regra:')
df=pd.read_csv('wrongDate.csv') # Leitura do CSV novamente para pegar sem as alterações anteriores
for duracao in df.index:
    if df.loc[duracao, 'Duration'] > 120:
        df.loc[duracao, 'Duration'] = 120
print(df.to_string())

# Removing Rows → também é possível remover as linhas com problemas.
# Apagando as linhas que a duração é maior do que 12
print('DF com linhas removidas quando a duração é maior que 120')
df=pd.read_csv('wrongDate.csv')
for tempo in df.index:
    if df.loc[tempo, 'Duration'] > 120:
        df.drop(tempo, inplace=True)
print(df.to_string())
