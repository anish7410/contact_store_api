SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;

CREATE TABLE `contact` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `phone_num` varchar(15) DEFAULT NULL,
  `addr` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `contact`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;
