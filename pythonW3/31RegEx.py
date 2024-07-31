# RegEx
import re
texto = "O rato roeu a roma do rei de Roma"
checa = re.search("^O.*Roma$", texto)
print(checa)

if checa:
    print("The pattern was found")
else:
    print('No match')

'''
findall  Retorna a lista de todas as correspondências
search   Retorna o objeto Match desde que haja correspondência na string
split    Retorna a lista onde a string foi fatiada em cada correspondência
sub      Substitui uma ou mais correspondências com uma string
'''
# Metacaracteres
'''
[] um conjunto de caracteres
\  sinal de escape
.  qualquer caracter
^  inicia com
$  Termina com
*  0 ou mais ocorrências
+  1 ou mais ocorrências
?  0 ou 1 ocorrência
{} exatamente o número de ocorrências
|  Um dos valores
() capturar e agrupar 
'''

# Sequências especiais
'''
\A Retorna uma correspondência se os caracteres específicos estão no início da string
\b Retorna uma correspondência se os caracteres específicos estão no final da string
\B Retorna uma correspondência onde os caracteres estão presentes, mas não no início e nem no fim da palavra
\d Retorna uma correspondência que contenha números de 0 a 9
\D Retorna uma correspondência que não contenha números
\s Retorna uma correspondência que contenha um espaço em branco
\S Retorna uma correspondência que não contenha um espaço em branco
\w Retorna uma correspondência que tenha quaisquer caracteres de 'a' a 'Z', 0 a 9 e _
\W Retorna uma correspondência que não contenha qualquer caracter na palavra
\Z Retorna uma correspondência que caracteres específicos estejam no final da string
'''

# Sets
'''
[arn] Retorna a correspondência se os caracteres 'a', 'r' e 'n' estão presentes
[a-n] Retorna a correspondência para os caracteres entre a e n (todos minúsculos) abcdefghijklmn
[^arn] Retorna a correspondência para qualquer caracter EXCETO 'a','r' e 'n'
[0123] Retorna a correspondência se os dígitos 0, 1, 2 e 3 estão presentes
[0-9]  Retorna a correspondência para quaquer dígito entre 0 e 9
[0-5][0-9] Retorna a correspondência para qualquer número entre 00 e 59
[a-zA-Z] Retorna a correspondência para qualquer caracter entre 'a' e 'z' sendo maíuscula ou minúscula
[+] Retorna a correspondência para qualquer caracter '+'
'''

# findall() 
chuvaEspanha = 'The rain in Spain'
este = re.findall('ai', chuvaEspanha)
print(este)

acucares = "glicose, frutose, dextrose, sacarose, xarope glucose-frutose"
ose = re.findall('ose', acucares)
print(ose)

# search() → Procura por uma correspondência e sendo positivo, retorna o objeto Match.
declaration = 'This is my Python studies'
objSearch = re.search('\s', declaration)
print('A posição do primeiro espaço em branco é a de número: ', objSearch.start())

# split() → retorna a lista onde a string foi fatiada em cada correspondência.
phrase = 'Hear me now!'
objSplit = re.split('\s', phrase)
print(objSplit)

# someUppercase = 'This Text has words That starts with Uppercase and lowercase'
# objsomeUppercase = re.split('\s', someUppercase)
# for item in objsomeUppercase:
#     if re.Match()

# sub() → substitui a correspondência por um texto desejado
someUppercase = 'This Text has words That starts with Uppercase and lowercase'
replacedSpaces = re.sub(' ', '_', someUppercase)
print(replacedSpaces)

# Controlando a quantidade de substituições
myText = 'Study is a good tool to prepare to the future'
newReplace = re.sub(' ', '_', myText, 2)
print(newReplace)

# Match → é um objeto que contém informações sobre a busca e o resultado. Caso nada seja encontrada, retorna None
inicioDiscurso = 'senhoras e senhores'
objSenhor = re.search('senhor', inicioDiscurso)
print(objSenhor)
print(objSenhor.span()) # o início e o final das posições de cada match
print(objSenhor.string) # retorna as ocorrências encontradas
print(objSenhor.group()) # retorna uma PARTE da string onde há correspondência