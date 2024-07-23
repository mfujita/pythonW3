languages=["Python","C#","javascript","PHP","Shell Script","C"]
print(languages)
languages[5]="PySimpleGUI"
print(languages)

frutas=["caqui","goiaba","banana","pokan","figo","maçã"]
print(frutas)
frutas[1:4]=["morango","melancia"] # Adição nos índices 1, 2 e 3 e são 2 elementos
print(frutas)
print('Se o intervalo for maior que a quantidade de elementos a ser substituídos, os valores serão apagados.')

frutas[1:2]=["pêra","abacaxi"] # Adição no índice 1 e são 2 elementos
print(frutas)
print('Se o intervalo for menor que a quantidade de elementos a ser substituídos, mais valores serão adicionados.')

print('A função insert() precisa de 2 argumentos: a posição e o elemento a ser inserido.')
carro=["Uno","Gol","Fox"]
carro.insert(1,"Mobi")
print(carro)