CREATE DATABASE Cine;
USE Cine;
CREATE TABLE Series(
idSerie SERIAL NOT NULL PRIMARY KEY,
nombre VARCHAR(255),
temporadas INT,
valoracion DECIMAL(10,0),
premios INT,
director varchar(255),
productora varchar(255)
);
