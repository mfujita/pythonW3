'''
Faça um programa que simule o funcionamento de um banco. Inicie com saldo zero, faça depósitos e saques.
Registe em uma lista a data, a descrição e o valor movimentado.
'''

class Banco:
    registroData = []
    registroDescricao = []
    registroValor = []
    saldo = 0
    def __init__(self, dt, desc, val):
        self.data = dt
        self.descricao = desc
        self.valor = val
    def depositar(self):
        self.registroData.append(self.data)
        self.registroDescricao.append(self.descricao)
        self.registroValor.append(self.valor)
    def sacar(self):
        self.registroData.append(self.data)
        self.registroDescricao.append(self.descricao)
        self.registroValor.append(-self.valor)
    def emitirExtrato(self):
        for i in range(len(self.registroData)):
            print(f'{self.registroData[i]}  {self.registroDescricao[i]:<28} {self.registroValor[i]:>5}')
    def exibirSaldo(self):
        for i in range(len(self.registroValor)):
            self.saldo += self.registroValor[i]
        print(f'Saldo atual: R$ {self.saldo}')

cliente = Banco('01/07/2024', 'Venda cliente 10', 120)
cliente.depositar()
cliente = Banco('02/07/2024', 'Venda cliente 4', 80)
cliente.depositar()
cliente = Banco('03/07/2024', 'Venda cliente 8', 40)
cliente.depositar()
cliente = Banco('05/07/2024', 'Venda cliente 2', 180)
cliente.depositar()
cliente = Banco('07/07/2024', 'Venda cliente 1', 70)
cliente.depositar()
cliente = Banco('09/07/2024', 'Aluguel', 400)
cliente.sacar()
cliente = Banco('11/07/2024', 'Pagamento promissória', 250)
cliente.depositar()
cliente = Banco('16/07/2024', 'Conserto balcão', 110)
cliente.sacar()
cliente.emitirExtrato()
cliente.exibirSaldo()