import random

def cria_letras():
    letras=[]
    aleatorio=[]
    i=65
    contador=0
    while (i<65+26):
        letras.append(chr(i))
        i+=1
    while contador < (len(letras)):
        indice = random.randint(0, len(letras)-1)
        if letras[indice] not in aleatorio:
            aleatorio.append(letras[indice])
            contador+=1
    for item in aleatorio:
        print(item, end=' ')

def cria_silabas():
    consoantes=['b', 'c', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'x', 'z']
    vogais=['a','e','i','o','u']
    silabas = []
    contador=0
    while contador < 31:
        indCon = random.randint(0,len(consoantes)-1)
        indVog = random.randint(0,len(vogais)-1)
        novaSibala = consoantes[indCon]+vogais[indVog]
        if novaSibala == 'ce' or  novaSibala == 'ci' or novaSibala == 'ge' or novaSibala == 'gi':
            pass
        if novaSibala not in silabas:
            silabas.append(novaSibala)
            contador+=1
    for item in silabas:
        print(item, end=' ')

cria_silabas()