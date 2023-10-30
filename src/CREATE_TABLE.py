import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

cursor = db.cursor()
query = "CREATE TABLE users (name VARCHAR(255), age INT(3), tel VARCHAR(10))"
cursor.execute(query)

cursor.close()
db.close()