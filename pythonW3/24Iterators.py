# Iterators → é um objeto que contem um número de valores contáveis.
# Métodos __iter__() e __next__()
frutas = ('banana','goiaba','ameixa')
myit = iter(frutas)
print(next(myit)) # banana
print(next(myit)) # goiaba
print(next(myit)) # ameixa

# um string pode ser um objeto iterable
nome = 'Murilo'
nome_it = iter(nome)

print(next(nome_it))
print(next(nome_it))
print(next(nome_it))
print(next(nome_it))
print(next(nome_it))
print(next(nome_it))

# Create an Iterator
class MeusNumeros:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
objMeusNumeros = MeusNumeros()
numeros_it = iter(objMeusNumeros)

print(next(numeros_it))
print(next(numeros_it))
print(next(numeros_it))
print(next(numeros_it))
print(next(numeros_it))

# StopIteration → previne o loop infinito
class NovosNumeros:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

objNovosNumeros = NovosNumeros()
novos_numeros_it = iter(objNovosNumeros)

for i in novos_numeros_it:
    print(str(i) + ' ', end=' ')
print()