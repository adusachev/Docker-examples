use db;

CREATE TABLE people_table(
    PearsonID int not null AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    age int(100) NOT NULL,
    PRIMARY KEY (PearsonID)
);
