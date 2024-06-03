use museo;
INSERT INTO `artistas` (`NombreArtista`, `FechaNac`, `FechaMuerte`, `Descripcion`, `Corriente`)
VALUES 
(1, '1881-10-25', '1973-04-08', 'Pablo Picasso, pintor y escultor español.', 'Cubismo'),
(2, '1452-04-15', '1519-05-02', 'Leonardo da Vinci, artista y científico italiano.', 'Renacimiento'),
(3, '1907-07-06', '1954-07-13', 'Frida Kahlo, pintora mexicana.', 'Surrealismo');

INSERT INTO `exposiciones` (`IDExposiciones`, `Titulo`, `Imagen`, `NumSala`)
VALUES 
(1, 'Exposición de Picasso', 'i', 101),
(2, 'Renacimiento Italiano', 'i', 102),
(3, 'Frida Kahlo: Viva la Vida', 'i', 103);

INSERT INTO `obras` (`IDObra`, `Titulo`, `Descripcion`, `Fecha`, `Imagen`, `IDArtista`, `IDExposicion`)
VALUES 
(1, 'Guernica', 'Pintura de Pablo Picasso', '1937-06-04', 'i', 1, 1),
(2, 'La Última Cena', 'Fresco de Leonardo da Vinci', '1498-01-01', 'i', 2, 2),
(3, 'Las Dos Fridas', 'Pintura de Frida Kahlo', '1939-01-01', 'i', 3, 3);

INSERT INTO `audioguias` (`IDAudioguia`, `IDObra`, `Audio`, `Duracion`)
VALUES 
(1, 1, 'a', '00:05:30'),
(2, 2, 'b', '00:07:45'),
(3, 3, 'c', '00:06:20');
