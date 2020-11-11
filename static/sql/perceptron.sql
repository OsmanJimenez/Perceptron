-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-11-2020 a las 18:09:02
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Estructura de tabla para la tabla `compuerta_an2`
--

CREATE TABLE `compuerta_an2` (
  `Patron` int(11) NOT NULL,
  `x1` float NOT NULL,
  `x2` float NOT NULL,
  `x3` float NOT NULL,
  `p1` float NOT NULL,
  `p2` float NOT NULL,
  `p3` float NOT NULL,
  `u` float NOT NULL,
  `d` float NOT NULL,
  `y` float NOT NULL,
  `fx` float NOT NULL,
  `n` float NOT NULL,
  `e` float NOT NULL,
  `v1` float NOT NULL,
  `v2` float NOT NULL,
  `v3` float NOT NULL,
  `pe1` float NOT NULL,
  `pe2` float NOT NULL,
  `pe3` float NOT NULL,
  `um` float NOT NULL,
  `it` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_nan`
--

CREATE TABLE `compuerta_nan` (
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_nan2`
--

CREATE TABLE `compuerta_nan2` (
  `Patron` int(11) NOT NULL,
  `x1` int(11) NOT NULL,
  `x2` int(11) NOT NULL,
  `x3` int(11) NOT NULL,
  `p1` float NOT NULL,
  `p2` float NOT NULL,
  `p3` float NOT NULL,
  `u` float NOT NULL,
  `d` float NOT NULL,
  `y` float NOT NULL,
  `fx` float NOT NULL,
  `n` float NOT NULL,
  `e` float NOT NULL,
  `v1` float NOT NULL,
  `v2` float NOT NULL,
  `v3` float NOT NULL,
  `pe1` float NOT NULL,
  `pe2` float NOT NULL,
  `pe3` float NOT NULL,
  `um` float NOT NULL,
  `it` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_nor`
--

CREATE TABLE `compuerta_nor` (
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_nor2`
--

CREATE TABLE `compuerta_nor2` (
  `Patron` int(11) NOT NULL,
  `x1` int(11) NOT NULL,
  `x2` int(11) NOT NULL,
  `x3` int(11) NOT NULL,
  `p1` float NOT NULL,
  `p2` float NOT NULL,
  `p3` float NOT NULL,
  `u` float NOT NULL,
  `d` float NOT NULL,
  `y` float NOT NULL,
  `fx` float NOT NULL,
  `n` float NOT NULL,
  `e` float NOT NULL,
  `v1` float NOT NULL,
  `v2` float NOT NULL,
  `v3` float NOT NULL,
  `pe1` float NOT NULL,
  `pe2` float NOT NULL,
  `pe3` float NOT NULL,
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_or2`
--

CREATE TABLE `compuerta_or2` (
  `Patron` int(11) NOT NULL,
  `x1` int(11) NOT NULL,
  `x2` int(11) NOT NULL,
  `x3` float NOT NULL,
  `p1` float NOT NULL,
  `p2` float NOT NULL,
  `p3` float NOT NULL,
  `u` float NOT NULL,
  `d` float NOT NULL,
  `y` float NOT NULL,
  `fx` float NOT NULL,
  `n` float NOT NULL,
  `e` float NOT NULL,
  `v1` float NOT NULL,
  `v2` float NOT NULL,
  `v3` float NOT NULL,
  `pe1` float NOT NULL,
  `pe2` float NOT NULL,
  `pe3` float NOT NULL,
  `um` float NOT NULL,
  `it` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_xor`
--

CREATE TABLE `compuerta_xor` (
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compuerta_xor2`
--

CREATE TABLE `compuerta_xor2` (
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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
