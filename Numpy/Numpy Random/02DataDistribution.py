# Data Distribution → é uma lista de todos os valores possível e sua respectiva frequência.
# Random Distribution → é um conjunto de instruções dos números aleatóriocs que seguem uma certa funçãp de densidade de probabilidade.
# Função de densidade de probabilidade → uma função que descreve uma probabilidade contínua, por exemplo, a probaabilidade de todos os valores em uma array.
# Os números aleatórios podem ser baseados nas probabilidades definidas usando o método choice() do módulo random.
# O método choice() permite especificar a probabilidade de cada valor.
# A probabilidade é um conjunto de números entre 0 e 1 onde 0 significa que o valor nunca acontece e 1 significa que sempre ocorre.

# Gere um array1D contendo 100 valores contendo os valores 3, 5, 7 ou 9 de acordo com a seguinte tabela:
'''
Valor Probabilidade
3     0.1
5     0.3
7     0.6
9     0.0
Total 1.0
'''
# A soma das probabilidades deve ser 1
from numpy import random
array1= random.choice([3,5,7,9], p=[0.1, 0.3, 0.6, 0.0], size=100)
print(array1)
'''
[5 7 5 7 5 5 5 7 5 7 7 5 5 5 7 5 5 7 3 5 7 7 7 7 3 7 7 5 7 5 7 5 7 7 5 3 7
 7 5 7 7 5 7 7 3 7 5 7 3 7 5 7 7 5 3 7 5 5 3 7 7 5 3 7 7 5 7 7 5 7 7 7 7 7
 7 7 7 5 7 7 3 5 5 7 5 7 3 7 7 7 3 5 7 5 7 5 7 5 5 7]
'''
# Gere um array2D com 3 linhas e 5 colunas

array2 = random.choice([3,5,7,9], p=[0.1, 0.3, 0.6, 0.0], size=(3,5))
print('Gere um array2D com 3 linhas e 5 colunas')
print(array2)
'''
[[5 7 5 5 5]
 [5 5 7 7 7]
 [7 3 3 7 7]]
'''