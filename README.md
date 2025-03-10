# User Sign-In System

A simple command-line application that allows users to create accounts, sign in, and interact with a MySQL database to store user credentials.

## Features

- **Create New Account**: Users can create a new account by providing a username, email, and password. The application ensures that the username and email are unique.
- **Sign In**: Users can log in with their username and password. The system will check if the credentials are valid.
- **Database Integration**: User data (username, email, and password) is stored in a MySQL database.

## Requirements

- Python 3.x
- `mysql-connector` Python package
- `pwinput` Python package
- MySQL Server with a database named `user_db`

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/sign-in-system.git
    cd sign-in-system
    ```

2. **Set up the database**:
    - Create a MySQL database named `user_db`.
    - Run the following SQL to create the `Users` table:
    ```sql
    CREATE TABLE IF NOT EXISTS Users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL UNIQUE,
        username VARCHAR(64) NOT NULL UNIQUE,
        pass VARCHAR(64) NOT NULL
    );
    ```

3. **Install required Python packages**:
    ```bash
    pip install mysql-connector-python pwinput
    ```

4. **Run the application**:
    ```bash
    python script.py
    ```

## Functions

### `createAcc()`
- Prompts the user to input a username, email, and password.
- Checks if the username or email already exists. If they do, the user is prompted to try again.
- Inserts the new account information into the `Users` table in the MySQL database.

### `insert_user(username, email, passwd)`
- Inserts the user information (username, email, password) into the database.
- Commits the changes to the database or rolls back in case of an error.

### `hasUser(username)`
- Checks if a given username already exists in the database.

### `hasEmail(email)`
- Checks if a given email already exists in the database.

### `passRequire()`
- Prompts the user to input a password, ensuring it is at least 8 characters long.

### `signin()`
- Prompts the user to input a username and password for sign-in.
- Checks the credentials against the data in the database. If valid, the user is logged in.

### `clear_screen()`
- Clears the terminal screen to make the interface cleaner.

### `option_handler(option)`
- Handles user input for different options: create account, sign in, or quit the application.
  
## Usage

Upon running the program, the user will be presented with the following options:
1. Create New Account
2. Sign In
3. Quit Application

### Create New Account:
- The user will be asked to enter a **username**, **email**, and **password**.
- If the username or email already exists, the user will be prompted to try again.
  
### Sign In:
- The user will enter their **username** and **password**. If valid, the system logs the user in.

### Quit Application:
- Exits the application.

## Error Handling

- If there is an issue with the database connection or an operation, an error message will be shown.
- Invalid user inputs, such as selecting a non-existent option, will prompt the user to try again.

## Notes

- Ensure that MySQL server is running and that the credentials for connecting to the database are correct.
- The database connection uses the default username (`root`) and an empty password. You may need to modify these details depending on your MySQL setup.

