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
    username = input('Username: ')
    email = input('Email: ')

    while hasUser(username) or hasEmail(email):
        print("Username or Email already taken. Try again.")
        username = input('Username: ')
        email = input('Email: ')

    passwd = passRequire()
    insert_user(username, email, passwd)

def insert_user(username, email, passwd):
    try:
        cursor.execute("INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)", (username, email, passwd))
        db.commit()
        print("Account Created Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

def hasUser(username):
    cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
    return cursor.fetchone() is not None
    
def hasEmail(email):
    cursor.execute("SELECT * FROM Users WHERE email = %s", (email,))
    return cursor.fetchone() is not None

def passRequire():
    password = pwinput.pwinput(prompt="Password: ")

    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = pwinput.pwinput(prompt="Password: ")
    
    return password

def option_handler(option):
    if option == 1:
        createAcc()
    elif option == 2:
        signin()
    elif option == 3:
        print("Successfully Exited")
        exit()
    elif option == 567:
        cursor.execute("SELECT * FROM Users")
        for row in cursor.fetchall():
            print(row)
    else:
        print("Invalid Option")

def signin():
    print("<--------------- Sign In --------------->")
    username = input('Username: ')
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

option = 0
while option != 3:
    option = int(input("1. Create New Account \n"
                "2. Sign In \n"
                "3. Quit Application \n"
                "Choose one of the option above (1-3): "))
    clear_screen()
    option_handler(option)
cursor.close()
db.close()