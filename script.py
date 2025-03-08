import os
import pwinput
import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "user_db"
)

cursor = db.cursor()

def signin():
    print("<------------- Sign In --------------->")
    username = input('Username: ')
    email = input('Email: ')

    while hasUser(username) and hasEmail(email):
        username = input('Username: ')
        email = input('Email: ')
        passwd = passRequire()

def hasUser(username):
    try:
        cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result:
            print(f"Error: Username '{username}' already exists. Please choose a different username.")   
            return False         
        else:
            print("Username is available.")
            return True
    except Error as e: 
        print(f"Error: {e}")
    
def hasEmail(email):
    try:
        cursor.execute("SELECT * FROM Users WHERE email = %s", (email,))
        result = cursor.fetchone()

        if result:
            print(f"Error: Email '{email}' already exists. Please enter a different email")
            return False
        else:
            print("Email is available")
            return True
    except Error as e: 
        print(f"Error: {e}")

def passRequire():
    password = pwinput.pwinput(prompt="Password: ")

    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = pwinput.pwinput(prompt="Password: ")

