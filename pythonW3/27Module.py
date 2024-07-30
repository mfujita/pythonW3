# Module → Funciona como uma biblioteca
import module
module.saudacao('Murilo')
# Uso → nome_modulo.nome_funcao(argumentos)

funcionario = module.pessoa1
print(funcionario)
funcionarioNome = module.pessoa1['nome']
print(funcionarioNome)
funcionarioIdade = module.pessoa1['idade']
print(funcionarioIdade)
funcionarioCidade = module.pessoa1['cidade']
print(funcionarioCidade)

# Importante: Não importa o nome dado ao módulo, mas a extensão deve ser .py

# Re-naming a Module → pode ser atribuido um alias para o módulo usando a palavra-chave as

import module as mdl
funcionarioNome = mdl.pessoa1['nome']
print('Depois de renomear o módulo:', funcionarioNome)

# Built-in Modules → são módulos embutidos na linguagem
import platform
print(platform.system())

print(dir(platform)) # imprime todas as variáveis - exercício 3
print(platform.architecture())
print(platform.machine())
print(platform.version())

# FROM → esta palavra-chave faz com que seja importado somente uma parte do módulo
from module import pessoa1
print(pessoa1['idade'])