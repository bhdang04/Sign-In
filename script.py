import os
import pwinput
import subprocess
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

def option_handler(option):
    match option:
        case 1:
            createAcc()
        case 2:
            signin()
        case 3:
            return "Successfully Quit Application"
        case _:
            return "Invalid Option"

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
    os_name = os_name
    if os_name == 'posix':
        subprocess.call('clear')
    elif os_name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        print("OS not supported to clear screen.")

option = input("1. Create New Account \n"
    "2. Sign In \n"
    "3. Quit Application \n"
    "Choose one of the option above (1-3): ")
clear_screen()
option_handler(option)