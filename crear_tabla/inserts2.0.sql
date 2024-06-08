INSERT INTO servicios (Nombre) VALUES ('Carpinteria');
SELECT IDServicios FROM servicios WHERE Nombre = 'Carpinteria';
select * from servicios;
select * from exposiciones;
select * from obras;
select * from obrassubastadas;
select * from juegos;
select * from juegossalas;
DELETE FROM SERVICIOS WHERE IdServicios=5;
select * from salas;
select * from resenas;
select * from artistas;
select * from juegosobras;
select * from audioguias;
DELETE FROM USUARIOS WHERE DNI='123456789';
DELETE FROM Obras where IDObra=6;
use museo;
select * from tarifas;
select * from clientespremium;

DELETE FROM SERVICIOS WHERE IDServicios=5;
UPDATE JuegosObras SET IDObra = 1 WHERE IDJuegoObra=5;

select * from subastas;

INSERT INTO SERVICIOS (Nombre) value('Catalogo');
INSERT INTO Catalogo (IdCatalogo,Titulo,Imagen) value(6,'Prueba','a');

select * from objetos;

select * from usuarios;

