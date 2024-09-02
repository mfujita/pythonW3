# Line
# O argumento linestyle ou a abreviação ls afeta o estilo da linha.
# import matplotlib.pyplot as plt
# import numpy as np
# Y=np.array([3,8,1,10])
# # plt.plot(Y, linestyle='dotted')
# plt.plot(Y, linestyle='dashed')
# plt.show()

# Shorter Syntax
'''
linestyle → ls
dotted → :
dashed → --
'''

# Line Styles
'''
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or ' '
'''

# Line Color
# import matplotlib.pyplot as plt
# import numpy as np
# Y=np.array([3,8,1,10])
# plt.plot(Y, color = 'r')
# plt.show()

# A cor pode ser substituída pelo código de cores HTML.
# 140 nomes https://www.w3schools.com/colors/colors_names.asp

# Line Width
# O argumento linewidth ou a abreviação lw modifica a espessura da linha
# O valor é do tipo float dado em points.
# import matplotlib.pyplot as plt
# import numpy as np
# Y=np.array([3,8,1,10])
# plt.plot(Y, linewidth='8.5')
# plt.show()

# Multiple Lines
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()