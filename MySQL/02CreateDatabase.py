# Create Database
'''
import mysql.connector
mydb= mysql.connector.connect (
    host="localhost",
    user="root",
    password="daskiblou1!"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
'''
'''
import mysql.connector
mydb = mysql.connector.connect (
    host='localhost',
    user='root',
    password='daskiblou1!'
)
mycursor = mydb.cursor()
mycursor.execute('show databases')
# Check if Database Exists
for x in mycursor:
    print(x)
'''

import mysql.connector
db1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='daskiblou1!',
    database='mydatabase'
)
print(db1) # <mysql.connector.connection.MySQLConnection object at 0x000002082F558350>