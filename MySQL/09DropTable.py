import mysql.connector

db1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1!2@3#4$",
    database="mydatabase"
)

mycursor = db1.cursor()
sql="DROP TABLE IF EXISTS p1"
mycursor.execute(sql)
print(mycursor)
if mycursor:
    print('Tabela removida')
else:
    print('Tabela não existe.')