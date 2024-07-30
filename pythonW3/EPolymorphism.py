'''
Faça um programa que abre a conta do novo cliente.
A classe-pai pergunta o nome e o número de telefone.
A diferença entre as classes-filhas é o valor do rendimento: se depositar a partir de 10 mil, o rendimento é 2% a.m. e se for um valor inferior, rende 1% a.m.
'''

class Cliente:
    def __init__(self, name, tel, dep):
        self.nome = name
        self.telefone = tel
        self.deposito = dep
    def calculaRendimento(self):
        pass

class Vip(Cliente):
    def calculaRendimento(self):
        if self.deposito >= 10000:
            return self.deposito*(1+0.02)
        else:
            return "Este valor de depósito é na categoria Comum."

class Comum(Cliente):
    def calculaRendimento(self):
        if self.deposito < 10000:
            return self.deposito*(1+0.01)
        else:
            return 'Este depósito pode ser feito na categoria VIP.'

objVip = Vip('Tuberaldo', '(19)123456789', 12000)
print(f'{objVip.nome:<15} {objVip.telefone:<15} {objVip.calculaRendimento()}')
objVip = Vip('Fulanildo', '(21)234567890', 2000)
print(f'{objVip.nome:<15} {objVip.telefone:<15} {objVip.calculaRendimento()}')
objComum = Comum('Fulano','(31)345678901', 2000)
print(f'{objComum.nome:<15} {objComum.telefone:<15} {objComum.calculaRendimento()}')
objComum = Comum('Beltrano', '(11)456789012', 12000)
print(f'{objComum.nome:<15} {objComum.telefone:<15} {objComum.calculaRendimento()}')