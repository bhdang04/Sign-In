DROP TABLE IF EXISTS Users;

CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(64) NOT NULL UNIQUE,
    pass VARCHAR(64) NOT NULL
);

SELECT * FROM Users;
