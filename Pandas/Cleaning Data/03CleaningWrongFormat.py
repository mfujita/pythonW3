# Cleaning Data of Wrong Format
# As 2 opções para tratar células com formato de data errado:
# 1. Remover a linha
# 2. Converter todas as células de uma coluna em um mesmo formato.

# Convert Into a Correct Format
import pandas as pd
df = pd.read_csv('wrongDate.csv')
df['Data'] = pd.to_datetime(df['Data']) # Exception has occurred: KeyError
print(df.to_string())