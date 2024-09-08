# Pie Charts
# Creating Pie Charts → função pie()
'''
import matplotlib.pyplot as plt
numeros=[16,8,4,2]
plt.pie(numeros)
plt.show()
'''

# O gráfico de pizza inicia no eixo X e é desenhado no sentido antihorário.
# O tamanho de cada wedge é calculado através da fórmual x/sum(x).

# Labels → para cada valor, um label descreve o wedge.
'''
import matplotlib.pyplot as plt
points = [16, 15, 22, 20, 30]
months = ["May", "June", "July", "August", "September"]
plt.pie(points, labels=months)
plt.show()
'''

# Start Angle → o ângulo inicial que o wegde é desenhado. O valor padrão é 0.
'''
import matplotlib.pyplot as plt
nomes = ['Murilo','Enzo','Hugo','Carro']
idades= [47,7,5,13]
plt.pie(idades,labels=nomes, startangle=90)
plt.show()
'''

# Explode → o parâmetro explode destaca o wedge usando números que são distância do centro do centro do gráfico.
'''
import matplotlib.pyplot as plt
valores=[10,5,8,15,40]
indicadores=['A', 'B', 'C', 'D', 'E']
explodido=[0, 0, 0, 0 , 0.2]
plt.pie(valores, labels=indicadores, explode=explodido)
plt.show()
'''

# Shadow → O argumento shadow = True cria uma sombra.
'''
import matplotlib.pyplot as plt
valores=[10,5,8,15,40]
indicadores=['A', 'B', 'C', 'D', 'E']
explodido=[0, 0, 0, 0 , 0.2]
plt.pie(valores, labels=indicadores, explode=explodido, shadow= True)
plt.show()
'''

# Colors → um array contendo as cores de mesmo tamanho que os outros arrays permite atribuir as cores respectivamente.
'''
import matplotlib.pyplot as plt
valores=[10,5,8,15,40]
indicadores=['A', 'B', 'C', 'D', 'E']
cores=['black', 'r', 'g', 'b', 'y']
plt.pie(valores, labels=indicadores, colors=cores, startangle=180)
plt.show()
'''

# Legend → Adicione uma legenda para cada wegde do gráfico de pizza com a função legend()
'''
import matplotlib.pyplot as plt
valores=[10,5,8,15,30]
indicadores=['Mercado', 'Financiamento', 'Condomínio', 'Combustível', 'Educação']
plt.pie(valores, labels=indicadores)
plt.legend()
plt.show()
'''

# Legend With Header → use o parâmetro title na função legend()
import matplotlib.pyplot as plt
valores=[10,5,8,15,30]
indicadores=['Mercado', 'Financiamento', 'Condomínio', 'Combustível', 'Educação']
plt.pie(valores, labels=indicadores)
plt.legend(title='Despesas')
plt.show()