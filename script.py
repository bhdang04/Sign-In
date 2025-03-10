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

def createAcc():
    print("<------------- Create Account --------------->")
    username = " "
    email = " "
    if hasUser(username) and hasEmail(email):
        username = input('Username: ')
        email = input('Email: ')

    passwd = passRequire()
    insert_user(username, email, passwd)

def insert_user(username, email, password):
    try:
        query = "INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        db.commit()
        print("Account Created Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

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
    
    return password

def option_handler(option):
    try:
        option = int(option)
    except ValueError:
        print("Invalid Option. Please enter a number.")
        return
    
    if option == 1:
        createAcc()
    elif option == 2:
        signin()
    elif option == 3:
        print("Successfully Exited")
        exit()
    else:
        print("Invalid Option")

def signin():
    print("<--------------- Sign In --------------->")
    username = input("Username: ")
    password = pwinput.pwinput(prompt="Password: ")
    cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()

    if result:
        print("You have successfully Logged In")
    else:
        print("Invalid Login")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

option = " "
while option != "3":
    option = input("1. Create New Account \n"
                "2. Sign In \n"
                "3. Quit Application \n"
                "Choose one of the option above (1-3): ")
    clear_screen()
    option_handler(option)
cursor.close()
db.close()