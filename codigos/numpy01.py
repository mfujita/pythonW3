# numpy-ref-1.14.0.pdf

import numpy as np
x=np.array([[1,2,3],[4,5,6]])
y=x
y[0,1]=11
print(x.T)
print('shape: ', y.shape)
print('dtype: ', y.dtype)
print('data', y.data)
print('flags', y.flags)
print('flat', y.flat)
print('imag', y.imag)
print('real', y.real)
print('size', y.size)
print('itemsize', y.itemsize)
print('nbytes', y.nbytes)
print('ndim', y.ndim)
print('strides', y.strides)
print('ctypes', y.ctypes)
print('base', y.base)
# x=np.empty((2,3))
# print(x)
# print('C')
# x=np.zeros((2,3), order='C')
# print(x)
# print('Fortran')
# x=np.zeros((2,3), order='F')
# print(x)

x.flat=3
print(x)
y=np.array([[-2,-1,0],[1,2,-1],[0,1,-2]])
# print(y)
# y.flat=0
# print(y)
# print('np.prod(y.shape)',np.prod(y.shape), ' size ', y.size)
for i in range(y.shape[0]):
    for j in range(y.shape[1]):
        print(y[i][j], end=' ')
print('\nnp.reshape(np.arange(2*3*4),(2,3,4))')
y=np.reshape(np.arange(2*3*4),(2,3,4))
print(y)
z=x[2:]
print('x.base is None → ',x.base is None,' z.base is x → ', z.base is x)

