# Get Started
'''
https://dev.mysql.com/downloads/installer/
Baixe a versão 8.0.39 que ocupa 2.1M
Clique em "No thanks, just start my download.
A opção "Samples" acusou erro. Voltei uma tela e removi esta opção. Depois de clicar em "avançar" a tela mostrou que o status "complete" dos 3 itens.
Windows Service Name: MySQL80
O driver é o MySQL Connector que pode ser obtido através do pip 
pip install mysql-connector-python
Teste se o driver foi importado corretamente
'''
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="daskiblou1!"
)
print(mydb) # <mysql.connector.connection.MySQLConnection object at 0x000002BD90EEA900>