CREATE DATABASE Cine;
USE Cine;
CREATE TABLE Series(
idSerie INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(255),
temporadas INT,
valoracion DOUBLE,
premios INT,
director varchar(255),
productora varchar(255)
);
