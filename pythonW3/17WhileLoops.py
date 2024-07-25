# While
i=1
while i < 6:
    print(i)
    i+=1

# break encerra sua execução incluindo o valor que critério de parada.
print('break')
contador=1
while contador < 9:
    print(contador)
    if contador == 4: # O 4 é incluído
        break
    contador+=1

# continue Executa toda as condições do laço de repetição pulando a condição verdadeira
print('continue')
indice = 0
while indice < 5:
    indice+=1 # o incremento deve acontecer logo após a instrução While
    if indice == 3: # este valor não é impresso
        continue
    print(indice)

# The else Statement → a partir do momento que a condição não é mais verdadeira, outro bloco é executado
contagem=1
while i < 6:
    print(i)
    i+=1
else: # else combinado com while
    print('A partir daqui os valores são maiores do que 5')
    


