# Markers → o argumento maker enfatiza cada ponto com um marcador específico:
# exemplo: marcador círculo
'''
import matplotlib.pyplot as plt
import numpy as np
Y=np.array([9,-8,7,-6,5,-4,3,-2,1,0])
plt.plot(Y, marker='s')
plt.show()
'''

'''
Mude o argumento de acordo com esta tabela para modificar o marker
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline 
'''

# Format Strings fmt → é um aparâmetro que especifica o marker.
# fmt é escrito com esta sitaxe: marker|line|color
'''
import matplotlib.pyplot as plt
import numpy as np
Y=np.array([3,8,1,10])
plt.plot(Y, '_-.k')
plt.show()
'''

'''
Line Reference
'-'	 Solid line	
':'	 Dotted line	
'--' Dashed line	
'-.' Dashed/dotted line
'''

'''
Color Reference
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
'''
# Marker Size
# O argumento makersize ou a forma abreviada ms configuram o tamanho dos markers
'''
import matplotlib.pyplot as plt
import numpy as np
Y=np.array([3,-8,1,-10])
plt.plot(Y, 'H-.m', ms=10)
plt.show()
'''

# Marker Color
# O argumento markeredgecolor ou a abreviatura mec configura a cor das bordas dos markers
import matplotlib.pyplot as plt
import numpy as np
Y=np.array([-9,8,-7,6,-5,4,-3,2,-1,0])
plt.plot(Y, 'o-r', ms=10, markeredgecolor= 'k')
plt.show()