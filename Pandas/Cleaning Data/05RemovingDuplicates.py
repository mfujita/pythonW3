# Removing Duplicates
# O método duplicate() para localizar os registros duplicados.
# Este método retorna booleanos para cada linha.
import pandas as pd
df=pd.read_csv('wrongDate.csv')
print(df.duplicated())

# Removing Duplicates
# Use o método drop_duplicates()
df.drop_duplicates(inplace=True)
print('df.drop_duplicates(inplace=True)')
print(df.to_string())