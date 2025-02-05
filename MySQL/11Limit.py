import mysql.connector

db1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1!2@3#4$",
    database="bancodados"
)

mycusor = db1.cursor()
# mycusor.execute("SELECT * FROM pessoa LIMIT 5") # Os primeiros 5 registros da tabela
# result=mycusor.fetchall()

# for item in result:
#     print(item)

mycusor.execute("SELECT * FROM pessoa LIMIT 5 OFFSET 2") # Os 5 registros da tabela ignorando os 2 primeiros registros.
result=mycusor.fetchall()

for item in result:
    print(item)