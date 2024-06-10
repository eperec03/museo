use museo;


INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Normal', 10.00, '1 hora');
INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Reducida', 7.50, '1 hora');
INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Grupo', 30.00, '1 hora');



INSERT INTO `artistas` (`NombreArtista`, `FechaNac`, `FechaMuerte`, `Descripcion`, `Corriente`)
VALUES 
('Pablo Picasso', '1881-10-25', '1973-04-08', 'Pablo Picasso, pintor y escultor español.', 'Cubismo'),
('Leonardo da Vinci', '1452-04-15', '1519-05-02', 'Leonardo da Vinci, artista y científico italiano.', 'Renacimiento'),
('Frida Kahlo', '1907-07-06', '1954-07-13', 'Frida Kahlo, pintora mexicana.', 'Surrealismo'),
('Vincent van Gogh', '1853-03-30', '1890-07-29', 'Vincent van Gogh, pintor postimpresionista neerlandés.', 'Postimpresionismo'),
('Claude Monet', '1840-11-14', '1926-12-05', 'Claude Monet, pintor francés, fundador del impresionismo.', 'Impresionismo'),
('Salvador Dalí', '1904-05-11', '1989-01-23', 'Salvador Dalí, pintor surrealista español.', 'Surrealismo'),
('Andy Warhol', '1928-08-06', '1987-02-22', 'Andy Warhol, artista estadounidense, figura principal del pop art.', 'Pop Art'),
('Henri Matisse', '1869-12-31', '1954-11-03', 'Henri Matisse, pintor, dibujante y escultor francés.', 'Fauvismo'),
('Jackson Pollock', '1912-01-28', '1956-08-11', 'Jackson Pollock, pintor estadounidense, figura principal del expresionismo abstracto.', 'Expresionismo Abstracto');


insert into servicios (Nombre) values ('MAPA');
insert into mapa (IDMapa,Imagen) values (1,"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\mapa.png");


INSERT INTO `salas` (`NumSala`, `Capacidad`, `Tematica`, `IDMapa`)
VALUES 
(1, 50, 'Cubismo y Picasso', 1),
(2, 75, 'Renacimiento Italiano', 1),
(3, 90, 'Arte Mexicano y Frida Kahlo', 1);

INSERT INTO servicios (Nombre) VALUES ('Exposición de Picasso');
INSERT INTO servicios (Nombre) VALUES ('Renacimiento Italiano');
INSERT INTO servicios (Nombre) VALUES ('Frida Kahlo: Viva la Vida');
INSERT INTO servicios (Nombre) VALUES ('Arte Moderno');
INSERT INTO servicios (Nombre) VALUES ('Escultura Griega');


