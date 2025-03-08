CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(64) NOT NULL UNIQUE,
    pass VARCHAR(64) NOT NULL
);

INSERT INTO Users(email, username, pass)
VALUES ('dragonfame10@gmail.com', 'dragonfame10', 'cool1234');
