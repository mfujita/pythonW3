import random

def entrada_saida():
    for i in range(30):
        print("<tr><td>" + str(random.randint(7,10))+":"+str(random.randint(0,60)).zfill(2) + "</td><td>" +  
                        str(random.randint(10,12))+":"+str(random.randint(46,60)).zfill(2) +"</td><td>" +
                        str(random.randint(13,15))+":"+str(random.randint(0,60)).zfill(2) + "</td><td>" +
                        str(random.randint(17,19))+":"+(str(random.randint(0,60)).zfill(2)) + "</td></tr>")
        
def imprime_precos():
    for i in range(50):
        print("<tr><td>"+ str(random.randint(3,23))+","+str(random.randint(0,100)).zfill(2) +"</td></tr>")
        
#entrada_saida()
imprime_precos()