# Create Table
import mysql.connector

db1=mysql.connector.connect (
    host="localhost",
    user="root",
    password="daskiblou1!",
    database="mydatabase"
)

mycursor=db1.cursor()

'''
mycursor.execute("CREATE TABLE cadastroPessoas (nome VARCHAR(100), nota1 int)")
'''

# Check if Table Exists
'''
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table) # ('cadastropessoas',)
'''

# Primary Key
'''
mycursor.execute("CREATE TABLE cadastropessoas (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), nota1 int)") # Table 'cadastropessoas' already exists
'''

# Se a tabela existe, use ALTER TABLE
mycursor.execute("ALTER TABLE cadastropessoas ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY)")
