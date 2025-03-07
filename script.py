import os
import mysql.connector

try:
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Fabangel0!",
        database = "userdatabase"
    )

    if db.is_connected():
        print("Succesfully connected")
    else:
        print("Connection Failed.")

    db.close()

except mysql.connector.Error as e:
    print(f"Error: {e}")

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS userdatabase")
cursor.execute("CREATE TABLE IF NOT EXISTS Account (id INT PRIMARY KEY, username VARCHAR(64), password VARCHAR(64))")

cursor.close()
db.close()


def signin():
    username = ""
    password = ""

    