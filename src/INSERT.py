import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

cursor = db.cursor()

# Excute one info
query = "INSERT INTO users (name, age, tel) VALUES (%s, %s, %s)"
val = ("John", 15, "01xxxxxxxx")
cursor.execute(query, val)

# Excute more than one info
query = "INSERT INTO users (name, age, tel) VALUES (%s, %s, %s)"
val = [("John", 15, "01xxxxxxxx"), ("Max", 18, "02xxxxxxxx"), ("Cream", 15, "03xxxxxxxx")]
cursor.executemany(query, val)

db.commit()
cursor.close()
db.close()