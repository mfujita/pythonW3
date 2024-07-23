valores=["zero","um","dois","tres","quatro","cinco"]
print(valores[3])
print(valores[-3])
print('Quando dois índices são usados para determinar um intervalo, o limite inferior está incluso e o limite superior está excluso.')
print(valores[1:4])
print('Use a palavra reservada "in" para indicar se tal elemento está contido ou não em uma lista.')

if "cinco" in valores:
    print("Este elemento está presente.")
else:
    print("Este elemento NÃO está presente.")
    
if "dez" in valores:
    print("Este elemento está presente.")
else:
    print("Este elemento NÃO está presente.")