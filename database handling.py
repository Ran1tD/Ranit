import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

abc=mydb.cursor()

abc.execute("create database msit")
print("database created successfully")