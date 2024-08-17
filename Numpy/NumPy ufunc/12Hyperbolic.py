# Hyperbolic → sinh(), cosh(), tang()
# Os valores são expressos em radianos 
import numpy as np
print(np.sinh(np.pi/2)) # 2.3012989023072947

array1=np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
arrCosh=np.cosh(array1)
print(arrCosh) # [2.50917848 1.60028686 1.32460909 1.20397209]

# Finding Angles
import numpy as np
radiano=np.arcsinh(1.0)
print('radiano',radiano) # 0.881373587019543
print('graus', np.deg2rad(radiano)) # 0.015382871033603782

# Angles of Each Value in Arrays
array2=np.array([0.1, 0.2, 0.5])
arrTaghRad=np.arctanh(array2)
print('arrTanh Radianos', arrTaghRad) # [0.10033535 0.20273255 0.54930614]
print('arrTanh graus', np.rad2deg(arrTaghRad)) # [ 5.74879196 11.61571972 31.47292373]