# Random Permutations → A forma como os elementos são dispostos. Há 2 métodos:
# 1. shuffle
# 2. permutation

# Shuffling Arrays
from numpy import random
import numpy as np
array1 = np.array([1,2,3,4,5])
print('shuffle')
random.shuffle(array1)
print(array1)
# IMPORTANTE: o método shuffle modifica o array original.

# Praticando: apresente 3 arrays com os mesmos elementos em ordens aleatórias
print('3 array com os mesmos elementos em ordens distintas')
for i in range(3):
    array2 = np.array([1,3,4,6,8,9])
    random.shuffle(array2)
    print(array2)

# Generating Permutation of Arrays
print('permutation')
array3 = np.array([1,2,3,4,5])
array3Perm = random.permutation(array3)
print(array3Perm)
# O método permutation mantém o original. permutation() retorna um novo array.