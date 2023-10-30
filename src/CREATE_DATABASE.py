import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

query = "CREATE DATABASE python"
cursor.execute(query)

cursor.close()
db.close()