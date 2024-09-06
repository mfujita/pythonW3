# Histogram
'''
É um gráfico que mostra a distribuição de frequências mostrando o número de observações dentro de cada intervalo.
Por exemplo, ao perguntar a altura de 250 pessoas, pode-se exibir os dados com um histograma.
'''

# Create Histogram - função hist()
import matplotlib.pyplot as plt
import numpy as np
alturas = np.random.normal(170, 10, 250)
plt.hist(alturas)
plt.show()
