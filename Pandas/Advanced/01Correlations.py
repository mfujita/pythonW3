# Correlations
# Finding Relationships → método corr().
# corr() ignora dados não numéricos.
import pandas as pd
print('mostre as correlações:')
df=pd.read_csv('data.csv')
print(df.corr())
'''
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922717
Pulse    -0.155408  1.000000  0.786535  0.025121
Maxpulse  0.009403  0.786535  1.000000  0.203813
Calories  0.922717  0.025121  0.203813  1.000000
'''

# Result Explained → uma tabela que mostra a relação entre 2 colunas.
'''
Os números variam entre -1 e 1.
1 → relação perfeita.
Para esse conjunto de dados, cada vez que um valor subia na primeira coluna, a outra também subia.
0.9 é também uma boa relação e se você aumenta um valor, o o outro também aumenta.
-0.9 é uma boa relação como 0,9, mas se aumentar um valor o outro provavelmente diminuirá.
0,2 não é uma boa relação significando que se um dos valores aumentar não implica que o outro também aumenta.

O que é uma boa correlação? Depende do uso, mas não pense que é seguro dizer que você tem pleo menso 0,6 (ou -0,6) para dizer que é uma boa correlação.
'''

# Perfect Correlation:
# Relacionando a coluna "Duration" com "Duration" obtemos o número 1.0000 que é uma correlção perfeita.

# Boa relação
# A relação entre as colunas "Duration" e "Calories" é uma relação mito boa prevendo que quanto mais você se exercita, mais calories são queimadas. Da mesma forma se você queimar mais calorias, provavelmente fez exercícios por mais tempo.

# Bad Correlation:
'''
Duração e Maxpulse tem uma correlação ruim, o que significa que não se pode prever o maxpulse apenas olhando a duração do exercício e vice-versa.
'''