INSERT INTO `exposiciones` (`IDExposiciones`, `Titulo`, `Imagen`, `Descripcion`, `NumSala`)
VALUES 
(2, 'Exposición de Picasso', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_picasso.jpg', 'Disfruta de una colección única de obras maestras del renombrado artista Pablo Picasso.', 1),
(3, 'Renacimiento Italiano', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_renacimientoitaliano.jpg', 'Explora el florecimiento del arte renacentista italiano y su impacto en la historia del arte europeo.', 2),
(4, 'Frida Kahlo: Viva la Vida', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_frida.jpg', 'Sumérgete en la vida y obra de la icónica artista Frida Kahlo, una figura destacada del arte mexicano del siglo XX.', 3),
(5, 'Arte Moderno', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_artemoderno.jpg', 'Explora la evolución del arte moderno a través de una colección ecléctica de obras maestras que abarcan desde el impresionismo hasta el arte contemporáneo.', 1),
(6, 'Escultura Griega', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_esculturagriega.jpg', 'Sumérgete en la belleza y el significado de la escultura griega clásica, donde cada obra cuenta una historia única de la antigua civilización griega.', 2);

INSERT INTO `obras` (`Titulo`, `Descripcion`, `Fecha`, `Imagen`, `IDArtista`, `NumSala`)
VALUES 
('Guernica', 'Pintura de Pablo Picasso', '1937-06-04', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\guernica.jpg', 1, 1),
('La Gioconda', 'El retrato de Lisa Gherardini, esposa de Francesco del Giocondo.', '1503-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\monalisa.jpg', 2, 2),
('La Última Cena', 'Fresco de Leonardo da Vinci', '1498-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\ultimacena.jpg', 2, 2),
('Las Dos Fridas', 'Pintura de Frida Kahlo', '1939-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\dosfridas.jpg', 3, 3),
('Starry Night', 'Pintura de Vincent van Gogh', '1889-06-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\starrynight.jpg', 4, 1),
('Water Lilies', 'Serie de pinturas de Claude Monet', '1920-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\waterlilies.jpg', 5, 1),
('The Persistence of Memory', 'Pintura de Salvador Dalí', '1931-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\persistenceofmemory.jpg', 6, 2);

INSERT INTO `clienteestandar` (`NumEntrada`, `PrecioEntrada`) VALUES
('E0001', 10.50),
('E0002', 11.00),
('E0003', 12.00),
('E0004', 10.75),
('E0005', 9.50),
('E0006', 10.25),
('E0007', 11.50),
('E0008', 12.25),
('E0009', 10.00),
('E0010', 9.75),
('E0011', 11.25),
('E0012', 12.50),
('E0013', 10.50),
('E0014', 11.75),
('E0015', 9.00),
('E0016', 10.00),
('E0017', 11.00),
('E0018', 12.00),
('E0019', 10.75),
('E0020', 9.50),
('E0021', 10.25),
('E0022', 11.50),
('E0023', 12.25),
('E0024', 10.00),
('E0025', 9.75),
('E0026', 11.25),
('E0027', 12.50),
('E0028', 10.50),
('E0029', 11.75),
('E0030', 9.00),
('E0031', 10.00),
('E0032', 11.00),
('E0033', 12.00),
('E0034', 10.75),
('E0035', 9.50),
('E0036', 10.25),
('E0037', 11.50),
('E0038', 12.25),
('E0039', 10.00),
('E0040', 9.75),
('E0041', 11.25),
('E0042', 12.50),
('E0043', 10.50),
('E0044', 11.75),
('E0045', 9.00),
('E0046', 10.00),
('E0047', 11.00),
('E0048', 12.00),
('E0049', 10.75),
('E0050', 9.50),
('E0051', 10.25),
('E0052', 11.50),
('E0053', 12.25),
('E0054', 10.00),
('E0055', 9.75),
('E0056', 11.25),
('E0057', 12.50),
('E0058', 10.50),
('E0059', 11.75),
('E0060', 9.00),
('E0061', 10.00),
('E0062', 11.00),
('E0063', 12.00),
('E0064', 10.75),
('E0065', 9.50),
('E0066', 10.25),
('E0067', 11.50),
('E0068', 12.25),
('E0069', 10.00),
('E0070', 9.75),
('E0071', 11.25),
('E0072', 12.50),
('E0073', 10.50),
('E0074', 11.75),
('E0075', 9.00),
('E0076', 10.00),
('E0077', 11.00),
('E0078', 12.00),
('E0079', 10.75),
('E0080', 9.50),
('E0081', 10.25),
('E0082', 11.50),
('E0083', 12.25),
('E0084', 10.00),
('E0085', 9.75),
('E0086', 11.25),
('E0087', 12.50),
('E0088', 10.50),
('E0089', 11.75),
('E0090', 9.00),
('E0091', 10.00),
('E0092', 11.00),
('E0093', 12.00),
('E0094', 10.75),
('E0095', 9.50),
('E0096', 10.25),
('E0097', 11.50),
('E0098', 12.25),
('E0099', 10.00),
('E0100', 9.75);


INSERT INTO SERVICIOS (Nombre) value('Catalogo');
INSERT INTO Catalogo (IdCatalogo,Titulo,Imagen) value(5,'Catalogo','a');

INSERT INTO objetos (NombreObjeto, imagen, precio, tipo, inspiracion, existencias, agotado, IDCatalogo) 
VALUES 
('Jarron', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\jarron.jpg', 25.00, 'Decoración', 'Arte Clásico', 10, 0, 5),
('Boli', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\boli.jpg', 3.50, 'Papelería', 'Modernismo', 50, 0, 5),
('Coletero', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\coletero.jpg', 5.00, 'Accesorios', 'Arte Contemporáneo', 30, 0, 5),
('Paraguas', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\paraguas.jpg', 15.00, 'Accesorios', 'Arte Impresionista', 20, 0, 5),
('Collar', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\collar.jpg', 12.00, 'Joyería', 'Arte Renacentista', 25, 0, 5),
('Micropuzle', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\micropuzle.jpg', 8.00, 'Juguetes', 'Arte Surrealista', 40, 0, 5),
('Totebag', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\totebag.jpg', 10.00, 'Bolsos', 'Pop Art', 35, 0, 5),
('Funda Cojin', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\funda_cojin.jpg', 12.50, 'Decoración', 'Arte Abstracto', 15, 0, 5),
('Funda Portatil', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\funda_portatil.jpg', 18.00, 'Accesorios', 'Arte Digital', 20, 0, 5);

SHOW VARIABLES LIKE 'secure_file_priv';
insert into audioguias (Titulo,IDObra,Audio,Duracion) VALUES ('Audio Gioconda',2,"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\audio_monalisa.mp3", '00:00:45');

INSERT INTO `subastas` (`Fecha`, `Titulo`, `Descripcion`) VALUES
('2023-01-15', 'Subasta de Invierno', 'Subasta de arte y antigüedades de invierno'),
('2023-02-20', 'Subasta de Primavera', 'Subasta de arte contemporáneo y moderno'),
('2023-03-25', 'Subasta de Arte Impresionista', 'Subasta de obras impresionistas y post-impresionistas'),
('2023-04-10', 'Subasta de Joyas', 'Subasta de joyas exclusivas y relojes'),
('2023-05-05', 'Subasta de Verano', 'Subasta de arte y esculturas de verano'),
('2023-06-18', 'Subasta de Fotografía', 'Subasta de fotografías históricas y contemporáneas'),
('2023-07-22', 'Subasta de Otoño', 'Subasta de arte y muebles antiguos'),
('2023-08-30', 'Subasta de Pintura Moderna', 'Subasta de pinturas modernas y abstractas'),
('2023-09-14', 'Subasta de Arte Latinoamericano', 'Subasta de arte y esculturas de América Latina'),
('2023-10-28', 'Subasta de Fin de Año', 'Subasta de fin de año con una variedad de colecciones');


