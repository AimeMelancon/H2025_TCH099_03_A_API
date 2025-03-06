DROP TABLE INSTRUCTIONS CASCADE CONSTRAINT;
DROP TABLE MODULE CASCADE CONSTRAINT;
DROP TABLE MATRICULE CASCADE CONSTRAINT;


CREATE TABLE Instructions
(
    id INTEGER(10) NOT NULL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    `description` VARCHAR(2048) NOT NULL
);

CREATE TABLE Module
(
    id INTEGER(6) NOT NULL PRIMARY KEY,
    `schema` VARCHAR(300) NOT NULL,
    nom VARCHAR(30) NOT NULL,
    instructionsId INTEGER(10) NOT NULL,
    FOREIGN KEY (instructionsId) REFERENCES Instructions(id)
);

CREATE TABLE Matricule
(
    numero VARCHAR(6) NOT NULL PRIMARY KEY,
    moduleId INTEGER(6) NOT NULL,
    FOREIGN KEY (moduleId) REFERENCES Module(id)
);