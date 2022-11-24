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

# Inserts de ejemplo
insert into Series(nombre, temporadas, valoracion, premios, director, productora) values('Breaking bad', '5', 9.9, 10000, 'Vince Gilligan', 'Sony pictures');
insert into Series(nombre, temporadas, valoracion, premios, director, productora) values('Dark', '7', 5, 3, 'Un tío random', 'Alguna productora alemana');
insert into Series(nombre, temporadas, valoracion, premios, director, productora) values('Stranger Things', '4', 0.0, 0, 'Shawn Levy', 'Netflix');
