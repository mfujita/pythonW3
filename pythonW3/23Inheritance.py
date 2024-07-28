# Inheritance → define que uma classe herde todos os métodos e propriedades de outra classe.
# Classe-pai ou classe base
# Classe-filha ou classe derivada.

class Pessoa:
    def __init__(self, pn, sn):
        self.primeiroNome = pn
        self.sobrenome = sn
    def imprimir(self):
        print(self.primeiroNome + " " + self.sobrenome)

objPessoa = Pessoa('Zé','Buscapé')
objPessoa.imprimir()

# Para a criação da classe-filha, envie o nome da classe-pai como parâmetro
class Estudante(Pessoa):
    pass

objEstudante = Estudante('Salvador','Dali Daesquina')
objEstudante.imprimir()

class Aluno(Pessoa):
    def __init__(self, fn, ln):
        self.firstname = fn
        self.lastname = ln
    def escreve(self):
        print(self.firstname + " " + self.lastname)

objAluno = Aluno('Tom','Seleck')
objAluno.escreve()

# Para manter o __init__() da classe-pai, explicite a chamada do __init__() da classe-pai:
class Matriculado:
    def __init__(self, primeiro, ultimo):
        Pessoa.__init__(self, primeiro, ultimo)

# super() → a classe-filha chama os métodos da classe-pai
# super() não precisa do parâmetro self
class Aprendiz(Pessoa):
    def __init__(self, pn, sn):
        super().__init__(pn, sn)

# Add Properties
class Aprendiz(Pessoa):
    def __init__(self, pn, sn):
        super().__init__(pn, sn)
        self.anoGraduacao = 2025
    def imprimeAnoGraduacao(self):
        print(self.anoGraduacao)

objAprendiz = Aprendiz('Fiote','Piador')
objAprendiz.imprimeAnoGraduacao()

class JovemEstudante(Pessoa):
    def __init__(self, pn, sn, ano):
        super().__init__(pn,sn)
        self.anoConclusao = ano
objJovemEstudante = JovemEstudante('Jeguenildo', 'Quaseburro', 2024)

# Add Methods
class NovoAluno(Pessoa):
    def __init__(self, pn, sn, ano):
        super().__init__(pn, sn)
        self.anoConclusao = ano
    def imprimir(self):
        print(self.primeiroNome + " " + self.sobrenome + " forma-se em " + str(self.anoConclusao))

objNovoAluno = NovoAluno('Tobias','Semfala', 2024)
objNovoAluno.imprimir()