-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 21, 2025 at 09:05 PM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `langchain`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
CREATE TABLE IF NOT EXISTS `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `category` varchar(255) COLLATE utf8mb4_vi_0900_as_cs DEFAULT NULL,
  `price` int NOT NULL DEFAULT '0',
  `description` text COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `feature` text COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `category`, `price`, `description`, `feature`) VALUES
(1, 'Bút bi Thiên Long', 'Bút', 6000, 'Bút bi có hình dáng đẹp, mực khô nhanh', '[\"Nhiều màu sắc\", \"Có nhiều loại vỏ\"]'),
(2, 'Vở 96 trang', 'Sách vở', 5000, 'Vở không lem, dày, chất lượng cao', '[\"Có nhiều loại bìa\", \"Nhiều loại ô ly\"]'),
(3, 'Bút xóa mực nước', 'Bút', 12000, 'Xóa sạch các vết mực, thơm, không gây lem', '[\"Nhiều loại thiết kế\"]'),
(4, 'Thước kẻ 30cm', 'Dụng cụ học tập', 7000, 'Thước nhựa dẻo, không gãy, in số rõ ràng', '[\"Chống gãy\", \"Chống mài mòn\"]'),
(5, 'Tẩy chì học sinh', 'Dụng cụ học tập', 4000, 'Tẩy sạch không lem, ít bụi', '[\"Không độc hại\", \"Hương thơm nhẹ\"]'),
(6, 'Bút chì gỗ 2B', 'Bút', 3000, 'Bút chì viết êm, không gãy ruột', '[\"Gỗ cao cấp\", \"Màu vỏ đa dạng\"]'),
(7, 'Hộp bút đa năng', 'Phụ kiện', 25000, 'Hộp bút có nhiều ngăn, thiết kế tiện lợi', '[\"Chống thấm\", \"Có gương\", \"Khóa kéo chắc chắn\"]'),
(8, 'Compa học sinh', 'Dụng cụ học tập', 15000, 'Compa thép không gỉ, vẽ tròn mượt', '[\"Đi kèm ruột chì\", \"Có hộp đựng\"]'),
(9, 'Bảng viết mini', 'Dụng cụ học tập', 20000, 'Bảng trắng nhỏ cho học sinh tiểu học', '[\"Dễ lau\", \"Có bút và khăn đi kèm\"]'),
(10, 'Bút lông bảng', 'Bút', 8000, 'Bút lông bảng viết êm, mực đều, dễ xóa', '[\"Nhiều màu\", \"Không độc hại\"]'),
(11, 'Vở ô ly 200 trang', 'Sách vở', 10000, 'Vở dày, giấy trắng đẹp, không thấm mực', '[\"Bìa dày\", \"Gáy dán chắc chắn\"]');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
