use museo;

INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Normal', 10.00, '1 hora');
INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Reducida', 7.50, '1 hora');
INSERT INTO tarifas (TipoTarifa, Precio, Duracion) VALUES ('Grupo', 30.00, '1 hora');



INSERT INTO `artistas` (`NombreArtista`, `FechaNac`, `FechaMuerte`, `Descripcion`, `Corriente`)
VALUES 
('Pablo Picasso', '1881-10-25', '1973-04-08', 'Pablo Picasso, pintor y escultor español.', 'Cubismo'),
('Leonardo da Vinci', '1452-04-15', '1519-05-02', 'Leonardo da Vinci, artista y científico italiano.', 'Renacimiento'),
('Frida Kahlo', '1907-07-06', '1954-07-13', 'Frida Kahlo, pintora mexicana.', 'Surrealismo');


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

INSERT INTO `exposiciones` (`IDExposiciones`, `Titulo`, `Imagen`, `NumSala`)
VALUES 
(2, 'Exposición de Picasso', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_picasso.jpg', 1),
(3, 'Renacimiento Italiano', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_renacimientoitaliano.jpg', 2),
(4, 'Frida Kahlo: Viva la Vida', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\exposicion_frida.jpg', 3);

INSERT INTO `obras` (`Titulo`, `Descripcion`, `Fecha`, `Imagen`, `IDArtista`, `NumSala`)
VALUES 
('Guernica', 'Pintura de Pablo Picasso', '1937-06-04', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\guernica.jpg', 1, 1),
('La Gioconda', 'El retrato de Lisa Gherardini, esposa de Francesco del Giocondo.', '1503-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\monalisa.jpg', 2, 2),
('La Última Cena', 'Fresco de Leonardo da Vinci', '1498-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\ultimacena.jpg', 2, 2),
('Las Dos Fridas', 'Pintura de Frida Kahlo', '1939-01-01', 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\dosfridas.jpg', 3, 3);

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