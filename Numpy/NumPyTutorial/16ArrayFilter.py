# Array Filter → Os índices recebem True ou False. Os que recebem True farão parte do array Filter.
import numpy as np
array1=np.array([15, 14, 18, 16])
boolIndex = [True, False, True, False]
array1Filtered=array1[boolIndex]
print(array1Filtered) # [15 18]

# Creating the Filter Array
arrayNumbers = np.array([2, 5, 3, 7, 6])
conditions = []
for item in arrayNumbers:
    if item > 5:
        conditions.append(True)
    else:
        conditions.append(False)

arrayNumbersFiltered = arrayNumbers[conditions]
print('Valores filtrados ', arrayNumbersFiltered)

# FIltrando os valores pares
numbers = np.array([0,1,2,3,4,5,6,7,8,9])
check = []
for item in numbers:
    if item%2 == 0:
        check.append(True)
    else:
        check.append(False)

evenNumbers = numbers[check]
print('Pares: ', evenNumbers)

# Creating Filter Directly From Array
filtradospares = numbers %2==0
print('Filtragem direta ', numbers[filtradospares])


# Exercício. Seja a lista com nomes e nota. Imprime os nomes daqueles que a nota é superior ou igual a 5.5
nomes=np.array(['Zé', 'Cida', 'Ana', 'Tonho', 'Bia', 'Maria'])
notas=np.array([7.5, 4.7, 6.3, 3.5, 5.4, 8.1])
notasParaAprovar = notas > 5.5
print('Alunos aprovados')
print(nomes[notasParaAprovar])