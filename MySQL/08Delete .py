# Delete
'''
import mysql.connector
db1=mysql.connector.connect(
    host='localhost',
    user='root',
    password='daskiblou1!',
    database='mydatabase'
)

sql='SELECT * FROM cadastropessoas'
mycursor=db1.cursor()
mycursor.execute(sql)
result=mycursor.fetchall()
contador = 1
for item in result:
    print(contador, item)
    contador+=1
'''

# sql="DELETE FROM cadastropessoas where nome = 'Luisinho'"
# mycursor.execute(sql)
# db1.commit()

# Prevent SQL Injection
import mysql.connector
db1=mysql.connector.connect(
    host='localhost',
    user='root',
    password='daskiblou1!',
    database='mydatabase'
)
sql="DELETE FROM cadastropessoas WHERE nome=%s"
value=('Zezinho',)
mycursor=db1.cursor()
result=db1.commit()
print(mycursor.rowcount, " registros apagados.")

sql="SELECT * FROM cadastropessoas"
mycursor.execute(sql)
result=mycursor.fetchall()
for item in result:
    print(item)

