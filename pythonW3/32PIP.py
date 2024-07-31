# PIP → gerenciador de pacotes ou de módulos.
# Package contém todos os arquivos que você precisa para um módulo
# Modulos são códigos de biblioteca que você pode inclui no seu projeto

'''
C:\\Users\\Murilo>pip --version
pip 24.1.1 from C:\\Users\\Murilo\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\local-packages\\Python312\\site-packages\\pip (python 3.12)
'''

'''
PS C:\\github\\pythonW3> pip install camelcase
Defaulting to user installation because normal site-packages is not writeable
Collecting camelcase
  Downloading camelcase-0.2.tar.gz (1.3 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: camelcase
  Building wheel for camelcase (setup.py) ... done
  Created wheel for camelcase: filename=camelcase-0.2-py3-none-any.whl size=1778 sha256=0715624d86be89a606a482aecfd3cf4460b3e5e11eee31aa6f657df04faedd7c
  Stored in directory: c:\\users\\murilo\\appdata\\local\\pip\\cache\\wheels\\a7\\40\\a3\\900133dd6de3e10c219659fec4118138db05d778e519c0b2bc
Successfully built camelcase
Installing collected packages: camelcase
Successfully installed camelcase-0.2
'''

import camelcase
cc = camelcase.CamelCase()
myText = "i am lerning about pip and my first package was camelcase."
print(cc.hump(myText))

# Remover um pacote
# pip uninstall camelcase

# Lista de packages
'''
pip list
Package                   Version
------------------------- -----------
altgraph                  0.17.4
camelcase                 0.2
et-xmlfile                1.1.0
numpy                     2.0.0
openpyxl                  3.1.5
packaging                 24.0
pandas                    2.2.2
pefile                    2023.2.7
pip                       24.1.1
psgcompiler               5.0.0
pyasn1                    0.5.1
pyinstaller               6.5.0
pyinstaller-hooks-contrib 2024.3
PySimpleGUI               5.0.3
pysimplegui-exemaker      1.3.0
python-dateutil           2.9.0.post0
pytz                      2024.1
pywin32-ctypes            0.2.2
rsa                       4.9
setuptools                69.2.0
six                       1.16.0
tzdata                    2024.1
wheel                     0.43.0
XlsxWriter                3.2.0
'''

# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 3-4: truncated \UXXXXXXX
# Solução: Substitua \ por \\
