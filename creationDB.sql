--Permet de désactivé la vérification des clefs étrangères
SET FOREIGN_KEY_CHECKS = 0;

--Permet de vérifié si une table existe avant de la supprimé
DROP TABLE IF EXISTS Matricule;
DROP TABLE IF EXISTS Module;
DROP TABLE IF EXISTS Instructions;

--Permet de réactivé la vérification  des clefs étrangères
SET FOREIGN_KEY_CHECKS = 1;

--Créatiion de la table des instructions
CREATE TABLE Instructions
(
    id INTEGER(10) NOT NULL PRIMARY KEY,
    nom VARCHAR(30) NOT NULL,
    `description` VARCHAR(2048) NOT NULL
);

--Création de la table des modules
CREATE TABLE Module
(
    id INTEGER(6) NOT NULL PRIMARY KEY,
    `schema` VARCHAR(300) NOT NULL,
    nom VARCHAR(30) NOT NULL,
    instructionsId INTEGER(10) NOT NULL,
    FOREIGN KEY (instructionsId) REFERENCES Instructions(id)
);
--Création de la table des matricules
CREATE TABLE Matricule
(
    numero VARCHAR(6) NOT NULL PRIMARY KEY,
    moduleId INTEGER(6) NOT NULL,
    FOREIGN KEY (moduleId) REFERENCES Module(id)
);