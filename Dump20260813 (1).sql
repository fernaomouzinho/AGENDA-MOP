-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: smartv04_agenda
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'admin'),(3,'gp_ass'),(4,'gp_che'),(2,'gp_min'),(5,'gp_sec');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(53,1,53),(54,1,54),(55,1,55),(56,1,56),(57,1,57),(58,1,58),(59,1,59),(60,1,60),(61,1,61),(62,1,62),(63,1,63),(64,1,64),(65,1,65),(66,1,66),(67,1,67),(68,1,68),(69,1,69),(70,1,70),(71,1,71),(72,1,72),(73,1,73),(74,1,74),(75,1,75),(76,1,76),(77,1,77),(78,1,78),(79,1,79),(80,1,80),(81,1,81),(82,1,82),(83,1,83),(84,1,84);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add attendence',7,'add_attendence'),(26,'Can change attendence',7,'change_attendence'),(27,'Can delete attendence',7,'delete_attendence'),(28,'Can view attendence',7,'view_attendence'),(29,'Can add institution',8,'add_institution'),(30,'Can change institution',8,'change_institution'),(31,'Can delete institution',8,'delete_institution'),(32,'Can view institution',8,'view_institution'),(33,'Can add unit adn',9,'add_unitadn'),(34,'Can change unit adn',9,'change_unitadn'),(35,'Can delete unit adn',9,'delete_unitadn'),(36,'Can view unit adn',9,'view_unitadn'),(37,'Can add department adn',10,'add_departmentadn'),(38,'Can change department adn',10,'change_departmentadn'),(39,'Can delete department adn',10,'delete_departmentadn'),(40,'Can view department adn',10,'view_departmentadn'),(41,'Can add agenda',11,'add_agenda'),(42,'Can change agenda',11,'change_agenda'),(43,'Can delete agenda',11,'delete_agenda'),(44,'Can view agenda',11,'view_agenda'),(45,'Can add comment informative',12,'add_commentinformative'),(46,'Can change comment informative',12,'change_commentinformative'),(47,'Can delete comment informative',12,'delete_commentinformative'),(48,'Can view comment informative',12,'view_commentinformative'),(49,'Can add informative',13,'add_informative'),(50,'Can change informative',13,'change_informative'),(51,'Can delete informative',13,'delete_informative'),(52,'Can view informative',13,'view_informative'),(53,'Can add yearagenda',14,'add_yearagenda'),(54,'Can change yearagenda',14,'change_yearagenda'),(55,'Can delete yearagenda',14,'delete_yearagenda'),(56,'Can view yearagenda',14,'view_yearagenda'),(57,'Can add hist agenda',15,'add_histagenda'),(58,'Can change hist agenda',15,'change_histagenda'),(59,'Can delete hist agenda',15,'delete_histagenda'),(60,'Can view hist agenda',15,'view_histagenda'),(61,'Can add cat agenda',16,'add_catagenda'),(62,'Can change cat agenda',16,'change_catagenda'),(63,'Can delete cat agenda',16,'delete_catagenda'),(64,'Can view cat agenda',16,'view_catagenda'),(65,'Can add request agenda',17,'add_requestagenda'),(66,'Can change request agenda',17,'change_requestagenda'),(67,'Can delete request agenda',17,'delete_requestagenda'),(68,'Can view request agenda',17,'view_requestagenda'),(69,'Can add semestral',18,'add_semestral'),(70,'Can change semestral',18,'change_semestral'),(71,'Can delete semestral',18,'delete_semestral'),(72,'Can view semestral',18,'view_semestral'),(73,'Can add trimestral',19,'add_trimestral'),(74,'Can change trimestral',19,'change_trimestral'),(75,'Can delete trimestral',19,'delete_trimestral'),(76,'Can view trimestral',19,'view_trimestral'),(77,'Can add mensual',20,'add_mensual'),(78,'Can change mensual',20,'change_mensual'),(79,'Can delete mensual',20,'delete_mensual'),(80,'Can view mensual',20,'view_mensual'),(81,'Can add logo',21,'add_logo'),(82,'Can change logo',21,'change_logo'),(83,'Can delete logo',21,'delete_logo'),(84,'Can view logo',21,'view_logo'),(85,'Can add type agenda',22,'add_typeagenda'),(86,'Can change type agenda',22,'change_typeagenda'),(87,'Can delete type agenda',22,'delete_typeagenda'),(88,'Can view type agenda',22,'view_typeagenda'),(89,'Can add attachment',23,'add_attachment'),(90,'Can change attachment',23,'change_attachment'),(91,'Can delete attachment',23,'delete_attachment'),(92,'Can view attachment',23,'view_attachment'),(93,'Can add Agenda WhatsApp Recipient',24,'add_agendawhatsapprecipient'),(94,'Can change Agenda WhatsApp Recipient',24,'change_agendawhatsapprecipient'),(95,'Can delete Agenda WhatsApp Recipient',24,'delete_agendawhatsapprecipient'),(96,'Can view Agenda WhatsApp Recipient',24,'view_agendawhatsapprecipient'),(97,'Can add Agenda Notification',25,'add_agendanotification'),(98,'Can change Agenda Notification',25,'change_agendanotification'),(99,'Can delete Agenda Notification',25,'delete_agendanotification'),(100,'Can view Agenda Notification',25,'view_agendanotification'),(101,'Can add agenda recipient',26,'add_agendarecipient'),(102,'Can change agenda recipient',26,'change_agendarecipient'),(103,'Can delete agenda recipient',26,'delete_agendarecipient'),(104,'Can view agenda recipient',26,'view_agendarecipient');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_user`
--

