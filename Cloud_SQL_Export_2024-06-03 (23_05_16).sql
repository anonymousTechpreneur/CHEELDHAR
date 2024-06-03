-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: shop_data
-- ------------------------------------------------------
-- Server version	8.0.31-google

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `shop_data`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `shop_data` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `shop_data`;

--
-- Table structure for table `Bill`
--

DROP TABLE IF EXISTS `Bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bill` (
  `BillID` int NOT NULL,
  `CustomerId` int DEFAULT NULL,
  `SalesId` int DEFAULT NULL,
  `TotalBillAmount` decimal(10,2) DEFAULT NULL,
  `CashPaidAmount` decimal(10,2) DEFAULT NULL,
  `OnlinePaidAmount` decimal(10,2) DEFAULT NULL,
  `RemainingAmount` decimal(10,2) DEFAULT NULL,
  `BillDateNTime` datetime DEFAULT NULL,
  PRIMARY KEY (`BillID`),
  KEY `CustomerId` (`CustomerId`),
  KEY `SalesId` (`SalesId`),
  CONSTRAINT `Bill_ibfk_1` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`),
  CONSTRAINT `Bill_ibfk_2` FOREIGN KEY (`SalesId`) REFERENCES `Sales` (`SalesId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bill`
--

LOCK TABLES `Bill` WRITE;
/*!40000 ALTER TABLE `Bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `Bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `CustomerId` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `PhoneNumber` varchar(15) DEFAULT NULL,
  `EmailId` varchar(255) DEFAULT NULL,
  `Address` text,
  `GSTNumber` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`CustomerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'Shubham Udsaria','+918694774831','random@gmail.com','Sardarshahar,Rajasthan','AA0000000'),(2,'Ram Prasad','+918694774832','random1@gmail.com','Sardarshahar,Rajasthan','AA0000001'),(3,'Kirodimal chandraprakash mittal','+918694774833','random2@gmail.com','Sardarshahar,Rajasthan','AA0000002'),(4,'Kirodimal Agarwal','+918694774834','random3@gmail.com','Sardarshahar,Rajasthan','AA0000003'),(5,'Kirodimal Agarwal','+918694774835','random4@gmail.com','Sardarshahar,Rajasthan','AA0000004');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Inventory`
--

DROP TABLE IF EXISTS `Inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Inventory` (
  `InventoryID` int NOT NULL,
  `Quantity` int DEFAULT NULL,
  `ManufacturingDate` date DEFAULT NULL,
  `ExpiryDate` date DEFAULT NULL,
  `BillDate` date DEFAULT NULL,
  `HSNNumber` varchar(15) DEFAULT NULL,
  `CostPrice` decimal(10,2) DEFAULT NULL,
  `ExtraCostPrice` decimal(10,2) DEFAULT NULL,
  `MinimumSellingPrice` decimal(10,2) DEFAULT NULL,
  `MaximumSellingPrice` decimal(10,2) DEFAULT NULL,
  `GST_Percentage` decimal(5,2) DEFAULT NULL,
  `PurchaseBillNo` varchar(255) DEFAULT NULL,
  `FirmName` varchar(255) DEFAULT NULL,
  `SupplierId` int DEFAULT NULL,
  `SKU_No` int DEFAULT NULL,
  PRIMARY KEY (`InventoryID`),
  KEY `SKU_No` (`SKU_No`),
  CONSTRAINT `Inventory_ibfk_1` FOREIGN KEY (`SKU_No`) REFERENCES `Product` (`SKU_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inventory`
--

LOCK TABLES `Inventory` WRITE;
/*!40000 ALTER TABLE `Inventory` DISABLE KEYS */;
INSERT INTO `Inventory` VALUES (1,100,'2024-01-28','2024-09-29','2024-02-02','1905',50.00,5.00,60.00,70.00,18.00,'A000001','MM',2,4);
/*!40000 ALTER TABLE `Inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product` (
  `SKU_No` int DEFAULT NULL,
  `Name` varchar(255) NOT NULL,
  `Category` varchar(255) DEFAULT NULL,
  `ProductDescription` text,
  UNIQUE KEY `SKU_No` (`SKU_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (1,'chawal basmati','food','star brand'),(2,'chawal basmati','food','billu brand'),(3,'chawal new','food','billu brand'),(4,'chini','food','local brand'),(5,'sabun','food','local brand'),(6,'sabudana','food','local brand'),(7,'kismis 11','food','local brand'),(8,'kismis','food','local brand'),(9,'senyi','food','local brand'),(10,'Badam Mamra','food','local brand');
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sales`
--

DROP TABLE IF EXISTS `Sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sales` (
  `SalesId` int NOT NULL,
  `SKU_No` int DEFAULT NULL,
  `Qty` int DEFAULT NULL,
  `Discount` decimal(10,2) DEFAULT NULL,
  `SellingPrice` decimal(10,2) DEFAULT NULL,
  `TotalAmount` decimal(10,2) DEFAULT NULL,
  `Firm` varchar(255) DEFAULT NULL,
  `GST_Percentage` decimal(5,2) DEFAULT NULL,
  `TotalGST` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`SalesId`),
  KEY `SKU_No` (`SKU_No`),
  CONSTRAINT `Sales_ibfk_1` FOREIGN KEY (`SKU_No`) REFERENCES `Product` (`SKU_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sales`
--

LOCK TABLES `Sales` WRITE;
/*!40000 ALTER TABLE `Sales` DISABLE KEYS */;
/*!40000 ALTER TABLE `Sales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-03 17:35:41
