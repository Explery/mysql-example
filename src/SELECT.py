import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

cursor = db.cursor()

# Normal
query = "SELECT * FROM users"
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    print("Result: " + str(result))

# Condition
query = "Select name FROM users WHERE age = 15"
cursor.execute(query)

results = cursor.fetchall()

for result in results:
    print("name: " + result[0])