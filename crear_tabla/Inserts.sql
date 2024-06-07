use museo;
INSERT INTO `mapa` (`IDMapa`,`imagen`) values (1,'a');
INSERT INTO `artistas` (`NombreArtista`, `FechaNac`, `FechaMuerte`, `Descripcion`, `Corriente`)
VALUES 
('Pablo Picasso', '1881-10-25', '1973-04-08', 'Pablo Picasso, pintor y escultor español.', 'Cubismo'),
('Leonardo da Vinci', '1452-04-15', '1519-05-02', 'Leonardo da Vinci, artista y científico italiano.', 'Renacimiento'),
('Frida Kahlo', '1907-07-06', '1954-07-13', 'Frida Kahlo, pintora mexicana.', 'Surrealismo');
insert into clienteestandar (NumEntrada,PrecioEntrada) values (25,25.00);
select * from artistas;
INSERT INTO `salas` (`NumSala`, `Capacidad`, `Tematica`, `IDMapa`)
VALUES 
(101, 50, 'Surrealismo', 1),
(102, 75, 'Generacion del 98', 1),
(103, 90, 'Brutalismo', 1);
insert into Servicios (Nombre) VALUES ('Frida Kahlo: Viva la Vida');
INSERT INTO `exposiciones` (`IdExposiciones`,`Titulo`, `Imagen`, `NumSala`)
VALUES 
( 1,'Exposición de Picasso', 'i', 101),
( 2,'Renacimiento Italiano', 'i', 102),
( 3,'Frida Kahlo: Viva la Vida', 'i', 103);

INSERT INTO `obras` (`Titulo`, `Descripcion`, `Fecha`, `Imagen`, `IDArtista`, `IDExposicion`)
VALUES 
('Guernica', 'Pintura de Pablo Picasso', '1937-06-04', 'i', 1, 1),
('La Última Cena', 'Fresco de Leonardo da Vinci', '1498-01-01', 'i', 2, 2),
('Las Dos Fridas', 'Pintura de Frida Kahlo', '1939-01-01', 'i', 3, 3);

INSERT INTO `audioguias` (`IDObra`, `Audio`, `Duracion`)
VALUES 
(1, 'a', '00:05:30'),
(2, 'b', '00:07:45'),
(3, 'c', '00:06:20');

INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Normal', 10.00, '1 hora');
INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Reducida', 7.50, '1 hora');
INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Grupo', 30.00, '1 hora');

select * from tarifas
INSERT INTO juegos (Nombre, Dificultad, Descripcion) VALUES ('Snake', 'Medio', 'Comerse Manzana');
select * from juegos

