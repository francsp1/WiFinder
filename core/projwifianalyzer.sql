-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 03-Maio-2023 às 15:37
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `projwifianalyzer`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `scans`
--

CREATE TABLE `scans` (
  `scanID` int(11) NOT NULL,
  `userID` int(11) DEFAULT NULL,
  `Authentication` varchar(10) NOT NULL,
  `BSSID` varchar(50) NOT NULL,
  `Beacons` int(11) NOT NULL,
  `Cipher` varchar(25) NOT NULL,
  `ESSID` varchar(255) NOT NULL,
  `Lasttimeseen` timestamp NULL DEFAULT NULL,
  `Firsttimeseen` timestamp NULL DEFAULT NULL,
  `IDlength` int(11) NOT NULL,
  `IV` int(11) NOT NULL,
  `LanIP` varchar(255) NOT NULL,
  `Manufacturer` varchar(255) NOT NULL,
  `Power` int(11) NOT NULL,
  `Privacy` varchar(10) NOT NULL,
  `Speed` int(11) NOT NULL,
  `WPSState` varchar(50) NOT NULL,
  `WPSVersion` float NOT NULL,
  `WPSLocked` tinyint(1) NOT NULL,
  `WPSmethod` varchar(50) NOT NULL,
  `Channel` int(11) NOT NULL,
  `Key` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `scans`
--

INSERT INTO `scans` (`scanID`, `userID`, `Authentication`, `BSSID`, `Beacons`, `Cipher`, `ESSID`, `Lasttimeseen`, `Firsttimeseen`, `IDlength`, `IV`, `LanIP`, `Manufacturer`, `Power`, `Privacy`, `Speed`, `WPSState`, `WPSVersion`, `WPSLocked`, `WPSmethod`, `Channel`, `Key`) VALUES
(1, NULL, ' PSK', '6C:06:D6:BB:0E:32', 4, ' CCMP', ' HUAWEI P30 lite', '2023-05-03 13:30:00', '2023-05-03 13:30:00', 15, 0, '   0.  0.  0.  0', ' Huawei Device Co., Ltd.', -52, ' WPA2', 65, ' Unknown', 0, 0, ' ', 11, ' '),
(2, NULL, ' PSK', 'C4:AD:34:9F:52:B9', 10, ' CCMP', ' BKP 2.4Ghz', '2023-05-02 11:05:03', '2023-05-02 11:04:57', 10, 0, '   0.  0.  0.  0', ' Routerboard.com', -36, ' WPA2', 130, ' Waiting for M2', 1, 0, ' PBC', 3, ' '),
(3, NULL, ' PSK', 'E6:A9:B0:9D:F4:74', 5, ' CCMP', ' operatornet', '2023-05-02 11:04:59', '2023-05-02 11:04:57', 11, 41, '   0.  0.  0.  0', ' Unknown', -49, ' WPA2', 180, ' Unknown', 0, 0, ' ', 1, ' '),
(4, NULL, ' PSK', '8E:C8:88:F3:E9:B7', 4, ' CCMP', ' Redmi Note 9S', '2023-05-02 11:04:59', '2023-05-02 11:04:57', 13, 2, '   0.  0.  0.  0', ' Unknown', -45, ' WPA2', 360, ' Unknown', 0, 0, ' ', 1, ' '),
(5, NULL, ' PSK', '3E:12:ED:AE:0B:C3', 0, ' CCMP', ' MigasNetwork', '2023-05-02 11:04:59', '2023-05-02 11:04:57', 12, 0, '   0.  0.  0.  0', ' Unknown', -55, ' WPA2', 65, ' Unknown', 0, 0, ' ', 1, ' '),
(6, NULL, ' PSK', '0A:C5:E1:D7:07:86', 8, ' CCMP', ' EduNet', '2023-05-02 11:05:04', '2023-05-02 11:04:57', 6, 22, '   0.  0.  0.  0', ' Unknown', -39, ' WPA2', 130, ' Unknown', 0, 0, ' ', 6, ' '),
(7, NULL, ' SAE PSK', 'B2:50:E3:30:23:DC', 8, ' CCMP', ' iPhone de Bruno', '2023-05-02 11:05:04', '2023-05-02 11:04:57', 15, 1, '   0.  0.  0.  0', ' Unknown', -68, ' WPA3 WPA2', 130, ' Unknown', 0, 0, ' ', 6, ' '),
(8, NULL, ' PSK', 'AA:78:2C:9F:08:05', 2, ' CCMP', ' AndroidAP2705', '2023-05-02 11:05:01', '2023-05-02 11:04:57', 13, 0, '   0.  0.  0.  0', ' Unknown', -58, ' WPA2', 180, ' Unknown', 0, 0, ' ', 6, ' '),
(9, NULL, ' SAE PSK', '3A:99:2F:72:B7:F0', 1, ' CCMP', ' Sousa’s', '2023-05-02 11:04:57', '2023-05-02 11:04:57', 9, 0, '   0.  0.  0.  0', ' Unknown', -72, ' WPA3 WPA2', 130, ' Not started', 0, 0, ' ', 6, ' '),
(10, NULL, ' PSK', 'E0:DC:FF:10:1C:82', 11, ' CCMP', ' Redme', '2023-05-02 11:05:05', '2023-05-02 11:04:58', 5, 126, '   0.  0.  0.  0', ' Xiaomi Communications Co Ltd', -41, ' WPA2', 180, ' Not started', 0, 0, ' ', 13, ' '),
(11, NULL, ' PSK', 'F6:1E:C0:C6:A4:6F', 7, ' CCMP', ' Pai do Bacalhau ', '2023-05-02 11:05:03', '2023-05-02 11:04:59', 16, 0, '   0.  0.  0.  0', ' Unknown', -70, ' WPA2', 180, ' Unknown', 0, 0, ' ', 6, ' '),
(12, NULL, ' SAE PSK', '5E:84:8C:93:DE:D5', 2, ' CCMP', ' iPhone', '2023-05-02 11:05:03', '2023-05-02 11:04:59', 6, 0, '   0.  0.  0.  0', ' Unknown', -57, ' WPA3 WPA2', 130, ' Unknown', 0, 0, ' ', 6, ' '),
(13, NULL, ' SAE PSK', '62:97:0C:AB:8E:DC', 3, ' CCMP', ' ', '2023-05-02 11:05:04', '2023-05-02 11:04:59', 15, 96, '   0.  0.  0.  0', ' Unknown', -59, ' WPA3 WPA2', 130, ' Not started', 0, 0, ' ', 6, ' '),
(14, NULL, ' SAE PSK', '86:77:1C:94:7B:63', 2, ' CCMP', ' iPhone de Adolfo', '2023-05-02 11:05:04', '2023-05-02 11:05:01', 16, 36, '   0.  0.  0.  0', ' Unknown', -62, ' WPA3 WPA2', 130, ' Unknown', 0, 0, ' ', 6, ' '),
(15, NULL, ' PSK', 'E6:FD:07:FE:E9:D8', 1, ' CCMP', ' Redmi Note 11S 5G', '2023-05-02 11:05:02', '2023-05-02 11:05:02', 17, 0, '   0.  0.  0.  0', ' Unknown', -72, ' WPA2', 180, ' Not started', 0, 0, ' ', 11, ' '),
(16, NULL, ' PSK', 'C4:AD:34:9F:52:BA', 8, ' CCMP', ' BKP 5Ghz', '2023-05-02 11:05:05', '2023-05-02 11:05:05', 8, 0, '   0.  0.  0.  0', ' Routerboard.com', -74, ' WPA2', 360, ' Waiting for M2', 1, 0, ' ', 36, ' '),
(17, NULL, ' PSK', '3A:6A:A5:3F:2B:E7', 7, ' CCMP', ' Crazy Frayzons', '2023-05-02 11:05:05', '2023-05-02 11:05:05', 14, 0, '   0.  0.  0.  0', ' Unknown', -83, ' WPA2', 433, ' Unknown', 0, 0, ' ', 36, ' ');

-- --------------------------------------------------------

--
-- Estrutura da tabela `users`
--

CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `users`
--

INSERT INTO `users` (`userID`, `username`, `password`) VALUES
(1, 'jose.jose', 'jose');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `scans`
--
ALTER TABLE `scans`
  ADD PRIMARY KEY (`scanID`);

--
-- Índices para tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `scans`
--
ALTER TABLE `scans`
  MODIFY `scanID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
