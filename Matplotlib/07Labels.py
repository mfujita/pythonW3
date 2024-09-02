# Labels and Title
# Create Labels for a Plot
# xlabel() e ylabel escrevem as descrições dos respectivos eixos.

# Create a Title for a Plot
# title() escreve um título para o plot.

# Set Font Properties for Title and Labels
# Use fontdict() para xlabel(), ylabel() e title() para configurar a fonte.

# Position the Title
# O parâmetro loc() da função title() posiciona o título.
# Valores: left, right e center. Center é o padrão.

import matplotlib.pyplot as plt
import math
X=[]
Y=[]
x=1
while x <=360*20:
    X.append(x)
    Y.append(5*math.sin(x*math.pi/180)/x)
    x+=1
plt.title("Amortecimento", loc='right', fontdict={'family':'Arial','color':'red', 'size':20})
plt.xlabel('Graus', fontdict={'family':'Arial','color':'green', 'size':14})
plt.ylabel('sen(x)/x', fontdict={'family':'Arial', 'color':'blue', 'size':14})
plt.plot(X,Y)
plt.show()