DROP TABLE IF EXISTS `authentication_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_adj` tinyint(1) NOT NULL,
  `is_dei` tinyint(1) NOT NULL,
  `is_media` tinyint(1) NOT NULL,
  `is_secretary` tinyint(1) NOT NULL,
  `is_uap` tinyint(1) NOT NULL,
  `is_ucvq` tinyint(1) NOT NULL,
  `is_uedc` tinyint(1) NOT NULL,
  `is_uga` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_user`
--

LOCK TABLES `authentication_user` WRITE;
/*!40000 ALTER TABLE `authentication_user` DISABLE KEYS */;
INSERT INTO `authentication_user` VALUES (1,'pbkdf2_sha256$870000$KHqVzcnJQBom12jVBtShtx$sdzaT5cNh++pJufpq2TEWN9Cu1FjvQfU0LmloF4Dhmg=','2026-04-19 20:00:38.447104',1,'admin','','','admin@gmail.com',1,1,'2025-03-24 15:25:41.000000',0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `authentication_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_user_groups`
--

DROP TABLE IF EXISTS `authentication_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authentication_user_groups_user_id_group_id_8af031ac_uniq` (`user_id`,`group_id`),
  KEY `authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id` (`group_id`),
  CONSTRAINT `authentication_user__user_id_30868577_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`),
  CONSTRAINT `authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_user_groups`
--

LOCK TABLES `authentication_user_groups` WRITE;
/*!40000 ALTER TABLE `authentication_user_groups` DISABLE KEYS */;
INSERT INTO `authentication_user_groups` VALUES (1,1,1);
/*!40000 ALTER TABLE `authentication_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_user_user_permissions`
--

DROP TABLE IF EXISTS `authentication_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authentication_user_user_user_id_permission_id_ec51b09f_uniq` (`user_id`,`permission_id`),
  KEY `authentication_user__permission_id_ea6be19a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `authentication_user__permission_id_ea6be19a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `authentication_user__user_id_736ebf7e_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_user_user_permissions`
--

LOCK TABLES `authentication_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `authentication_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `authentication_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_authentication_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-03-24 15:29:59.426363','1','admin',1,'[{\"added\": {}}]',3,1),(2,'2025-03-24 15:30:08.030558','2','gp_min',1,'[{\"added\": {}}]',3,1),(3,'2025-03-24 15:30:15.442066','3','gp_ass',1,'[{\"added\": {}}]',3,1),(4,'2025-03-24 15:30:21.696949','4','gp_che',1,'[{\"added\": {}}]',3,1),(5,'2025-03-24 15:30:29.071443','5','gp_sec',1,'[{\"added\": {}}]',3,1),(6,'2025-03-24 15:30:45.449631','1','admin',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',6,1),(7,'2025-03-24 16:19:05.557359','1','2025',1,'[{\"added\": {}}]',14,1),(8,'2025-03-24 16:36:30.793988','1','Logo object (1)',1,'[{\"added\": {}}]',21,1),(9,'2025-03-28 15:04:16.418730','1','Enkontru',1,'[{\"added\": {}}]',22,1),(10,'2025-03-28 15:04:31.334667','2','Lansamentu',1,'[{\"added\": {}}]',22,1),(11,'2026-03-23 10:00:27.912123','2','2026',1,'[{\"added\": {}}]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(6,'authentication','user'),(4,'contenttypes','contenttype'),(23,'django_summernote','attachment'),(11,'event','agenda'),(25,'event','agendanotification'),(26,'event','agendarecipient'),(24,'event','agendawhatsapprecipient'),(16,'event','catagenda'),(12,'event','commentinformative'),(15,'event','histagenda'),(13,'event','informative'),(17,'event','requestagenda'),(22,'event','typeagenda'),(14,'event','yearagenda'),(7,'institute','attendence'),(10,'institute','departmentadn'),(8,'institute','institution'),(9,'institute','unitadn'),(21,'reports','logo'),(20,'reports','mensual'),(18,'reports','semestral'),(19,'reports','trimestral'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-03-24 15:25:05.805934'),(2,'contenttypes','0002_remove_content_type_name','2025-03-24 15:25:05.888729'),(3,'auth','0001_initial','2025-03-24 15:25:06.035333'),(4,'auth','0002_alter_permission_name_max_length','2025-03-24 15:25:06.098717'),(5,'auth','0003_alter_user_email_max_length','2025-03-24 15:25:06.103718'),(6,'auth','0004_alter_user_username_opts','2025-03-24 15:25:06.113717'),(7,'auth','0005_alter_user_last_login_null','2025-03-24 15:25:06.120808'),(8,'auth','0006_require_contenttypes_0002','2025-03-24 15:25:06.124716'),(9,'auth','0007_alter_validators_add_error_messages','2025-03-24 15:25:06.132900'),(10,'auth','0008_alter_user_username_max_length','2025-03-24 15:25:06.138892'),(11,'auth','0009_alter_user_last_name_max_length','2025-03-24 15:25:06.142900'),(12,'auth','0010_alter_group_name_max_length','2025-03-24 15:25:06.158307'),(13,'auth','0011_update_proxy_permissions','2025-03-24 15:25:06.164294'),(14,'auth','0012_alter_user_first_name_max_length','2025-03-24 15:25:06.172309'),(15,'authentication','0001_initial','2025-03-24 15:25:06.365751'),(16,'admin','0001_initial','2025-03-24 15:25:06.434067'),(17,'admin','0002_logentry_remove_auto_add','2025-03-24 15:25:06.442033'),(18,'admin','0003_logentry_add_action_flag_choices','2025-03-24 15:25:06.452033'),(19,'authentication','0002_alter_user_is_media_alter_user_is_secretary','2025-03-24 15:25:06.476113'),(20,'authentication','0003_remove_user_is_adj_remove_user_is_dei_and_more','2025-03-24 15:25:06.789227'),(21,'authentication','0004_user_is_adj_user_is_dei_user_is_media_and_more','2025-03-24 15:25:07.298286'),(22,'institute','0001_initial','2025-03-24 15:25:07.321855'),(23,'institute','0002_rename_name_institution_invitedinstitute_name_institute','2025-03-24 15:25:07.341854'),(24,'institute','0003_invitedas','2025-03-24 15:25:07.358849'),(25,'institute','0004_rename_invitedas_attencence_and_more','2025-03-24 15:25:07.396668'),(26,'institute','0005_rename_attencence_attendence','2025-03-24 15:25:07.417678'),(27,'institute','0006_alter_attendence_options_and_more','2025-03-24 15:25:07.422903'),(28,'institute','0007_alter_attendence_options_and_more','2025-03-24 15:25:07.426910'),(29,'event','0001_initial','2025-03-24 15:25:07.490880'),(30,'event','0002_agenda_commentinformative_informative_yearagenda_and_more','2025-03-24 15:25:07.767266'),(31,'event','0003_agenda_location_alter_commentinformative_comment','2025-03-24 15:25:07.807033'),(32,'event','0004_invitedinstitue_remove_agenda_description_and_more','2025-03-24 15:25:07.924283'),(33,'event','0005_rename_invitedinstitue_invitedinstitute','2025-03-24 15:25:08.045101'),(34,'event','0006_alter_agenda_options','2025-03-24 15:25:08.052980'),(35,'event','0007_alter_agenda_options_remove_agenda_invitedinstitue','2025-03-24 15:25:08.157977'),(36,'event','0008_alter_invitedinstitute_id','2025-03-24 15:25:08.187976'),(37,'event','0009_agenda_invitedinstitue_alter_invitedinstitute_id','2025-03-24 15:25:08.431782'),(38,'event','0010_alter_invitedinstitute_name_institution','2025-03-24 15:25:08.438864'),(39,'event','0011_alter_invitedinstitute_options','2025-03-24 15:25:08.446778'),(40,'event','0012_remove_agenda_invitedinstitue_and_more','2025-03-24 15:25:08.557374'),(41,'event','0013_agenda_invitedinstitue','2025-03-24 15:25:08.625745'),(42,'event','0014_agenda_attendence','2025-03-24 15:25:08.713488'),(43,'event','0015_rename_active_commentinformative_is_active','2025-03-24 15:25:08.730355'),(44,'event','0016_alter_commentinformative_is_active','2025-03-24 15:25:08.739353'),(45,'event','0017_remove_informative_description','2025-03-24 15:25:08.771438'),(46,'event','0018_agenda_status','2025-03-24 15:25:08.819843'),(47,'event','0019_agenda_observation','2025-03-24 15:25:08.850076'),(48,'event','0020_alter_agenda_attendence_alter_agenda_invitedinstitue_and_more','2025-03-24 15:25:08.943255'),(49,'event','0021_alter_histagenda_options_remove_histagenda_agenda_and_more','2025-03-24 15:25:09.619469'),(50,'event','0022_alter_agenda_location_alter_agenda_observation_and_more','2025-03-24 15:25:09.771618'),(51,'event','0023_remove_agenda_invitedinstitue_and_more','2025-03-24 15:25:09.963550'),(52,'institute','0008_institution_delete_invitedinstitute','2025-03-24 15:25:09.992030'),(53,'institute','0009_alter_institution_name_institution','2025-03-24 15:25:09.998032'),(54,'institute','0010_alter_institution_name_institution','2025-03-24 15:25:10.002028'),(55,'institute','0011_unitadn_departmentadn','2025-03-24 15:25:10.071750'),(56,'institute','0012_alter_departmentadn_options_alter_unitadn_options','2025-03-24 15:25:10.076747'),(57,'institute','0013_alter_attendence_options_alter_institution_options_and_more','2025-03-24 15:25:10.088749'),(58,'event','0024_agenda_institution_histagenda_institution','2025-03-24 15:25:10.258880'),(59,'event','0025_catagenda','2025-03-24 15:25:10.311163'),(60,'event','0026_agenda_catagenda','2025-03-24 15:25:10.411787'),(61,'event','0027_alter_agenda_observation_alter_agenda_status','2025-03-24 15:25:10.593699'),(62,'event','0028_remove_commentinformative_comment_and_more','2025-03-24 15:25:10.762225'),(63,'event','0029_commentinformative_is_done','2025-03-24 15:25:10.809008'),(64,'event','0030_commentinformative_is_comment','2025-03-24 15:25:10.851849'),(65,'event','0031_remove_commentinformative_is_comment_and_more','2025-03-24 15:25:10.923864'),(66,'event','0032_remove_commentinformative_is_done','2025-03-24 15:25:10.944515'),(67,'event','0033_requestagenda','2025-03-24 15:25:11.030529'),(68,'event','0034_rename_updated_at_requestagenda_aproved_at_and_more','2025-03-24 15:25:11.080732'),(69,'event','0035_remove_requestagenda_status_requestagenda_is_approve_and_more','2025-03-24 15:25:11.151807'),(70,'event','0036_rename_aproved_at_requestagenda_approved_at','2025-03-24 15:25:11.181974'),(71,'event','0037_alter_requestagenda_options_and_more','2025-03-24 15:25:11.876151'),(72,'event','0038_alter_requestagenda_options_histagenda_catagenda_and_more','2025-03-24 15:25:12.146290'),(73,'event','0039_alter_histagenda_id','2025-03-24 15:25:12.228938'),(74,'event','0040_catagenda_name_category_slug','2025-03-24 15:25:12.292946'),(75,'event','0041_alter_agenda_observation','2025-03-24 15:25:12.306960'),(76,'event','0042_alter_agenda_options_alter_catagenda_options_and_more','2025-03-24 15:25:12.480036'),(77,'event','0043_alter_agenda_end_time_alter_agenda_location_and_more','2025-03-24 15:25:12.530891'),(78,'event','0044_agenda_meeting_type_alter_agenda_end_time','2025-03-24 15:25:12.630919'),(79,'event','0045_histagenda_meeting_type','2025-03-24 15:25:12.717872'),(80,'event','0046_remove_histagenda_meeting_type','2025-03-24 15:25:12.788851'),(81,'event','0047_alter_agenda_meeting_type','2025-03-24 15:25:12.836530'),(82,'event','0048_alter_agenda_observation','2025-03-24 15:25:12.850528'),(83,'event','0049_alter_agenda_observation','2025-03-24 15:25:12.863946'),(84,'event','0050_alter_agenda_observation','2025-03-24 15:25:12.933805'),(85,'event','0051_histagenda_meeting_type','2025-03-24 15:25:12.990728'),(86,'reports','0001_initial','2025-03-24 15:25:13.061451'),(87,'reports','0002_mensual','2025-03-24 15:25:13.102470'),(88,'reports','0003_alter_mensual_options','2025-03-24 15:25:13.106451'),(89,'reports','0004_logo','2025-03-24 15:25:13.128496'),(90,'reports','0005_alter_logo_options','2025-03-24 15:25:13.133496'),(91,'sessions','0001_initial','2025-03-24 15:25:13.172500'),(92,'event','0052_typeagenda','2025-03-28 14:51:14.190024'),(93,'event','0053_alter_agenda_meeting_type','2025-03-28 14:53:38.819186'),(94,'event','0054_agenda_attachment','2025-05-27 14:55:25.195619'),(95,'django_summernote','0001_initial','2025-05-27 15:24:53.256036'),(96,'django_summernote','0002_update-help_text','2025-05-27 15:24:53.260689'),(97,'django_summernote','0003_alter_attachment_id','2026-03-23 10:36:28.895256'),(98,'event','0055_alter_yearagenda_year','2026-03-23 10:36:28.897269'),(99,'event','0056_remove_agenda_user','2026-08-11 11:40:09.341106'),(100,'event','0057_remove_commentinformative_user_and_more','2026-08-11 16:21:17.014215'),(101,'event','0058_alter_histagenda_title','2026-08-11 16:22:57.470545'),(102,'event','0059_alter_histagenda_title_slug','2026-08-11 16:24:18.090328'),(103,'event','0060_agendawhatsapprecipient_agendanotification','2026-08-12 10:14:37.404658'),(104,'event','0061_alter_agendawhatsapprecipient_options_and_more','2026-08-12 05:20:10.408426'),(105,'event','0062_remove_agendawhatsapprecipient_agenda_and_more','2026-08-12 05:29:38.666369'),(106,'event','0063_agendarecipient_agendanotification','2026-08-12 12:14:09.239155'),(107,'event','0064_alter_agendarecipient_options_and_more','2026-08-12 13:45:11.432134'),(108,'event','0065_alter_agendanotification_reminder_type','2026-08-12 13:47:54.987288'),(109,'event','0066_alter_agendanotification_reminder_type','2026-08-13 01:15:31.442922');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2k8hcsgpyxm3pihsjokxfz932473oujc','.eJxdUNtugzAM_Rc_80BLQ0J-ZZoil7jDDBIUh27T1H9vaCWq7ck-N_nyCyLR4ZoHCpl7zOTB5rRSBfhBwaNbhZLjwh6OxvxhwQL6mYMwz3GBXUtxIgH7BkOaxT0sRSyuvV9iyjj9hzN5xhfc0i_kwybh-JjwDL5XMH5lN2Yum1DbGrqcjWl9fzqY7qw1KlWfSDdolLrA0ywkwjG4K6Wtgm3qCiaUopQ_9AP1n-VSbVrV6GPXVbAn6Hvh9AO2fKGub3fYbWpT:1wu7xj:H45uE3c370DseMa7K6BIU2VDRBS1xBgqZb03QffR2WM','2026-08-12 20:21:39.942806'),('70fnml231knk1lmfc9hx5sqqq5udkgfn','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1wEPtG:UxjndwWTGRHx-Fglf444eeDL52XYxen9sGGK4f1KD4g','2026-05-03 20:00:38.450093'),('9qvh994c46kd173sus0q9xe942sk0vzw','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1u22YJ:dBFm1pVYBKLCp717QHjtyICgIK_k5BUJ585Rrcwz0k0','2025-04-22 15:35:19.821190'),('ac6mprnzeomal212lc4m32tabdfvrr4a','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1twbGR:wDSuPhIdTfLm6TNpmdn33-I8xuNLzkXr3A1SPbZGPmg','2025-04-07 15:26:23.295618'),('g13kn3ijm6c8zac3snlf91eszphver1r','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1uJnEA:b1buLsLVz1qt5oLPQkNkFaWguL238hParc_ZYX9pxJ0','2025-06-10 14:51:54.813441'),('jurd2n1rx1uji6l6i3u0dy8493q8mvy6','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1wEPE1:7dflDpirfaoMDu0-yBy2EWJlO1jacKSzPlWECli73SU','2026-05-03 19:18:01.078941'),('mabq4x4q3cypbaq2doo67835wz8ojitc','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1u3sSr:3dKXrK9AXZtVrqqk-6hz7rowTJiblElP-9fovGjn1oo','2025-04-27 17:13:17.410424'),('npex1tzm7drvzbujr0c0z38536bypv54','.eJxdUMmOgzAM_RefOYQptCG_UlWRSZwSBhIUh1lU9d8bWolq5mS_TV5uwBw1rnmgkL3BTBZUTitVgFcKFvXKlLQvbP0h5R8WFKCdfWDv57jArqU4EYM6w5Bm1k9LEYtr75eYMk7_4UzW4xtu6TeyYZNwfE54BS8VjN9Zj9mXTUzX1EY411ojm6Pr-4MRSG3tenuS5Gp4mZmYfQz6i9JWQR1EBRNyUcofzEDms1x6kse265q23Lsn6Gfx6RdU-YIQ9wczOmtZ:1wuO8I:4SQ6vz4ouvh6UBOwD-4Q5pXaAyIiVejhFfARueAgvDk','2026-08-13 13:37:38.282786'),('qhrd47quy523n8ejml2bt62bh7l5lfl4','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1w4TfE:fCPJmzGDcZ3J_06z7Vrp72S3Tf5KgTjNVD_TpJx5bHU','2026-04-06 10:01:04.330589'),('qnchulji5wndpzyxcsujxrs6fogv0bz0','.eJxdUEmuwjAMvYvXXYROlFzl6ysyjUtd2qSKUwYh7k4KEghW9pss2zcQ8QaX2JOL3GIkCzqGhTLAAzmLZhEKhhO7yZvmiwUNaCd2wjz5Gd5a8CMJ6D_owyTGHpKSLObpTf3sQ8TxF05kGT9wjX6QdauEw3P8K_ifwXCOZoic1sjrbtPZqilUW5S42-9qte3yoi4tYYXlFl5mIRH2zpworBV0lcGIkoT0g7an9ghaZfD20WXmcAWdDlfq_gBrr2bj:1wFGyG:UFyu4IVzqVAoWBkRdT3r3q8NLDXkz0E995dBQ_MW1kA','2026-04-22 12:41:20.578430'),('sk2tl8qtmn2zkqzcj4aqhnat1vbfd7ci','.eJxdUNtugzAM_Rc_85BQRgO_Mk2RSdxhBgmKw7aq2r8vtBLV9mSfm3y5gUi0uOWRQmaHmTz0OW1UAb5T8Gg3oWS5sLo25g8LPaBfOAjzElc4tBRnEuhfYUyL2LuliMV19GtMGef_cCHP-IR7-ol82CWc7hMewbcKpq9sp8xlE-OM6nT3ooaTbgZUg9bdRZFv2uHiTk7BwywkwjHYT0p7hb5uK5hRilL-4EZyH-XSs2mbpq3PqoIjQd8rp2sJGKPUzy_MmWpL:1wtkHq:-q2cQj1kDN9d4rJ2zuc-JG0WlEEyiBNBF3OYcLlKzM0','2026-08-12 04:04:50.266203'),('zazixb383wo3396dv6qruywkxwqs3n0q','.eJxVjMEOgkAMRP9lz2ZDrSxdj975BtLSIqjZTVg4Gf9dSDjoaZJ5b-btOl6XsVuLzd2k7urAnX474f5paQf64HTPvs9pmSfxu-IPWnyb1V63w_07GLmM21pIwhnBIChwHQPxFgh9oNpUm1gxKdogUiMT43AxgghNhAqRQSr3-QLeCzeT:1ty397:BktsgCmRiZR0J8MDcfB6Oc5-7eseT5NAVT31-rLBzR4','2025-04-11 15:24:49.453942');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_summernote_attachment`
--

DROP TABLE IF EXISTS `django_summernote_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_summernote_attachment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_summernote_attachment`
--

LOCK TABLES `django_summernote_attachment` WRITE;
/*!40000 ALTER TABLE `django_summernote_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_summernote_attachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_agenda`
--

DROP TABLE IF EXISTS `event_agenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_agenda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `title_slug` varchar(255) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `is_cancel` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` varchar(20) NOT NULL,
  `observation` longtext,
  `institution_id` bigint NOT NULL,
  `catagenda_id` bigint NOT NULL,
  `meeting_type_id` varchar(255) NOT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `title_slug` (`title_slug`),
  KEY `event_agenda_institution_id_a6ce7188_fk_institute_institution_id` (`institution_id`),
  KEY `event_agenda_catagenda_id_11e15102_fk_event_catagenda_id` (`catagenda_id`),
  CONSTRAINT `event_agenda_catagenda_id_11e15102_fk_event_catagenda_id` FOREIGN KEY (`catagenda_id`) REFERENCES `event_catagenda` (`id`),
  CONSTRAINT `event_agenda_institution_id_a6ce7188_fk_institute_institution_id` FOREIGN KEY (`institution_id`) REFERENCES `institute_institution` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_agenda`
--

LOCK TABLES `event_agenda` WRITE;
/*!40000 ALTER TABLE `event_agenda` DISABLE KEYS */;
INSERT INTO `event_agenda` VALUES (5,'a','a','2025-07-21 14:42:09.000000','2026-07-21 18:42:51.000000',0,1,'2026-03-23 10:39:16.085359','2026-08-13 04:59:47.368221','Administrasaun Posto Balibo','Read','<p>nnggffndngffdn nnnnn</p>',1,1,'1',''),(6,'e','e','2025-03-21 14:42:09.000000','2025-03-21 17:42:51.000000',0,1,'2026-08-11 11:49:24.228695','2026-08-11 17:01:33.177107','Administrasaun Posto Balibo','Read','<p>nggfnf</p>',1,1,'1',''),(8,'W','w','2026-08-21 14:42:09.000000','2026-08-21 14:42:09.000000',1,1,'2026-08-11 17:10:00.414635','2026-08-12 11:49:45.453825','syy','Read','<p>BBXgvv</p>',1,1,'1',''),(9,'FF','ff','2026-08-13 06:52:09.000000','2026-08-21 14:42:09.000000',0,1,'2026-08-11 17:10:29.341351','2026-08-13 04:57:43.264404','ssss','Read',NULL,1,1,'1',''),(10,'fdgfdg','fdgfdg','2026-08-13 07:19:09.000000','2026-08-13 07:42:09.000000',0,1,'2026-08-11 17:11:18.186339','2026-08-13 05:19:38.062029','jgg','Read',NULL,1,1,'1','agenda_files/requirements_8H6XJMw.txt'),(11,'Atauor','atauor','2026-08-13 07:00:09.000000','2026-08-21 15:42:09.000000',0,1,'2026-08-11 17:13:12.826251','2026-08-13 05:00:36.368717','ssss','Read',NULL,1,1,'1',''),(12,'eee','eee','2026-08-13 07:14:09.000000','2026-08-22 16:42:09.000000',0,1,'2026-08-11 18:47:02.525450','2026-08-13 05:17:21.686644','ssss','Read',NULL,1,1,'1',''),(13,'er','er','2026-08-22 15:42:09.000000','2026-08-22 16:42:09.000000',0,1,'2026-08-11 19:59:51.691590','2026-08-11 19:59:51.691590','Administrasaun Posto Balibob','Read',NULL,1,1,'1',''),(14,'aT','at','2026-08-22 13:42:09.000000','2026-08-22 16:42:09.000000',0,1,'2026-08-12 11:34:16.826289','2026-08-12 11:34:16.826289','ssss6','Read',NULL,1,1,'1',''),(15,'DD','dd','2026-08-13 06:50:09.000000','2026-08-22 17:42:09.000000',0,1,'2026-08-12 11:35:03.045826','2026-08-13 04:50:05.753799','ssssX','Read',NULL,1,1,'1',''),(16,'FEFEF','fefef','2026-08-12 11:42:09.000000','2026-08-12 13:42:09.000000',0,1,'2026-08-12 11:35:48.248847','2026-08-12 12:03:24.947676','Administrasaun Posto Balibo','Read',NULL,1,1,'1',''),(17,'Plano Servisu','plano-servisu','2026-08-13 06:36:00.000000','2026-08-14 07:56:00.000000',0,1,'2026-08-13 01:00:16.454294','2026-08-13 04:37:24.146463','MOP OFfice','Read',NULL,1,1,'1','');
/*!40000 ALTER TABLE `event_agenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_agenda_recipients`
--

DROP TABLE IF EXISTS `event_agenda_recipients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_agenda_recipients` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `agenda_id` bigint NOT NULL,
  `agendarecipient_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_agenda_recipients_agenda_id_agendarecipien_806f0965_uniq` (`agenda_id`,`agendarecipient_id`),
  KEY `event_agenda_recipie_agendarecipient_id_02b0cebf_fk_event_age` (`agendarecipient_id`),
  CONSTRAINT `event_agenda_recipie_agendarecipient_id_02b0cebf_fk_event_age` FOREIGN KEY (`agendarecipient_id`) REFERENCES `event_agendarecipient` (`id`),
  CONSTRAINT `event_agenda_recipients_agenda_id_7fdffdeb_fk_event_agenda_id` FOREIGN KEY (`agenda_id`) REFERENCES `event_agenda` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_agenda_recipients`
--

LOCK TABLES `event_agenda_recipients` WRITE;
/*!40000 ALTER TABLE `event_agenda_recipients` DISABLE KEYS */;
INSERT INTO `event_agenda_recipients` VALUES (6,9,4),(7,9,6),(10,10,4),(8,11,4),(9,12,4),(5,15,4),(1,17,1),(2,17,4),(4,17,6);
/*!40000 ALTER TABLE `event_agenda_recipients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_agendanotification`
--

DROP TABLE IF EXISTS `event_agendanotification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_agendanotification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reminder_type` varchar(20) NOT NULL,
  `sent_at` datetime(6) DEFAULT NULL,
  `success` tinyint(1) NOT NULL,
  `error_message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `agenda_id` bigint NOT NULL,
  `recipient_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_agenda_email_reminder` (`agenda_id`,`recipient_id`,`reminder_type`),
  KEY `event_agendanotifica_recipient_id_66935d42_fk_event_age` (`recipient_id`),
  CONSTRAINT `event_agendanotifica_recipient_id_66935d42_fk_event_age` FOREIGN KEY (`recipient_id`) REFERENCES `event_agendarecipient` (`id`),
  CONSTRAINT `event_agendanotification_agenda_id_8a50d915_fk_event_agenda_id` FOREIGN KEY (`agenda_id`) REFERENCES `event_agenda` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_agendanotification`
--

LOCK TABLES `event_agendanotification` WRITE;
/*!40000 ALTER TABLE `event_agendanotification` DISABLE KEYS */;
INSERT INTO `event_agendanotification` VALUES (1,'2_hours','2026-08-13 03:56:07.929419',1,'','2026-08-13 03:56:02.028672',17,1),(2,'2_hours','2026-08-13 03:56:12.917901',1,'','2026-08-13 03:56:07.934154',17,4),(3,'2_hours','2026-08-13 03:56:17.863532',1,'','2026-08-13 03:56:12.921828',17,6),(4,'2_hours','2026-08-13 04:40:29.468653',1,'','2026-08-13 04:40:23.395079',15,4),(5,'2_hours','2026-08-13 04:52:28.464065',1,'','2026-08-13 04:52:23.314837',9,4),(6,'2_hours','2026-08-13 04:58:28.603478',1,'','2026-08-13 04:58:23.295131',9,6),(7,'2_hours','2026-08-13 05:01:28.707437',1,'','2026-08-13 05:01:23.324097',11,4),(8,'2_hours','2026-08-13 05:21:28.649525',1,'','2026-08-13 05:14:23.312327',12,4),(9,'2_hours','2026-08-13 05:21:34.332628',1,'','2026-08-13 05:19:23.348407',10,4);
/*!40000 ALTER TABLE `event_agendanotification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_agendarecipient`
--

DROP TABLE IF EXISTS `event_agendarecipient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_agendarecipient` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `position` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_agendarecipient_email_f825b230_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_agendarecipient`
--

LOCK TABLES `event_agendarecipient` WRITE;
/*!40000 ALTER TABLE `event_agendarecipient` DISABLE KEYS */;
INSERT INTO `event_agendarecipient` VALUES (1,'Cristovão Fausto Guterres','crisguterres8486@gmail.com',1,'2026-08-13 00:55:26.983535','2026-08-13 03:02:09.370299',1,'Chefe Gabinete Ministro-MOP'),(4,'Emerenciana da Costa Maia Freitas','fernaomouzinho00@gmail.com',1,'2026-08-13 01:21:07.252957','2026-08-13 03:09:19.847709',1,'Assesora Gabinete Ministro-MOP'),(6,'João Fátima de Jesus','joaofdejesu@gmail.com',1,'2026-08-13 03:04:14.856348','2026-08-13 03:04:14.856348',1,'Secretario Gabinete Ministro-MOP');
/*!40000 ALTER TABLE `event_agendarecipient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_catagenda`
--

DROP TABLE IF EXISTS `event_catagenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_catagenda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name_category` varchar(200) NOT NULL,
  `name_category_slug` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_category` (`name_category`),
  UNIQUE KEY `name_category_slug` (`name_category_slug`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_catagenda`
--

LOCK TABLES `event_catagenda` WRITE;
/*!40000 ALTER TABLE `event_catagenda` DISABLE KEYS */;
INSERT INTO `event_catagenda` VALUES (1,'Internal','internal'),(2,'Eksternal','eksternal');
/*!40000 ALTER TABLE `event_catagenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_commentinformative`
--

DROP TABLE IF EXISTS `event_commentinformative`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_commentinformative` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_on` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `informative_id` bigint NOT NULL,
  `problems` longtext NOT NULL,
  `results` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `event_commentinforma_informative_id_116a69a0_fk_event_inf` (`informative_id`),
  CONSTRAINT `event_commentinforma_informative_id_116a69a0_fk_event_inf` FOREIGN KEY (`informative_id`) REFERENCES `event_informative` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_commentinformative`
--

LOCK TABLES `event_commentinformative` WRITE;
/*!40000 ALTER TABLE `event_commentinformative` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_commentinformative` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_histagenda`
--

DROP TABLE IF EXISTS `event_histagenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_histagenda` (
  `id` int NOT NULL,
  `location_new` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `end_time_new` datetime(6) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_cancel` tinyint(1) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `observation` longtext,
  `start_time` datetime(6) DEFAULT NULL,
  `start_time_new` datetime(6) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `title` varchar(255) NOT NULL,
  `title_slug` varchar(255) NOT NULL,
  `institution` varchar(255) DEFAULT NULL,
  `catagenda` varchar(25) DEFAULT NULL,
  `meeting_type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `event_histagenda_title_slug_82dc6b2a` (`title_slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_histagenda`
--

LOCK TABLES `event_histagenda` WRITE;
/*!40000 ALTER TABLE `event_histagenda` DISABLE KEYS */;
INSERT INTO `event_histagenda` VALUES (4,'Sala Mop','2025-03-24 15:43:56.440986','2025-05-27 15:27:39.489605','2025-03-21 17:42:51.000000','2025-03-21 17:42:51.000000',1,0,'Sala Mop','<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Baseia ba encontro nebe realiza iha dia 13/3/2025&nbsp; nebe propoin husi Unicef -DNRAS- BTL.&nbsp;</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Objectivo</span></strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\"> husi encontro ida nee :</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">konvida Sua Exc. Sr. Samuel Marcal (Ministro das Obras Publicas ) atu marka Prezensa iha dia 21 de Marsu 2025 hodi asina Akordo&nbsp; entre parte rua MOP no UNICEF.&nbsp;</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">&nbsp;</span>Assunto sobre</strong> :</p>\r\n<ol style=\"margin-top: 0cm; text-align: left;\" start=\"1\" type=\"1\">\r\n<li class=\"MsoNormal\" style=\"mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;\">servisu bee no saniamento basika no&nbsp;<em>Climate Resilient&nbsp; wate</em>r ( <em>include Children in Schools/ECD and families in HCFs</em>) iha 2025 foka ba Municipio neen&nbsp; &nbsp; hanesan Aileu, Ainaro, Dili, Ermera<strong> &nbsp;Lautem</strong> no Viqueque (hare liu ba&nbsp; area rural)</li>\r\n<li class=\"MsoNormal\" style=\"mso-list: l0 level1 lfo1; tab-stops: list 36.0pt;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Plano Orsamento ba tinan 2025 hamutuk : $1,236,478.27</span></li>\r\n</ol>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Resume :&nbsp;</span></strong></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">plano servsiu anual 2025&nbsp; Realiza ona&nbsp; iha <strong>21/3/2025</strong></span></p>','2025-03-21 14:42:09.000000','2025-03-21 14:42:09.000000','Read','a','a','MOP','Internal','Apresentasaun Servisu IT'),(5,'Administrasaun Posto Balibo','2026-08-11 16:24:24.537239','2026-08-11 16:46:49.369202','2025-03-21 17:42:51.000000','2025-03-21 17:42:51.000000',1,0,'Administrasaun Posto Balibo','','2025-03-21 14:42:09.000000','2025-03-21 14:42:09.000000','Read','a','a','MOPs','Internal','Enkontru'),(6,'Administrasaun Posto Balibo','2026-08-11 16:29:51.464560','2026-08-11 17:01:33.180101','2025-03-21 17:42:51.000000','2025-03-21 17:42:51.000000',1,0,'Administrasaun Posto Balibo','<p>nggfnf</p>','2025-03-21 14:42:09.000000','2025-03-21 14:42:09.000000','Read','e','e','MOPs','Internal','Enkontru'),(7,'f','2026-08-11 17:03:34.937058','2026-08-11 17:05:14.982655','2026-07-21 18:42:09.000000','2026-07-21 18:42:09.000000',1,0,'f','<p>kkkk</p>','2026-07-21 14:42:09.000000','2026-07-21 14:42:09.000000','Read','gg','gg','MOPs','Internal','Enkontru'),(8,'syy','2026-08-11 17:10:00.417632','2026-08-12 11:49:45.458822','2026-08-21 14:42:09.000000','2026-08-21 14:42:09.000000',1,1,'s','<p>BBXgvv</p>','2026-08-21 14:42:09.000000','2026-08-21 14:42:09.000000','Read','W','w','MOPs','Internal','Enkontru'),(9,'ssss','2026-08-11 17:10:29.345349','2026-08-11 17:10:29.345349','2026-08-21 14:42:09.000000','2026-08-21 14:42:09.000000',1,0,'ssss',NULL,'2026-08-21 14:42:09.000000','2026-08-21 14:42:09.000000','Pending','FF','ff','MOPs','Internal','Enkontru'),(10,'jgg','2026-08-11 17:11:18.189332','2026-08-11 17:11:18.189332','2026-08-21 18:42:09.000000','2026-08-21 18:42:09.000000',1,0,'jgg',NULL,'2026-08-21 14:42:09.000000','2026-08-21 14:42:09.000000','Pending','fdgfdg','fdgfdg','MOPs','Internal','Enkontru'),(11,'ssss','2026-08-11 17:13:12.829251','2026-08-11 17:13:12.829251','2026-08-21 15:42:09.000000','2026-08-21 15:42:09.000000',1,0,'ssss',NULL,'2026-08-21 14:42:09.000000','2026-08-21 14:42:09.000000','Pending','Atauor','atauor','MOPs','Internal','Enkontru'),(12,'ssss','2026-08-11 18:47:02.528446','2026-08-11 18:47:02.528446','2026-08-22 16:42:09.000000','2026-08-22 16:42:09.000000',1,0,'ssss',NULL,'2026-08-22 14:42:09.000000','2026-08-22 14:42:09.000000','Pending','eee','eee','MOPs','Internal','Enkontru'),(13,'Administrasaun Posto Balibob','2026-08-11 19:59:51.694588','2026-08-11 19:59:51.694588','2026-08-22 16:42:09.000000','2026-08-22 16:42:09.000000',1,0,'Administrasaun Posto Balibob',NULL,'2026-08-22 15:42:09.000000','2026-08-22 15:42:09.000000','Pending','er','er','MOPs','Internal','Enkontru'),(14,'ssss6','2026-08-12 11:34:16.843294','2026-08-12 11:34:16.843294','2026-08-22 16:42:09.000000','2026-08-22 16:42:09.000000',1,0,'ssss6',NULL,'2026-08-22 13:42:09.000000','2026-08-22 13:42:09.000000','Pending','aT','at','MOPs','Internal','Enkontru'),(15,'ssssX','2026-08-12 11:35:03.048810','2026-08-12 11:35:03.048810','2026-08-22 17:42:09.000000','2026-08-22 17:42:09.000000',1,0,'ssssX',NULL,'2026-08-22 16:42:09.000000','2026-08-22 16:42:09.000000','Pending','DD','dd','MOPs','Internal','Enkontru'),(16,'Administrasaun Posto Balibo','2026-08-12 11:35:48.251849','2026-08-12 11:35:48.251849','2026-08-22 18:42:09.000000','2026-08-22 18:42:09.000000',1,0,'Administrasaun Posto Balibo',NULL,'2026-08-22 17:42:09.000000','2026-08-22 17:42:09.000000','Pending','FEFEF','fefef','MOPs','Internal','Enkontru'),(17,'MOP OFfice','2026-08-13 01:00:16.459294','2026-08-13 01:00:16.459294','2026-08-14 08:42:09.000000','2026-08-14 08:42:09.000000',1,0,'MOP OFfice',NULL,'2026-08-14 01:00:09.000000','2026-08-14 01:00:09.000000','Pending','Plano Servisu','plano-servisu','MOPs','Internal','Enkontru');
/*!40000 ALTER TABLE `event_histagenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_informative`
--

DROP TABLE IF EXISTS `event_informative`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_informative` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `title_slug` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_done` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_comment` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `title_slug` (`title_slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_informative`
--

LOCK TABLES `event_informative` WRITE;
/*!40000 ALTER TABLE `event_informative` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_informative` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_requestagenda`
--

DROP TABLE IF EXISTS `event_requestagenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_requestagenda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `title_slug` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `catagenda_id` bigint DEFAULT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `institution_id` bigint DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `title_slug` (`title_slug`),
  KEY `event_requestagenda_catagenda_id_cd1b6485_fk_event_catagenda_id` (`catagenda_id`),
  KEY `event_requestagenda_institution_id_2f1cf5c3_fk_institute` (`institution_id`),
  CONSTRAINT `event_requestagenda_catagenda_id_cd1b6485_fk_event_catagenda_id` FOREIGN KEY (`catagenda_id`) REFERENCES `event_catagenda` (`id`),
  CONSTRAINT `event_requestagenda_institution_id_2f1cf5c3_fk_institute` FOREIGN KEY (`institution_id`) REFERENCES `institute_institution` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_requestagenda`
--

LOCK TABLES `event_requestagenda` WRITE;
/*!40000 ALTER TABLE `event_requestagenda` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_requestagenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_typeagenda`
--

DROP TABLE IF EXISTS `event_typeagenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_typeagenda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name_type` varchar(200) NOT NULL,
  `name_type_slug` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_type` (`name_type`),
  UNIQUE KEY `name_type_slug` (`name_type_slug`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_typeagenda`
--

LOCK TABLES `event_typeagenda` WRITE;
/*!40000 ALTER TABLE `event_typeagenda` DISABLE KEYS */;
INSERT INTO `event_typeagenda` VALUES (1,'Enkontru','enkontru'),(2,'Lansamentu','lansamentu');
/*!40000 ALTER TABLE `event_typeagenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_yearagenda`
--

DROP TABLE IF EXISTS `event_yearagenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_yearagenda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `year` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_yearagenda`
--

LOCK TABLES `event_yearagenda` WRITE;
/*!40000 ALTER TABLE `event_yearagenda` DISABLE KEYS */;
INSERT INTO `event_yearagenda` VALUES (1,2025,1),(2,2026,1);
/*!40000 ALTER TABLE `event_yearagenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institute_attendence`
--

DROP TABLE IF EXISTS `institute_attendence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institute_attendence` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name_attendence` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institute_attendence`
--

LOCK TABLES `institute_attendence` WRITE;
/*!40000 ALTER TABLE `institute_attendence` DISABLE KEYS */;
/*!40000 ALTER TABLE `institute_attendence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institute_departmentadn`
--

DROP TABLE IF EXISTS `institute_departmentadn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institute_departmentadn` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name_department` varchar(255) DEFAULT NULL,
  `unitadn_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `institute_department_unitadn_id_351f427c_fk_institute` (`unitadn_id`),
  CONSTRAINT `institute_department_unitadn_id_351f427c_fk_institute` FOREIGN KEY (`unitadn_id`) REFERENCES `institute_unitadn` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institute_departmentadn`
--

LOCK TABLES `institute_departmentadn` WRITE;
/*!40000 ALTER TABLE `institute_departmentadn` DISABLE KEYS */;
/*!40000 ALTER TABLE `institute_departmentadn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institute_institution`
--

DROP TABLE IF EXISTS `institute_institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institute_institution` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name_institution` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institute_institution`
--

LOCK TABLES `institute_institution` WRITE;
/*!40000 ALTER TABLE `institute_institution` DISABLE KEYS */;
INSERT INTO `institute_institution` VALUES (1,'MOPs');
/*!40000 ALTER TABLE `institute_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institute_unitadn`
--

DROP TABLE IF EXISTS `institute_unitadn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institute_unitadn` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name_unit` varchar(255) DEFAULT NULL,
  `abreviation` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institute_unitadn`
--

LOCK TABLES `institute_unitadn` WRITE;
/*!40000 ALTER TABLE `institute_unitadn` DISABLE KEYS */;
/*!40000 ALTER TABLE `institute_unitadn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_logo`
--

DROP TABLE IF EXISTS `reports_logo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_logo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `logo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_logo`
--

LOCK TABLES `reports_logo` WRITE;
/*!40000 ALTER TABLE `reports_logo` DISABLE KEYS */;
INSERT INTO `reports_logo` VALUES (1,'logo/logo-mop_0yjZIHp.jpeg');
/*!40000 ALTER TABLE `reports_logo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_mensual`
--

DROP TABLE IF EXISTS `reports_mensual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_mensual` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `name_slug` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_slug` (`name_slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_mensual`
--

LOCK TABLES `reports_mensual` WRITE;
/*!40000 ALTER TABLE `reports_mensual` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports_mensual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_semestral`
--

DROP TABLE IF EXISTS `reports_semestral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_semestral` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `name_slug` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_slug` (`name_slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_semestral`
--

LOCK TABLES `reports_semestral` WRITE;
/*!40000 ALTER TABLE `reports_semestral` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports_semestral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_trimestral`
--

DROP TABLE IF EXISTS `reports_trimestral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_trimestral` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `name_slug` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_slug` (`name_slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_trimestral`
--

LOCK TABLES `reports_trimestral` WRITE;
/*!40000 ALTER TABLE `reports_trimestral` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports_trimestral` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-13 14:38:24
