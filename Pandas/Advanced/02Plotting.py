# Plotting
# Pandas usa o método plot() para criar diagramas.
# Usa-se Pyplot, um submódulo da biblioteca Matplotlib para visualizar o diagrama na tela.

# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv('data.csv')
# df.plot()
# plt.show()

# kind é o argumento para especificar o plot a ser exibido. Tem scatter, hist.
# Scatter precisa um eixo X e Y. Por exemplo, entre as opções Duration, Pulse, Maxpulse e Calories, serão usados para cada eixo:
# X → Duration
# Y → Calories
'''
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
df.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df["Duration"].plot(kind = 'hist')
plt.show()