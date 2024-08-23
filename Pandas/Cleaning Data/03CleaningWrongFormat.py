# Cleaning Data of Wrong Format
# As 2 opções para tratar células com formato de data errado:
# 1. Remover a linha
# 2. Converter todas as células de uma coluna em um mesmo formato.

# Convert Into a Correct Format
import pandas as pd
df = pd.read_csv('C:\\github\\Pandas\\Cleaning Data\\wrongDate.csv')
df['Date'] = pd.to_datetime(df['Date']) # Exception has occurred: KeyError
print(df.to_string()) # Linha 22
# 22        45        NaT    100       119     282.0
# NaT → Not a Time
# Porém só funcionou depois que o formato errado (linha 26) foi eliminado.

# Removing Rows
# df.dropna(subset=['Date'], inplace=True)
# print(df.to_string()) # Linha 22 removida igual ao site W3Schools
# Linha 26 W3Schools:
# 26        60 2020-12-26    100       120     250.0

# Linha 26 deste programa
# 26        60      20201226    100       120     250.0