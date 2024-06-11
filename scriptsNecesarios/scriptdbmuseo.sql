DROP database museo;
CREATE DATABASE museo;
USE museo;
CREATE TABLE USUARIOS (
    DNI VARCHAR(9) NOT NULL,
    UsuNombreCompleto VARCHAR(50) NOT NULL,
    Usutfno VARCHAR(9) NOT NULL,
    UsuEmail VARCHAR(50) NOT NULL,
    UsuTitularMP VARCHAR(50) NOT NULL,
    UsuNumTarjMP VARCHAR(16) NOT NULL,
    UsuCvvMP INT NOT NULL,
    UsuCadMP DATE NOT NULL,
    UsuContrasenna VARCHAR(100) NOT NULL,
    UsuFecha DATE NOT NULL,
    CONSTRAINT PK_UsuId PRIMARY KEY (DNI),
    CONSTRAINT UECHECK CHECK (UsuEmail LIKE '%@%.com'),
    CONSTRAINT UQ_UsuEmail UNIQUE (UsuEmail),
    CONSTRAINT UCMPCHECK CHECK (UsuCvvMP >= 0 AND UsuCvvMP <= 999)
);

INSERT INTO USUARIOS (DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP,  UsuNumTarjMP,  UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha)
VALUES ('71345267S', 'Pedro Alonso Juez', '651634873', 'pedritoalju@gmail.com', 'Pedro Alonso Juez', '454521216589 ',234, '2030-06-07', 'ped7alJu', '2024-04-25');

SELECT * FROM USUARIOS;
SELECT * FROM USUARIOS WHERE DNI = "71345267S";

INSERT INTO USUARIOS (DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP,  UsuNumTarjMP,  UsuCvvMP, UsuCadMP, UsuContrasenna, UsuFecha)
VALUES ('71345267A', 'Pedro Alonso Juez', '651634873', 'pedritoalju7@gmail.com', 'Pedro Alonso Juez', '454521216589 ',234, '2030-06-07', 'ped7alJu', '2024-04-25');

CREATE TABLE MAPA (
    IdMapa INT NOT NULL,
    Imagen LONGBLOB NOT NULL,
    PRIMARY KEY (IdMapa)
);
SHOW VARIABLES LIKE 'secure_file_priv';
INSERT INTO MAPA (IdMapa, Imagen)
VALUES (1, LOAD_FILE('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/imagenmuseo.jpg'));
SELECT 	IdMapa, Imagen FROM MAPA WHERE IdMapa = 1;
