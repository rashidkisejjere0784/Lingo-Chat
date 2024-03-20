-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 20, 2024 at 08:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lingo_chat`
--

-- --------------------------------------------------------

--
-- Table structure for table `messages_22_23`
--

CREATE TABLE `messages_22_23` (
  `id` int(11) NOT NULL,
  `sender_id` int(255) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `src_lang` varchar(10) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `messages_22_23`
--

INSERT INTO `messages_22_23` (`id`, `sender_id`, `content`, `src_lang`, `timestamp`) VALUES
(1, 22, '   ', 'en', '2024-03-16 22:35:25'),
(2, 22, '   ', 'en', '2024-03-16 22:36:13'),
(3, 22, 'todays meaning was okay', 'en', '2024-03-16 22:37:54'),
(4, 22, 'sorry i meant meeting', 'en', '2024-03-16 22:39:45'),
(5, 23, 'oooh kale nange mbadde neewunyiza', 'lg', '2024-03-16 22:40:30'),
(6, 23, 'oooh kale, nange mbadde neewunyiza', 'lg', '2024-03-16 22:40:59'),
(7, 22, 'hehe okay good thing you get it', 'en', '2024-03-16 22:41:38'),
(8, 23, 'nayenga oli otya mukwano', 'lg', '2024-03-16 22:42:47'),
(9, 22, 'well am definitely trying to be better ', 'en', '2024-03-16 22:43:28'),
(10, 23, 'kale, sula bulungi dear', 'lg', '2024-03-16 22:44:15'),
(11, 22, 'you too dear', 'en', '2024-03-16 22:44:39'),
(12, 22, 'good morning', 'sw', '2024-03-17 08:51:07');

-- --------------------------------------------------------

--
-- Table structure for table `messages_22_24`
--

CREATE TABLE `messages_22_24` (
  `id` int(11) NOT NULL,
  `sender_id` int(255) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `src_lang` varchar(10) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `messages_22_24`
--

INSERT INTO `messages_22_24` (`id`, `sender_id`, `content`, `src_lang`, `timestamp`) VALUES
(1, 24, 'hello', 'en', '2024-03-16 21:52:28'),
(2, 24, 'hello', 'nl', '2024-03-16 21:54:09'),
(3, 24, 'hello my name is rashid', 'nl', '2024-03-16 21:54:22'),
(4, 24, 'hello my name is rashid', 'lg', '2024-03-16 21:56:15'),
(5, 24, 'wasibye otya', 'lg', '2024-03-16 21:56:35'),
(6, 24, 'hi', 'en', '2024-03-16 22:05:28'),
(7, 22, 'hey, sorry for taking long to respond but how are you', 'en', '2024-03-16 22:08:15'),
(8, 24, 'ndi bulungi naye mpulila obulwadde', 'lg', '2024-03-16 22:08:52'),
(9, 22, 'sorry mukwano', 'lg', '2024-03-17 08:54:34'),
(10, 22, 'hello', 'en', '2024-03-18 11:28:58'),
(11, 24, 'jebaleko', 'lg', '2024-03-18 11:29:15');

-- --------------------------------------------------------

--
-- Table structure for table `messages_22_25`
--

CREATE TABLE `messages_22_25` (
  `id` int(11) NOT NULL,
  `sender_id` int(255) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `src_lang` varchar(10) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `messages_23_24`
--

CREATE TABLE `messages_23_24` (
  `id` int(11) NOT NULL,
  `sender_id` int(255) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `src_lang` varchar(10) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(255) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(22, 'Rashid ', 'rashid@gmail.com', '9090'),
(23, 'Kisejjere', 'rashidkiss@gmail.com', '123456'),
(24, 'John', 'john@gmail.com', '9090'),
(25, 'Rodgers', 'rodgers@gmail.com', '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `messages_22_23`
--
ALTER TABLE `messages_22_23`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `messages_22_24`
--
ALTER TABLE `messages_22_24`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `messages_22_25`
--
ALTER TABLE `messages_22_25`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `messages_23_24`
--
ALTER TABLE `messages_23_24`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `messages_22_23`
--
ALTER TABLE `messages_22_23`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `messages_22_24`
--
ALTER TABLE `messages_22_24`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `messages_22_25`
--
ALTER TABLE `messages_22_25`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `messages_23_24`
--
ALTER TABLE `messages_23_24`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
