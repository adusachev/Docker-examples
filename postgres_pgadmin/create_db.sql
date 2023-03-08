CREATE TABLE accounts(
    user_id serial PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP
);

INSERT INTO accounts(username, password, email, created_on)
VALUES('user', 'pass', 'test@email.com', CURRENT_TIMESTAMP);



CREATE TABLE people(
    id serial PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO people(name, surname, email)
VALUES('User Name', 'User Surname', 'test@email.com')
