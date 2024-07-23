def mensagem():
    return False

if mensagem():
    print('Retornou True')
else:
    print('retornou False')
    

n1=10
print(isinstance(n1,int))
n2=3.14
print(isinstance(n2,float))
n3=("n1","n2","n3")
print(isinstance(n3,tuple))
n4=["n1","n2","n3"]
print(isinstance(n4,list))
n5={"nome": "Murilo", "profissão" : "programador"}
print(isinstance(n5,dict))