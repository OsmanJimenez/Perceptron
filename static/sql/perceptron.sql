-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2020 a las 17:29:00
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `perceptron`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_an`
--

CREATE TABLE `compuerta_an` (
  `Patron` int(11) NOT NULL,
  `x1` float NOT NULL,
  `x2` float NOT NULL,
  `p1` float NOT NULL,
  `p2` float NOT NULL,
  `u` float NOT NULL,
  `d` float NOT NULL,
  `y` float NOT NULL,
  `fx` float NOT NULL,
  `n` float NOT NULL,
  `e` float NOT NULL,
  `v1` float NOT NULL,
  `v2` float NOT NULL,
  `pe1` float NOT NULL,
  `pe2` float NOT NULL,
  `um` float NOT NULL,
  `it` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_or`
--

CREATE TABLE `compuerta_or` (
  `Patron` int(11) NOT NULL,
  `x1` int(11) NOT NULL,
  `x2` int(11) NOT NULL,
  `p1` float NOT NULL,
  `p2` float NOT NULL,
  `u` float NOT NULL,
  `d` float NOT NULL,
  `y` float NOT NULL,
  `fx` float NOT NULL,
  `n` float NOT NULL,
  `e` float NOT NULL,
  `v1` float NOT NULL,
  `v2` float NOT NULL,
  `pe1` float NOT NULL,
  `pe2` float NOT NULL,
  `um` float NOT NULL,
  `it` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
