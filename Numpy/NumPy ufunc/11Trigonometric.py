# Trigonometric
import numpy as np
senPiOver2=np.sin(np.pi/2)
print(senPiOver2) # 1.0

# Calcule o valor dos elementos em um array
array1=np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print('Cálculo do seno dos elementos do array')
senos=np.sin(array1)
print(senos) # [1.         0.8660254  0.70710678 0.58778525]

# Convert Degrees Into Radians → pi/180*graus
# deg2rad(array)
array2=np.array([90, 180, 270, 360])
convertDeg2rad=np.deg2rad(array2)
print('Deg2rad')
print(convertDeg2rad) # [1.57079633 3.14159265 4.71238898 6.28318531]

# Radians to Degrees
array3=np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
arrayrad2deg=np.rad2deg(array3)
print('rad 2 deg')
print(arrayrad2deg) # [ 90. 180. 270. 360.

# Finding Angles → arcsin(), arccos(), arctan()
radianos=np.arcsin(1.0)
print(radianos) # 1.5707963267948966
print(np.rad2deg(radianos)) # 90.0

# Angles of Each Value in Arrays
array4=np.array([1, -1, 0.1])
arrRadianos=np.arcsin(array4)
arrGraus=np.rad2deg(arrRadianos)
print('arrRadianos', arrRadianos) # [ 1.57079633 -1.57079633  0.10016742]
print('arrGraus', arrGraus) # [ 90.         -90.           5.73917048]

# Hypotenues → hypot()
base=3
perp=4
hipotenusa=np.hypot(base, perp)
print('hipotenusa', hipotenusa)