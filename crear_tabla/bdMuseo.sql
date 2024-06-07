-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: museo
-- ------------------------------------------------------
-- Server version	8.0.35
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
--
-- Table structure for table `artistas`
--
USE MUSEO;
DROP TABLE IF EXISTS `artistas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artistas` (
	`IdArtista`int auto_increment not null,
  `NombreArtista` varchar(50) NOT NULL,
  `FechaNac` date NOT NULL,
  `FechaMuerte` date DEFAULT NULL,
  `Descripcion` varchar(100) DEFAULT NULL,
  `Corriente` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`IdArtista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artistas`
--

LOCK TABLES `artistas` WRITE;
/*!40000 ALTER TABLE `artistas` DISABLE KEYS */;
/*!40000 ALTER TABLE `artistas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audioguias`
--

DROP TABLE IF EXISTS `audioguias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audioguias` (
  `IDAudioguia` int NOT NULL,
  `IDObra` int NOT NULL,
  `Audio` blob NOT NULL,
  `Duracion` time NOT NULL,
  PRIMARY KEY (`IDAudioguia`,`IDObra`),
  KEY `ObraAud_idx` (`IDObra`),
  CONSTRAINT `ObraAud` FOREIGN KEY (`IDObra`) REFERENCES `obras` (`IDObra`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audioguias`
--

LOCK TABLES `audioguias` WRITE;
/*!40000 ALTER TABLE `audioguias` DISABLE KEYS */;
/*!40000 ALTER TABLE `audioguias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalogo`
--

DROP TABLE IF EXISTS `catalogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalogo` (
  `IDCatalogo` int NOT NULL,
  `Imagen` blob NOT NULL,
  PRIMARY KEY (`IDCatalogo`),
  CONSTRAINT `SerCat` FOREIGN KEY (`IDCatalogo`) REFERENCES `servicios` (`IDServicios`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogo`
--

LOCK TABLES `catalogo` WRITE;
/*!40000 ALTER TABLE `catalogo` DISABLE KEYS */;
/*!40000 ALTER TABLE `catalogo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clienteestandar`
--

DROP TABLE IF EXISTS `clienteestandar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clienteestandar` (
  `NumEntrada` varchar(5) NOT NULL,
  `PrecioEntrada` float NOT NULL,
  PRIMARY KEY (`NumEntrada`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clienteestandar`
--

LOCK TABLES `clienteestandar` WRITE;
/*!40000 ALTER TABLE `clienteestandar` DISABLE KEYS */;
/*!40000 ALTER TABLE `clienteestandar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientespremium`
--

DROP TABLE IF EXISTS `clientespremium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientespremium` (
  `ObrasAdquiridas` text,
  `DineroGastado` float DEFAULT '0',
  `Penalizacion` binary(1) DEFAULT NULL,
  `DNI` varchar(9) NOT NULL,
  `TipoTarifa` varchar(15) NOT NULL,
  PRIMARY KEY (`DNI`),
  KEY `TipoTarifa_idx` (`TipoTarifa`),
  CONSTRAINT `cliPreTar` FOREIGN KEY (`TipoTarifa`) REFERENCES `tarifas` (`TipoTarifa`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `UsuCliP` FOREIGN KEY (`DNI`) REFERENCES `usuarios` (`DNI`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientespremium`
--

LOCK TABLES `clientespremium` WRITE;
/*!40000 ALTER TABLE `clientespremium` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientespremium` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliestserv`
--

DROP TABLE IF EXISTS `cliestserv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliestserv` (
  `NumEntrada` varchar(5) NOT NULL,
  `IDServicio` int NOT NULL,
  PRIMARY KEY (`NumEntrada`,`IDServicio`),
  KEY `ServCli_idx` (`IDServicio`),
  CONSTRAINT `ClienteServ` FOREIGN KEY (`NumEntrada`) REFERENCES `clienteestandar` (`NumEntrada`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ServCli` FOREIGN KEY (`IDServicio`) REFERENCES `servicios` (`IDServicios`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliestserv`
--

LOCK TABLES `cliestserv` WRITE;
/*!40000 ALTER TABLE `cliestserv` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliestserv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edicionaudioguias`
--

DROP TABLE IF EXISTS `edicionaudioguias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edicionaudioguias` (
  `IDEdicionaudioguias` int NOT NULL,
  PRIMARY KEY (`IDEdicionaudioguias`),
  CONSTRAINT `menuEdicionAudioguias` FOREIGN KEY (`IDEdicionaudioguias`) REFERENCES `menusedicion` (`IDMenusedicion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edicionaudioguias`
--

LOCK TABLES `edicionaudioguias` WRITE;
/*!40000 ALTER TABLE `edicionaudioguias` DISABLE KEYS */;
/*!40000 ALTER TABLE `edicionaudioguias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edicioncatalogo`
--

DROP TABLE IF EXISTS `edicioncatalogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edicioncatalogo` (
  `IDEdicioncatalogo` int NOT NULL,
  PRIMARY KEY (`IDEdicioncatalogo`),
  CONSTRAINT `MenuEdicionCatalogo` FOREIGN KEY (`IDEdicioncatalogo`) REFERENCES `menusedicion` (`IDMenusedicion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edicioncatalogo`
--

LOCK TABLES `edicioncatalogo` WRITE;
/*!40000 ALTER TABLE `edicioncatalogo` DISABLE KEYS */;
/*!40000 ALTER TABLE `edicioncatalogo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edicionexposiciones`
--

DROP TABLE IF EXISTS `edicionexposiciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edicionexposiciones` (
  `IDEdicionexposiciones` int NOT NULL,
  PRIMARY KEY (`IDEdicionexposiciones`),
  CONSTRAINT `MenuEdicionExpo` FOREIGN KEY (`IDEdicionexposiciones`) REFERENCES `menusedicion` (`IDMenusedicion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edicionexposiciones`
--

LOCK TABLES `edicionexposiciones` WRITE;
/*!40000 ALTER TABLE `edicionexposiciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `edicionexposiciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edicionjuegos`
--

DROP TABLE IF EXISTS `edicionjuegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edicionjuegos` (
  `IDEdicionjuegos` int NOT NULL,
  PRIMARY KEY (`IDEdicionjuegos`),
  CONSTRAINT `MenuEdicionJuegos` FOREIGN KEY (`IDEdicionjuegos`) REFERENCES `menusedicion` (`IDMenusedicion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edicionjuegos`
--

LOCK TABLES `edicionjuegos` WRITE;
/*!40000 ALTER TABLE `edicionjuegos` DISABLE KEYS */;
/*!40000 ALTER TABLE `edicionjuegos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edicionmapa`
--

DROP TABLE IF EXISTS `edicionmapa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edicionmapa` (
  `IDEdicionmapa` int NOT NULL,
  PRIMARY KEY (`IDEdicionmapa`),
  CONSTRAINT `MenuEdicionMapa` FOREIGN KEY (`IDEdicionmapa`) REFERENCES `menusedicion` (`IDMenusedicion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edicionmapa`
--

LOCK TABLES `edicionmapa` WRITE;
/*!40000 ALTER TABLE `edicionmapa` DISABLE KEYS */;
/*!40000 ALTER TABLE `edicionmapa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edicionresennas`
--

DROP TABLE IF EXISTS `edicionresennas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edicionresennas` (
  `IDEdicionResennas` int NOT NULL,
  PRIMARY KEY (`IDEdicionResennas`),
  CONSTRAINT `menuEdicionResenas` FOREIGN KEY (`IDEdicionResennas`) REFERENCES `menusedicion` (`IDMenusedicion`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edicionresennas`
--

LOCK TABLES `edicionresennas` WRITE;
/*!40000 ALTER TABLE `edicionresennas` DISABLE KEYS */;
/*!40000 ALTER TABLE `edicionresennas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editaudioguias`
--

DROP TABLE IF EXISTS `editaudioguias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editaudioguias` (
  `IDEdicionAudioguias` int NOT NULL,
  `IDAudioguia` int DEFAULT NULL,
  PRIMARY KEY (`IDEdicionAudioguias`),
  CONSTRAINT `edicionmenuA` FOREIGN KEY (`IDEdicionAudioguias`) REFERENCES `edicionaudioguias` (`IDEdicionaudioguias`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editaudioguias`
--

LOCK TABLES `editaudioguias` WRITE;
/*!40000 ALTER TABLE `editaudioguias` DISABLE KEYS */;
/*!40000 ALTER TABLE `editaudioguias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editcatalogo`
--

DROP TABLE IF EXISTS `editcatalogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editcatalogo` (
  `IDEdicioncatalogo` int NOT NULL,
  `IDCatalogo` int DEFAULT NULL,
  PRIMARY KEY (`IDEdicioncatalogo`),
  CONSTRAINT `edicionmenuC` FOREIGN KEY (`IDEdicioncatalogo`) REFERENCES `edicioncatalogo` (`IDEdicioncatalogo`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editcatalogo`
--

LOCK TABLES `editcatalogo` WRITE;
/*!40000 ALTER TABLE `editcatalogo` DISABLE KEYS */;
/*!40000 ALTER TABLE `editcatalogo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editexpo`
--

DROP TABLE IF EXISTS `editexpo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editexpo` (
  `IDEdicionExposiciones` int NOT NULL,
  `IDExposicion` int NOT NULL,
  PRIMARY KEY (`IDEdicionExposiciones`,`IDExposicion`),
  KEY `EdicionExpo_idx` (`IDExposicion`),
  CONSTRAINT `EdicionExpo` FOREIGN KEY (`IDExposicion`) REFERENCES `exposiciones` (`IDExposiciones`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Edicionmenu` FOREIGN KEY (`IDEdicionExposiciones`) REFERENCES `edicionexposiciones` (`IDEdicionexposiciones`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editexpo`
--

LOCK TABLES `editexpo` WRITE;
/*!40000 ALTER TABLE `editexpo` DISABLE KEYS */;
/*!40000 ALTER TABLE `editexpo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editjuegos`
--

DROP TABLE IF EXISTS `editjuegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editjuegos` (
  `IDdicionJuegos` int NOT NULL,
  `IDJuegos` int NOT NULL,
  PRIMARY KEY (`IDdicionJuegos`,`IDJuegos`),
  KEY `edicionjuegos_idx` (`IDJuegos`),
  CONSTRAINT `edicionjuegos` FOREIGN KEY (`IDJuegos`) REFERENCES `juegos` (`IDJuego`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `edicionMenuJ` FOREIGN KEY (`IDdicionJuegos`) REFERENCES `edicionjuegos` (`IDEdicionjuegos`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editjuegos`
--

LOCK TABLES `editjuegos` WRITE;
/*!40000 ALTER TABLE `editjuegos` DISABLE KEYS */;
/*!40000 ALTER TABLE `editjuegos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editmapa`
--

DROP TABLE IF EXISTS `editmapa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editmapa` (
  `IDEdicionMapa` int NOT NULL,
  `IDMapa` int DEFAULT NULL,
  PRIMARY KEY (`IDEdicionMapa`),
  KEY `edicionMapa_idx` (`IDMapa`),
  CONSTRAINT `edicionMapa` FOREIGN KEY (`IDMapa`) REFERENCES `mapa` (`IDMapa`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `edicionMenuM` FOREIGN KEY (`IDEdicionMapa`) REFERENCES `edicionmapa` (`IDEdicionmapa`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editmapa`
--

LOCK TABLES `editmapa` WRITE;
/*!40000 ALTER TABLE `editmapa` DISABLE KEYS */;
/*!40000 ALTER TABLE `editmapa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editores`
--

DROP TABLE IF EXISTS `editores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editores` (
  `SSN` varchar(9) NOT NULL,
  `Rol` varchar(30) NOT NULL,
  PRIMARY KEY (`SSN`),
  CONSTRAINT `UsuEditores` FOREIGN KEY (`SSN`) REFERENCES `usuarios` (`DNI`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editores`
--

LOCK TABLES `editores` WRITE;
/*!40000 ALTER TABLE `editores` DISABLE KEYS */;
/*!40000 ALTER TABLE `editores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editresennas`
--

DROP TABLE IF EXISTS `editresennas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `editresennas` (
  `IDEdicionResennas` int NOT NULL,
  `IDResenna` int DEFAULT NULL,
  PRIMARY KEY (`IDEdicionResennas`),
  KEY `IDResenna_idx` (`IDResenna`),
  CONSTRAINT `edicionMenuR` FOREIGN KEY (`IDEdicionResennas`) REFERENCES `edicionresennas` (`IDEdicionResennas`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `IDResenna` FOREIGN KEY (`IDResenna`) REFERENCES `resenas` (`Numresena`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editresennas`
--

LOCK TABLES `editresennas` WRITE;
/*!40000 ALTER TABLE `editresennas` DISABLE KEYS */;
/*!40000 ALTER TABLE `editresennas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exposiciones`
--

DROP TABLE IF EXISTS `exposiciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exposiciones` (
  `IDExposiciones` int NOT NULL,
  `Titulo` varchar(45) NOT NULL,
  `Imagen` blob NOT NULL,
  `NumSala` int NOT NULL,
  PRIMARY KEY (`IDExposiciones`),
  KEY `ExpSal_idx` (`NumSala`),
  CONSTRAINT `ExpSal` FOREIGN KEY (`NumSala`) REFERENCES `salas` (`NumSala`) ON UPDATE CASCADE,
  CONSTRAINT `SerExp` FOREIGN KEY (`IDExposiciones`) REFERENCES `servicios` (`IDServicios`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exposiciones`
--

LOCK TABLES `exposiciones` WRITE;
/*!40000 ALTER TABLE `exposiciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `exposiciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juegos`
--

DROP TABLE IF EXISTS `juegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juegos` (
  `IDJuego` int NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Dificultad` varchar(45) NOT NULL,
  `Descripcion` varchar(100) DEFAULT NULL,
  `ruta` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`IDJuego`),
  CONSTRAINT `SerJue` FOREIGN KEY (`IDJuego`) REFERENCES `servicios` (`IDServicios`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juegos`
--

LOCK TABLES `juegos` WRITE;
/*!40000 ALTER TABLE `juegos` DISABLE KEYS */;
/*!40000 ALTER TABLE `juegos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juegosobras`
--

DROP TABLE IF EXISTS `juegosobras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juegosobras` (
  `IDJuegoobra` int NOT NULL,
  `IDObra` int NOT NULL,
  PRIMARY KEY (`IDJuegoobra`),
  KEY `JuegObr_idx` (`IDObra`),
  CONSTRAINT `JuegObr` FOREIGN KEY (`IDObra`) REFERENCES `obras` (`IDObra`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `JuegoObr` FOREIGN KEY (`IDJuegoobra`) REFERENCES `juegos` (`IDJuego`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juegosobras`
--

LOCK TABLES `juegosobras` WRITE;
/*!40000 ALTER TABLE `juegosobras` DISABLE KEYS */;
/*!40000 ALTER TABLE `juegosobras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juegossalas`
--

DROP TABLE IF EXISTS `juegossalas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juegossalas` (
  `IDJuegossalas` int NOT NULL,
  `IDSala` int NOT NULL,
  PRIMARY KEY (`IDJuegossalas`),
  KEY `SalaJuego_idx` (`IDSala`),
  CONSTRAINT `JuegSal` FOREIGN KEY (`IDJuegossalas`) REFERENCES `juegos` (`IDJuego`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SalaJuego` FOREIGN KEY (`IDSala`) REFERENCES `salas` (`NumSala`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juegossalas`
--

LOCK TABLES `juegossalas` WRITE;
/*!40000 ALTER TABLE `juegossalas` DISABLE KEYS */;
/*!40000 ALTER TABLE `juegossalas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mapa`
--

DROP TABLE IF EXISTS `mapa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mapa` (
  `IDMapa` int NOT NULL,
  `imagen` blob NOT NULL,
  PRIMARY KEY (`IDMapa`),
  CONSTRAINT `SerMap` FOREIGN KEY (`IDMapa`) REFERENCES `servicios` (`IDServicios`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mapa`
--

LOCK TABLES `mapa` WRITE;
/*!40000 ALTER TABLE `mapa` DISABLE KEYS */;
/*!40000 ALTER TABLE `mapa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menusedicion`
--

DROP TABLE IF EXISTS `menusedicion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menusedicion` (
  `IDMenusedicion` int NOT NULL,
  `SSN` varchar(9) DEFAULT NULL,
  PRIMARY KEY (`IDMenusedicion`),
  KEY `MenuEditores_idx` (`SSN`),
  CONSTRAINT `MenuEditores` FOREIGN KEY (`SSN`) REFERENCES `editores` (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menusedicion`
--

LOCK TABLES `menusedicion` WRITE;
/*!40000 ALTER TABLE `menusedicion` DISABLE KEYS */;
/*!40000 ALTER TABLE `menusedicion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objetos`
--

DROP TABLE IF EXISTS `objetos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `objetos` (
  `IDObjeto` int NOT NULL auto_increment,
  `NombreObjeto` varchar(30) not null unique,
  `imagen` blob NOT NULL,
  `precio` float NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `inspiracion` varchar(45) NOT NULL,
  `existencias` int NOT NULL,
  `agotado` binary(1) NOT NULL,
  `IDCatalogo` int NOT NULL,
  PRIMARY KEY (`IDObjeto`),
  CONSTRAINT `CatObj` FOREIGN KEY (`IDCatalogo`) REFERENCES `catalogo` (`IDCatalogo`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objetos`
--

LOCK TABLES `objetos` WRITE;
/*!40000 ALTER TABLE `objetos` DISABLE KEYS */;
/*!40000 ALTER TABLE `objetos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `obras`
--

DROP TABLE IF EXISTS `obras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `obras` (
  `IDObra` int NOT NULL auto_increment,
  `Titulo` varchar(45) NOT NULL,
  `Descripcion` varchar(100) DEFAULT NULL,
  `Fecha` date NULL,
  `Imagen` blob NOT NULL,
  `IDArtista` int NOT NULL,
  `IDExposicion` int NOT NULL,
  PRIMARY KEY (`IDObra`),
  KEY `ExpOb_idx` (`IDExposicion`),
  KEY `ArtObr_idx` (`IDArtista`),
  CONSTRAINT `ArtObr` FOREIGN KEY (`IDArtista`) REFERENCES `artistas` (`IdArtista`) ON UPDATE CASCADE,
  CONSTRAINT `ExpOb` FOREIGN KEY (`IDExposicion`) REFERENCES `exposiciones` (`IDExposiciones`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obras`
--

LOCK TABLES `obras` WRITE;
/*!40000 ALTER TABLE `obras` DISABLE KEYS */;
/*!40000 ALTER TABLE `obras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `obrasexpuestas`
--

DROP TABLE IF EXISTS `obrasexpuestas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `obrasexpuestas` (
  `IDObrasexpuestas` int NOT NULL,
  `Disponible` binary(1) NOT NULL,
  PRIMARY KEY (`IDObrasexpuestas`),
  CONSTRAINT `ObraExp` FOREIGN KEY (`IDObrasexpuestas`) REFERENCES `obras` (`IDObra`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obrasexpuestas`
--

LOCK TABLES `obrasexpuestas` WRITE;
/*!40000 ALTER TABLE `obrasexpuestas` DISABLE KEYS */;
/*!40000 ALTER TABLE `obrasexpuestas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `obrassubastadas`
--

DROP TABLE IF EXISTS `obrassubastadas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `obrassubastadas` (
  `IDObrassubastadas` int NOT NULL,
  `Preciosalida` float NOT NULL,
  `Precioventa` float NOT NULL,
  `MejorPostor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`IDObrassubastadas`),
  CONSTRAINT `ObraSub` FOREIGN KEY (`IDObrassubastadas`) REFERENCES `obras` (`IDObra`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obrassubastadas`
--

LOCK TABLES `obrassubastadas` WRITE;
/*!40000 ALTER TABLE `obrassubastadas` DISABLE KEYS */;
/*!40000 ALTER TABLE `obrassubastadas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puja`
--

DROP TABLE IF EXISTS `puja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puja` (
  `DNI` varchar(9) NOT NULL,
  `IDObra` int NOT NULL,
  `IDSubasta` int NOT NULL,
  `DineroPuja` float NOT NULL,
  PRIMARY KEY (`DNI`,`IDObra`,`IDSubasta`),
  KEY `ObraSubCliente_idx` (`IDObra`),
  KEY `SubClienteObra_idx` (`IDSubasta`),
  CONSTRAINT `ClienteObraSub` FOREIGN KEY (`DNI`) REFERENCES `clientespremium` (`DNI`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ObraSubCliente` FOREIGN KEY (`IDObra`) REFERENCES `obrassubastadas` (`IDObrassubastadas`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `SubClienteObra` FOREIGN KEY (`IDSubasta`) REFERENCES `subastas` (`IDSubasta`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puja`
--

LOCK TABLES `puja` WRITE;
/*!40000 ALTER TABLE `puja` DISABLE KEYS */;
/*!40000 ALTER TABLE `puja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resenas`
--

DROP TABLE IF EXISTS `resenas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resenas` (
  `Numresena` int NOT NULL,
  `IDObra` int NOT NULL,
  `Texto` varchar(1000) NOT NULL,
  `Numestrellas` int NOT NULL,
  `Visible` binary(1) NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`Numresena`,`IDObra`),
  KEY `ObraRese_idx` (`IDObra`),
  CONSTRAINT `ObraRese` FOREIGN KEY (`IDObra`) REFERENCES `obras` (`IDObra`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resenas`
--

LOCK TABLES `resenas` WRITE;
/*!40000 ALTER TABLE `resenas` DISABLE KEYS */;
/*!40000 ALTER TABLE `resenas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salas`
--

DROP TABLE IF EXISTS `salas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salas` (
  `NumSala` int NOT NULL,
  `Capacidad` int NOT NULL,
  `Tematica` varchar(45) NOT NULL,
  `IDMapa` int NOT NULL,
  PRIMARY KEY (`NumSala`),
  KEY `MapSal_idx` (`IDMapa`),
  CONSTRAINT `MapSal` FOREIGN KEY (`IDMapa`) REFERENCES `mapa` (`IDMapa`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salas`
--

LOCK TABLES `salas` WRITE;
/*!40000 ALTER TABLE `salas` DISABLE KEYS */;
/*!40000 ALTER TABLE `salas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios`
--

DROP TABLE IF EXISTS `servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios` (
  `IDServicios` int NOT NULL auto_increment,
  `Nombre` varchar(80) NULL,
  PRIMARY KEY (`IDServicios`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subastas`
--

DROP TABLE IF EXISTS `subastas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subastas` (
  `IDSubasta` int NOT NULL auto_increment,
  `Fecha` date NOT NULL,
  `Titulo` varchar(45) NOT NULL UNIQUE,
  `Descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`IDSubasta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subastas`
--

LOCK TABLES `subastas` WRITE;
/*!40000 ALTER TABLE `subastas` DISABLE KEYS */;
/*!40000 ALTER TABLE `subastas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarifas`
--

DROP TABLE IF EXISTS `tarifas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarifas` (
  `TipoTarifa` varchar(15) NOT NULL,
  `Precio` float DEFAULT NULL,
  `Duracion` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`TipoTarifa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarifas`
--

LOCK TABLES `tarifas` WRITE;
/*!40000 ALTER TABLE `tarifas` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarifas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `DNI` varchar(9) NOT NULL ,
  `UsuNombreCompleto` varchar(50) NOT NULL,
  `Usutfno` varchar(9) NOT NULL,
  `UsuEmail` varchar(50) NOT NULL,
  `UsuTitularMP` varchar(50) NOT NULL,
  `UsuNumTarjMP` varchar(16) NOT NULL,
  `UsuCvvMP` int NOT NULL,
  `UsuCadMP` date NOT NULL,
  `UsuContrasenna` varchar(100) NOT NULL,
  `UsuFecha` date NOT NULL,
  PRIMARY KEY (`DNI`),
  UNIQUE KEY `UQ_UsuEmail` (`UsuEmail`),
  CONSTRAINT `UCMPCHECK` CHECK (((`UsuCvvMP` >= 0) and (`UsuCvvMP` <= 999))),
  CONSTRAINT `UECHECK` CHECK ((`UsuEmail` like _utf8mb4'%@%.com'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ususerv`
--

DROP TABLE IF EXISTS `ususerv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ususerv` (
  `IDUsuario` varchar(9) NOT NULL,
  `IDServicio` int NOT NULL,
  PRIMARY KEY (`IDUsuario`,`IDServicio`),
  KEY `ServUsu_idx` (`IDServicio`),
  CONSTRAINT `ServUsu` FOREIGN KEY (`IDServicio`) REFERENCES `servicios` (`IDServicios`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `UsuServ` FOREIGN KEY (`IDUsuario`) REFERENCES `usuarios` (`DNI`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ususerv`
--

LOCK TABLES `ususerv` WRITE;
/*!40000 ALTER TABLE `ususerv` DISABLE KEYS */;
/*!40000 ALTER TABLE `ususerv` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-03 16:39:04
