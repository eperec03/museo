CREATE DATABASE museo;
USE museo;
CREATE TABLE USUARIOS (
    DNI varchar(9) NOT NULL,
    UsuNombreCompleto varchar(50) NOT NULL,
    Usutfno varchar(9) NOT NULL,
    UsuEmail varchar(50) NOT NULL,
    UsuTitularMP varchar(50),
    UsuCvvMP int,
    UsuCadMP date,
    UsuContraseña varchar(100) NOT NULL,
    UsuFecha date NOT NULL ,
    CONSTRAINT PK_UsuId PRIMARY KEY (DNI),
    CONSTRAINT UECHECK CHECK (UsuEmail LIKE '%@%.com'),
    CONSTRAINT UQ_UsuEmail UNIQUE (UsuEmail),
    CONSTRAINT UCMPCHECK CHECK (UsuCvvMP >= 0 AND UsuCvvMP <= 999),
);

INSERT INTO USUARIOS (DNI, UsuNombreCompleto, Usutfno, UsuEmail, UsuTitularMP, UsuCvvMP, UsuCadMP, UsuContraseña, UsuFecha)
VALUES ('71345267S', 'Pedro Alonso Juez', '651634873', 'pedritoalju@gmail.com', 'Pedro Alonso Juez', 234, '2030-06-07', 'ped7alJu', '2024-04-25');

SELECT * FROM USUARIOS;
