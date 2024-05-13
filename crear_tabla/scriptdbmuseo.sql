CREATE DATABASE museo;
USE museo;
CREATE TABLE USUARIOS (
    DNI varchar(9) NOT NULL,
    UsuNombreCompleto varchar(50) NOT NULL,
    Usutfno varchar(9) NOT NULL,
    UsuEmail varchar(50) NOT NULL,
    UsuTitularMP varchar(50) not null,
    UsuNumTarjMP varchar(16) not null,
    UsuCvvMP int not null,
    UsuCadMP date not null,
    UsuContrasenna varchar(100) NOT NULL,
    UsuFecha date NOT NULL ,
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