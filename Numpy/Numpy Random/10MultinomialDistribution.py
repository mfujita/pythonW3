# Multinomial Distribution → é a generalização da distribuição binomial.
# Descreve resultados de cenários multi-nomial diferente dos binomais onde cenários devem ser apenas um de dois.
# Por exemplo, tipo sanguíneo da população, lançamento de dado.
# 3 parâmetros:
# n → número de resultados possíveis (são 6 para um lançamento de dados)
# pvals → lista de possibilidades dos resultados (por exemplo [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] para o lançamento de dados)
# size → o shape do array retornado

# Faça uma amostra para o lançamento de dados
from numpy import random
array1=random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(array1)

'''
Nota 1: Amostras multimodais não produzirão um único valor. Eles produzem um valor para cada pval.
Nota 2: Por serem generalizações da distribuição binomial, suas representações visuais e similaridade de uma distribuição normal é a mesma como as distribuições binomiais múltiplas.
'''