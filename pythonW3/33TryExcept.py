# Try Except
# try → Testa um bloco de códigos
# except → manipula o erro
# else → executa o código quando não há erro
# finally → executa o código independente se existe erro

# Manipulando a exceção
try:
    print(x) # x was not defined
except:
    print('An error occured')

# Muitos erros → pode-se criar um bloco específico para um erro
try:
    print(x)
except NameError:
    print('A variável não foi definida') # Este erro foi impresso.
except:
    print('Algo deu errado.')

# else → a instrução é executada quando não acontece qualquer erro
try:
    print("hello world")
except:
    print('Algo deu errado no código')
else:
    print('Esta mensagem será impressa por não ter qualquer erro')

# Finally → executa o bloco independente se tem erro ou não
try:
    print(x)
except:
    print('Este é o bloco except')
finally:
    print('Este é o bloco finally')

# Usado para fechar um objeto e limpar os recursos
try:
    f = open('myfile.txt')
    try:
        f.write('Lorem Ipsum')
    except:
        print('Falha ao escrever no arquivo')
    finally:
        f.close()
except:
    print('Aconteceu um problema com o arquivo')

# Raise an exception
# a palavra reservada raise lança uma exceção
# este programa lança uma exceção e interrompe o funcionamento se x é menor que 0
# Atenção: o programa para de funcionar, mas aparece a tela desagradável de erro

'''
x = -1
if x < 0:
    raise Exception('--->  o valor não pode menor que 0')
'''

# este programa lança uma exceção se a variável não guarda um inteiro. O programa mostra a tela desagradável de erro
'''
valor = 'python'
if not type(valor) is int:
    raise TypeError('Não é um inteiro!')
'''

