# Seaborn Module → é uma biblioteca que usa Matplotlib para plotar gráficos. É usada para visualizar distribuições aleatórias.
# pip install seaborn
# Installing collected packages: pyparsing, pillow, kiwisolver, fonttools, cycler, contourpy, matplotlib, seaborn

# Distplots → disgnifica distribution plot. Recebe um arry como entrada e plota uma curva correspondente à distribuição dos pontos no array.
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0,1,2,3,4,5])  # Visualização diferente. Investigar futuramente!
plt.show()

# Plotting a Distplot Without the Histogram
'''
sns.displot([0,1,2,3,4,5], hist=False)
plt.show()
'''