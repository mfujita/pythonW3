# Pandas Getting Started
# pip install pandas

# Import Pandas
import pandas

paiFilhos = {
    'nomes': ['Murilo','Enzo','Hugo'],
    'dias' : [13, 7, 12]
}

mydf=pandas.DataFrame(paiFilhos)
print(mydf)
'''
    nomes  dias
0  Murilo    13
1    Enzo     7
2    Hugo    12
'''
print('tipo: ', type(mydf))

# Pandas as pd
# import pandas as pd

# Checking Pandas Version
import pandas as pd

print(pd.__version__) # 2.2.2