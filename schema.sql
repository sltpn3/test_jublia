-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 09, 2019 at 11:52 AM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `jublia2`
--

-- --------------------------------------------------------

--
-- Table structure for table `email`
--

CREATE TABLE `email` (
  `id` int(11) NOT NULL,
  `email` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `email_event`
--

CREATE TABLE `email_event` (
  `email_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `email_to_send`
--

CREATE TABLE `email_to_send` (
  `id` int(11) NOT NULL,
  `event_id` int(11) DEFAULT NULL,
  `email_subject` varchar(256) CHARACTER SET utf8mb4 DEFAULT NULL,
  `email_content` text CHARACTER SET utf8mb4,
  `timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `id` int(11) NOT NULL,
  `event_name` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `email`
--
ALTER TABLE `email`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `email_event`
--
ALTER TABLE `email_event`
  ADD PRIMARY KEY (`email_id`,`event_id`),
  ADD KEY `event_id` (`event_id`);

--
-- Indexes for table `email_to_send`
--
ALTER TABLE `email_to_send`
  ADD PRIMARY KEY (`id`),
  ADD KEY `event_id` (`event_id`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `email`
--
ALTER TABLE `email`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `email_to_send`
--
ALTER TABLE `email_to_send`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `email_event`
--
ALTER TABLE `email_event`
  ADD CONSTRAINT `email_event_ibfk_1` FOREIGN KEY (`email_id`) REFERENCES `email` (`id`),
  ADD CONSTRAINT `email_event_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`);

--
-- Constraints for table `email_to_send`
--
ALTER TABLE `email_to_send`
  ADD CONSTRAINT `email_to_send_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`);
