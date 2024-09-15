import random

enabled=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
sorteio=[]
counter=0
max=36

while (counter <= max):
    raffle=random.randint(0,len(enabled))
    if raffle not in sorteio:
        sorteio.append(enabled[raffle])
        counter+=1

for i in range(len(sorteio)):
    print(sorteio[i], end=' ')