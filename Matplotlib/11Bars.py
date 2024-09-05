# Bars → função bar()
# Exemplo: desenhar 4 barras
'''
import matplotlib.pyplot as plt
X=["Julho", "Agosto", "Setembro", "Outubro"]
Y=[10, 8.5, 7.3, 10.9]
plt.subplot(1,2,1)
plt.bar(X,Y)

x1 = ["APPLES", "BANANAS"]
y1 = [400, 350]
plt.subplot(1,2,2)
plt.bar(x1, y1)
plt.show()
'''

# Horizontal Bars
import matplotlib.pyplot as plt
'''
X=['A', 'B', 'C', 'D']
Y=[7,3,4,8]
plt.subplot(2,1,1)
plt.barh(X,Y)
X=['D', 'C', 'B', 'A']
Y=[8,4,3,7]
plt.subplot(2,1,2)
plt.barh(X,Y)
plt.show()
'''

# Bar Color → As funções bar() e barh() usam o argumento color para atribuir cor à barra.
'''
import matplotlib.pyplot as plt
X=['A','B', 'C', 'D']
Y=[-3, 5, -6, 2]
plt.bar(X,Y, color='red')
plt.grid(axis='y')
plt.show()
'''

# Bar Width → o argumento width configura a largura das barras. Usado na função bar()
import matplotlib.pyplot as plt
X=['Jan','Fev','Mar','Abr','Maio','Junho', 'Julho', 'Agosto']
Y=[4,7,2,1,8,6,3,5]
plt.bar(X,Y, width=0.1) 
plt.show()

# Para a função barh usa-se o argumento height