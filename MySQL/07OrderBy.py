# Order By
import mysql.connector
db1 = mysql.connector.connect (
    host='localhost',
    user = 'root',
    password='daskiblou1!',
    database='mydatabase'
)

mycursor=db1.cursor()
# sql="SELECT * FROM cadastropessoas ORDER BY nome"
sql="SELECT * FROM cadastropessoas ORDER BY nome DESC"
mycursor.execute(sql)
result=mycursor.fetchall()
for nomeAsc in result:
    print(nomeAsc)