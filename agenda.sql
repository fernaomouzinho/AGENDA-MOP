-- phpMyAdmin SQL Dump
-- version 
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 12, 2026 at 05:48 AM
-- Server version: 8.4.7-percona-sure1
-- PHP Version: 8.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartvps04_agenda`
--

-- --------------------------------------------------------

--
-- Table structure for table `authentication_user`
--

CREATE TABLE `authentication_user` (
  `id` bigint NOT NULL,
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
  `is_dei` tinyint(1) NOT NULL,
  `is_adj` tinyint(1) NOT NULL,
  `is_uga` tinyint(1) NOT NULL,
  `is_uap` tinyint(1) NOT NULL,
  `is_ucvq` tinyint(1) NOT NULL,
  `is_uedc` tinyint(1) NOT NULL,
  `is_secretary` tinyint(1) NOT NULL,
  `is_media` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `authentication_user`
--

INSERT INTO `authentication_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_dei`, `is_adj`, `is_uga`, `is_uap`, `is_ucvq`, `is_uedc`, `is_secretary`, `is_media`) VALUES
(1, 'pbkdf2_sha256$600000$tEgTM28gStRA6vFXm7HLNg$cBKZto+oxx9p7bMZFAlnfa8qK3vkwiynz/4TzPfwYFI=', '2026-08-11 00:37:35.868157', 1, 'admin', '', '', 'admin@gmil.com', 1, 1, '2025-03-20 03:18:08.000000', 0, 0, 0, 0, 0, 0, 0, 0),
(2, 'pbkdf2_sha256$600000$iKJBQs0QXxJTE2LhOcgk8p$2mqCsny3S895VwyddUb30dWsle0xP77gLq84qtfcFWY=', '2025-08-01 07:45:22.610115', 0, 'emerenciana', 'Emerenciana', '', '', 0, 1, '2025-03-20 06:08:53.000000', 0, 0, 0, 0, 0, 0, 0, 0),
(3, 'pbkdf2_sha256$600000$tEgTM28gStRA6vFXm7HLNg$cBKZto+oxx9p7bMZFAlnfa8qK3vkwiynz/4TzPfwYFI=', '2025-03-22 00:01:45.000000', 0, 'cristovao', 'Cristovão', 'Fausto Guterres', '', 0, 1, '2025-03-22 00:01:19.000000', 0, 0, 0, 0, 0, 0, 0, 0),
(4, 'pbkdf2_sha256$600000$cu9z5MvWULExrHQXaCfMwA$GfWHybK43GBHBStaQkPOaPKvycJNAkGHtvXTJBR/J4U=', '2025-06-29 23:45:55.943308', 0, 'fidelia', 'Fidelia', 'Cristiana Freitas', '', 1, 1, '2025-03-22 03:32:39.000000', 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `authentication_user_groups`
--

CREATE TABLE `authentication_user_groups` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `authentication_user_groups`
--

INSERT INTO `authentication_user_groups` (`id`, `user_id`, `group_id`) VALUES
(4, 1, 1),
(2, 2, 2),
(1, 3, 3),
(3, 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `authentication_user_user_permissions`
--

CREATE TABLE `authentication_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'admin'),
(2, 'gp_ass'),
(3, 'gp_che'),
(4, 'gp_min'),
(5, 'gp_sec');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36),
(37, 1, 37),
(38, 1, 38),
(39, 1, 39),
(40, 1, 40),
(41, 1, 41),
(42, 1, 42),
(43, 1, 43),
(44, 1, 44),
(45, 1, 45),
(46, 1, 46),
(47, 1, 47),
(48, 1, 48),
(49, 1, 49),
(50, 1, 50),
(51, 1, 51),
(52, 1, 52),
(53, 1, 53),
(54, 1, 54),
(55, 1, 55),
(56, 1, 56),
(57, 1, 57),
(58, 1, 58),
(59, 1, 59),
(60, 1, 60),
(61, 1, 61),
(62, 1, 62),
(63, 1, 63),
(64, 1, 64),
(65, 1, 65),
(66, 1, 66),
(67, 1, 67),
(68, 1, 68),
(69, 1, 69),
(70, 1, 70),
(71, 1, 71),
(72, 1, 72),
(73, 1, 73),
(74, 1, 74),
(75, 1, 75),
(76, 1, 76),
(77, 1, 77),
(78, 1, 78),
(79, 1, 79),
(80, 1, 80),
(81, 1, 81),
(82, 1, 82),
(83, 1, 83),
(84, 1, 84);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add attendence', 7, 'add_attendence'),
(26, 'Can change attendence', 7, 'change_attendence'),
(27, 'Can delete attendence', 7, 'delete_attendence'),
(28, 'Can view attendence', 7, 'view_attendence'),
(29, 'Can add institution', 8, 'add_institution'),
(30, 'Can change institution', 8, 'change_institution'),
(31, 'Can delete institution', 8, 'delete_institution'),
(32, 'Can view institution', 8, 'view_institution'),
(33, 'Can add unit adn', 9, 'add_unitadn'),
(34, 'Can change unit adn', 9, 'change_unitadn'),
(35, 'Can delete unit adn', 9, 'delete_unitadn'),
(36, 'Can view unit adn', 9, 'view_unitadn'),
(37, 'Can add department adn', 10, 'add_departmentadn'),
(38, 'Can change department adn', 10, 'change_departmentadn'),
(39, 'Can delete department adn', 10, 'delete_departmentadn'),
(40, 'Can view department adn', 10, 'view_departmentadn'),
(41, 'Can add agenda', 11, 'add_agenda'),
(42, 'Can change agenda', 11, 'change_agenda'),
(43, 'Can delete agenda', 11, 'delete_agenda'),
(44, 'Can view agenda', 11, 'view_agenda'),
(45, 'Can add comment informative', 12, 'add_commentinformative'),
(46, 'Can change comment informative', 12, 'change_commentinformative'),
(47, 'Can delete comment informative', 12, 'delete_commentinformative'),
(48, 'Can view comment informative', 12, 'view_commentinformative'),
(49, 'Can add informative', 13, 'add_informative'),
(50, 'Can change informative', 13, 'change_informative'),
(51, 'Can delete informative', 13, 'delete_informative'),
(52, 'Can view informative', 13, 'view_informative'),
(53, 'Can add yearagenda', 14, 'add_yearagenda'),
(54, 'Can change yearagenda', 14, 'change_yearagenda'),
(55, 'Can delete yearagenda', 14, 'delete_yearagenda'),
(56, 'Can view yearagenda', 14, 'view_yearagenda'),
(57, 'Can add hist agenda', 15, 'add_histagenda'),
(58, 'Can change hist agenda', 15, 'change_histagenda'),
(59, 'Can delete hist agenda', 15, 'delete_histagenda'),
(60, 'Can view hist agenda', 15, 'view_histagenda'),
(61, 'Can add cat agenda', 16, 'add_catagenda'),
(62, 'Can change cat agenda', 16, 'change_catagenda'),
(63, 'Can delete cat agenda', 16, 'delete_catagenda'),
(64, 'Can view cat agenda', 16, 'view_catagenda'),
(65, 'Can add request agenda', 17, 'add_requestagenda'),
(66, 'Can change request agenda', 17, 'change_requestagenda'),
(67, 'Can delete request agenda', 17, 'delete_requestagenda'),
(68, 'Can view request agenda', 17, 'view_requestagenda'),
(69, 'Can add semestral', 18, 'add_semestral'),
(70, 'Can change semestral', 18, 'change_semestral'),
(71, 'Can delete semestral', 18, 'delete_semestral'),
(72, 'Can view semestral', 18, 'view_semestral'),
(73, 'Can add trimestral', 19, 'add_trimestral'),
(74, 'Can change trimestral', 19, 'change_trimestral'),
(75, 'Can delete trimestral', 19, 'delete_trimestral'),
(76, 'Can view trimestral', 19, 'view_trimestral'),
(77, 'Can add mensual', 20, 'add_mensual'),
(78, 'Can change mensual', 20, 'change_mensual'),
(79, 'Can delete mensual', 20, 'delete_mensual'),
(80, 'Can view mensual', 20, 'view_mensual'),
(81, 'Can add logo', 21, 'add_logo'),
(82, 'Can change logo', 21, 'change_logo'),
(83, 'Can delete logo', 21, 'delete_logo'),
(84, 'Can view logo', 21, 'view_logo'),
(85, 'Can add type agenda', 22, 'add_typeagenda'),
(86, 'Can change type agenda', 22, 'change_typeagenda'),
(87, 'Can delete type agenda', 22, 'delete_typeagenda'),
(88, 'Can view type agenda', 22, 'view_typeagenda'),
(89, 'Can add attachment', 23, 'add_attachment'),
(90, 'Can change attachment', 23, 'change_attachment'),
(91, 'Can delete attachment', 23, 'delete_attachment'),
(92, 'Can view attachment', 23, 'view_attachment');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-03-20 03:23:43.237007', '1', '2025', 1, '[{\"added\": {}}]', 14, 1),
(2, '2025-03-20 03:26:25.493166', '1', 'Internal', 1, '[{\"added\": {}}]', 16, 1),
(3, '2025-03-20 03:26:41.783303', '2', 'Eksternal', 1, '[{\"added\": {}}]', 16, 1),
(4, '2025-03-20 03:27:36.682418', '2', '2024', 1, '[{\"added\": {}}]', 14, 1),
(5, '2025-03-20 03:27:42.206973', '3', '2023', 1, '[{\"added\": {}}]', 14, 1),
(6, '2025-03-20 03:27:47.952966', '4', '2022', 1, '[{\"added\": {}}]', 14, 1),
(7, '2025-03-20 06:10:18.865890', '2', 'emerenciana', 1, '[{\"added\": {}}]', 6, 1),
(8, '2025-03-22 00:02:12.735562', '2', 'emerenciana', 2, '[{\"changed\": {\"fields\": [\"Password\"]}}]', 6, 1),
(9, '2025-03-22 00:02:23.254127', '3', 'cristovao', 1, '[{\"added\": {}}]', 6, 1),
(10, '2025-03-22 00:03:04.291387', '1', 'admin', 1, '[{\"added\": {}}]', 3, 1),
(11, '2025-03-22 00:03:19.021470', '2', 'gp_ass', 1, '[{\"added\": {}}]', 3, 1),
(12, '2025-03-22 00:03:30.999309', '3', 'gp_che', 1, '[{\"added\": {}}]', 3, 1),
(13, '2025-03-22 03:28:20.849274', '4', 'gp_min', 1, '[{\"added\": {}}]', 3, 1),
(14, '2025-03-22 03:28:41.290749', '5', 'gp_sec', 1, '[{\"added\": {}}]', 3, 1),
(15, '2025-03-22 03:28:56.981456', '3', 'cristovao', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 6, 1),
(16, '2025-03-22 03:29:06.430073', '2', 'emerenciana', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 6, 1),
(17, '2025-03-22 03:32:02.198565', '2', 'emerenciana', 2, '[{\"changed\": {\"fields\": [\"Last login\"]}}]', 6, 1),
(18, '2025-03-22 03:32:44.822136', '4', 'fidelia', 1, '[{\"added\": {}}]', 6, 1),
(19, '2025-03-22 03:33:11.119506', '4', 'fidelia', 2, '[{\"changed\": {\"fields\": [\"Last login\"]}}]', 6, 1),
(20, '2025-03-22 03:33:17.822527', '3', 'cristovao', 2, '[]', 6, 1),
(21, '2025-03-22 03:33:29.513925', '2', 'emerenciana', 2, '[]', 6, 1),
(22, '2025-03-24 00:19:51.451245', '1', 'Logo object (1)', 1, '[{\"added\": {}}]', 21, 1),
(23, '2025-03-24 00:35:37.859992', '1', 'Logo object (1)', 3, '', 21, 1),
(24, '2025-03-24 00:35:48.342739', '2', 'Logo object (2)', 1, '[{\"added\": {}}]', 21, 1),
(25, '2025-03-24 00:46:18.462678', '2', 'Logo object (2)', 3, '', 21, 1),
(26, '2025-03-24 00:47:19.530347', '3', 'Logo object (3)', 1, '[{\"added\": {}}]', 21, 1),
(27, '2025-03-24 00:50:38.637390', '3', 'Logo object (3)', 3, '', 21, 1),
(28, '2025-03-24 00:50:45.562537', '4', 'Logo object (4)', 1, '[{\"added\": {}}]', 21, 1),
(29, '2025-03-24 01:02:59.207569', '4', 'Logo object (4)', 3, '', 21, 1),
(30, '2025-03-24 01:09:35.203730', '5', 'Logo object (5)', 1, '[{\"added\": {}}]', 21, 1),
(31, '2025-03-24 01:10:02.498756', '5', 'Logo object (5)', 3, '', 21, 1),
(32, '2025-03-24 01:23:12.282037', '6', 'Logo object (6)', 1, '[{\"added\": {}}]', 21, 1),
(33, '2025-03-24 06:55:23.601993', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 6, 1),
(34, '2025-03-28 06:17:36.451652', '1', 'Enkontru', 1, '[{\"added\": {}}]', 22, 1),
(35, '2025-03-28 06:17:45.534677', '2', 'Lansamentu', 1, '[{\"added\": {}}]', 22, 1),
(36, '2025-03-28 06:42:39.433713', '3', 'Seluk-Seluk', 1, '[{\"added\": {}}]', 22, 1),
(37, '2025-04-10 06:45:15.300757', '16', 'Lansamento projeto melloramento sistema fornesimentu Bee moos iha P.A. Balibo, Munisipio Bobonaro', 2, '[{\"changed\": {\"fields\": [\"Oras Remata\"]}}]', 11, 1),
(38, '2025-04-10 06:47:03.294329', '16', 'Lansamento projeto melloramento sistema fornesimentu Bee moos iha P.A. Balibo, Munisipio Bobonaro', 2, '[{\"changed\": {\"fields\": [\"Oras Remata\"]}}]', 11, 1),
(39, '2025-04-10 06:49:10.476717', '16', 'Lansamento projeto melloramento sistema fornesimentu Bee moos iha P.A. Balibo, Munisipio Bobonaro', 2, '[{\"changed\": {\"fields\": [\"Is cancel\"]}}]', 11, 1),
(40, '2025-04-13 08:10:52.340769', '6', 'Logo object (6)', 3, '', 21, 1),
(41, '2025-04-13 08:11:29.211022', '7', 'Logo object (7)', 1, '[{\"added\": {}}]', 21, 1),
(42, '2026-02-23 05:51:44.089240', '5', '2026', 1, '[{\"added\": {}}]', 14, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(6, 'authentication', 'user'),
(4, 'contenttypes', 'contenttype'),
(23, 'django_summernote', 'attachment'),
(11, 'event', 'agenda'),
(16, 'event', 'catagenda'),
(12, 'event', 'commentinformative'),
(15, 'event', 'histagenda'),
(13, 'event', 'informative'),
(17, 'event', 'requestagenda'),
(22, 'event', 'typeagenda'),
(14, 'event', 'yearagenda'),
(7, 'institute', 'attendence'),
(10, 'institute', 'departmentadn'),
(8, 'institute', 'institution'),
(9, 'institute', 'unitadn'),
(21, 'reports', 'logo'),
(20, 'reports', 'mensual'),
(18, 'reports', 'semestral'),
(19, 'reports', 'trimestral'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-03-17 06:25:24.000924'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-03-17 06:25:24.062048'),
(3, 'auth', '0001_initial', '2025-03-17 06:25:24.302662'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-03-17 06:25:24.363662'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-03-17 06:25:24.373846'),
(6, 'auth', '0004_alter_user_username_opts', '2025-03-17 06:25:24.386334'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-03-17 06:25:24.397345'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-03-17 06:25:24.401915'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-03-17 06:25:24.412507'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-03-17 06:25:24.424854'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-03-17 06:25:24.435555'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-03-17 06:25:24.458247'),
(13, 'auth', '0011_update_proxy_permissions', '2025-03-17 06:25:24.470829'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-03-17 06:25:24.482617'),
(15, 'authentication', '0001_initial', '2025-03-17 06:25:24.760416'),
(16, 'admin', '0001_initial', '2025-03-17 06:25:24.898544'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-03-17 06:25:24.915475'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-03-17 06:25:24.931954'),
(19, 'authentication', '0002_alter_user_is_media_alter_user_is_secretary', '2025-03-17 06:25:24.953387'),
(20, 'institute', '0001_initial', '2025-03-17 06:25:24.975016'),
(21, 'institute', '0002_rename_name_institution_invitedinstitute_name_institute', '2025-03-17 06:25:24.991444'),
(22, 'institute', '0003_invitedas', '2025-03-17 06:25:25.013630'),
(23, 'institute', '0004_rename_invitedas_attencence_and_more', '2025-03-17 06:25:25.060919'),
(24, 'institute', '0005_rename_attencence_attendence', '2025-03-17 06:25:25.095464'),
(25, 'institute', '0006_alter_attendence_options_and_more', '2025-03-17 06:25:25.103086'),
(26, 'institute', '0007_alter_attendence_options_and_more', '2025-03-17 06:25:25.109951'),
(27, 'event', '0001_initial', '2025-03-17 06:25:25.191041'),
(28, 'event', '0002_agenda_commentinformative_informative_yearagenda_and_more', '2025-03-17 06:25:25.518244'),
(29, 'event', '0003_agenda_location_alter_commentinformative_comment', '2025-03-17 06:25:25.585337'),
(30, 'event', '0004_invitedinstitue_remove_agenda_description_and_more', '2025-03-17 06:25:25.801337'),
(31, 'event', '0005_rename_invitedinstitue_invitedinstitute', '2025-03-17 06:25:25.975589'),
(32, 'event', '0006_alter_agenda_options', '2025-03-17 06:25:25.992566'),
(33, 'event', '0007_alter_agenda_options_remove_agenda_invitedinstitue', '2025-03-17 06:25:26.087427'),
(34, 'event', '0008_alter_invitedinstitute_id', '2025-03-17 06:25:26.130176'),
(35, 'event', '0009_agenda_invitedinstitue_alter_invitedinstitute_id', '2025-03-17 06:25:26.425982'),
(36, 'event', '0010_alter_invitedinstitute_name_institution', '2025-03-17 06:25:26.434024'),
(37, 'event', '0011_alter_invitedinstitute_options', '2025-03-17 06:25:26.443716'),
(38, 'event', '0012_remove_agenda_invitedinstitue_and_more', '2025-03-17 06:25:26.559739'),
(39, 'event', '0013_agenda_invitedinstitue', '2025-03-17 06:25:26.648076'),
(40, 'event', '0014_agenda_attendence', '2025-03-17 06:25:26.742771'),
(41, 'event', '0015_rename_active_commentinformative_is_active', '2025-03-17 06:25:26.768367'),
(42, 'event', '0016_alter_commentinformative_is_active', '2025-03-17 06:25:26.784429'),
(43, 'event', '0017_remove_informative_description', '2025-03-17 06:25:26.823555'),
(44, 'event', '0018_agenda_status', '2025-03-17 06:25:26.883129'),
(45, 'event', '0019_agenda_observation', '2025-03-17 06:25:26.930168'),
(46, 'event', '0020_alter_agenda_attendence_alter_agenda_invitedinstitue_and_more', '2025-03-17 06:25:27.068612'),
(47, 'event', '0021_alter_histagenda_options_remove_histagenda_agenda_and_more', '2025-03-17 06:25:27.873425'),
(48, 'event', '0022_alter_agenda_location_alter_agenda_observation_and_more', '2025-03-17 06:25:28.067267'),
(49, 'event', '0023_remove_agenda_invitedinstitue_and_more', '2025-03-17 06:25:28.291959'),
(50, 'institute', '0008_institution_delete_invitedinstitute', '2025-03-17 06:25:28.326133'),
(51, 'institute', '0009_alter_institution_name_institution', '2025-03-17 06:25:28.335974'),
(52, 'institute', '0010_alter_institution_name_institution', '2025-03-17 06:25:28.344639'),
(53, 'institute', '0011_unitadn_departmentadn', '2025-03-17 06:25:28.448823'),
(54, 'institute', '0012_alter_departmentadn_options_alter_unitadn_options', '2025-03-17 06:25:28.462376'),
(55, 'institute', '0013_alter_attendence_options_alter_institution_options_and_more', '2025-03-17 06:25:28.483358'),
(56, 'event', '0024_agenda_institution_histagenda_institution', '2025-03-17 06:25:28.719770'),
(57, 'event', '0025_catagenda', '2025-03-17 06:25:28.751161'),
(58, 'event', '0026_agenda_catagenda', '2025-03-17 06:25:28.876268'),
(59, 'event', '0027_alter_agenda_observation_alter_agenda_status', '2025-03-17 06:25:28.993229'),
(60, 'event', '0028_remove_commentinformative_comment_and_more', '2025-03-17 06:25:29.301103'),
(61, 'event', '0029_commentinformative_is_done', '2025-03-17 06:25:29.369219'),
(62, 'event', '0030_commentinformative_is_comment', '2025-03-17 06:25:29.434383'),
(63, 'event', '0031_remove_commentinformative_is_comment_and_more', '2025-03-17 06:25:29.557005'),
(64, 'event', '0032_remove_commentinformative_is_done', '2025-03-17 06:25:29.605439'),
(65, 'event', '0033_requestagenda', '2025-03-17 06:25:29.730322'),
(66, 'event', '0034_rename_updated_at_requestagenda_aproved_at_and_more', '2025-03-17 06:25:29.809113'),
(67, 'event', '0035_remove_requestagenda_status_requestagenda_is_approve_and_more', '2025-03-17 06:25:29.996502'),
(68, 'event', '0036_rename_aproved_at_requestagenda_approved_at', '2025-03-17 06:25:30.042979'),
(69, 'event', '0037_alter_requestagenda_options_and_more', '2025-03-17 06:25:30.838882'),
(70, 'event', '0038_alter_requestagenda_options_histagenda_catagenda_and_more', '2025-03-17 06:25:31.184663'),
(71, 'event', '0039_alter_histagenda_id', '2025-03-17 06:25:31.262565'),
(72, 'event', '0040_catagenda_name_category_slug', '2025-03-17 06:25:31.330982'),
(73, 'event', '0041_alter_agenda_observation', '2025-03-17 06:25:31.366376'),
(74, 'event', '0042_alter_agenda_options_alter_catagenda_options_and_more', '2025-03-17 06:25:31.719019'),
(75, 'reports', '0001_initial', '2025-03-17 06:25:31.763162'),
(76, 'reports', '0002_mensual', '2025-03-17 06:25:31.788562'),
(77, 'reports', '0003_alter_mensual_options', '2025-03-17 06:25:31.796257'),
(78, 'reports', '0004_logo', '2025-03-17 06:25:31.818273'),
(79, 'reports', '0005_alter_logo_options', '2025-03-17 06:25:31.826028'),
(80, 'sessions', '0001_initial', '2025-03-17 06:25:31.866403'),
(81, 'event', '0043_agenda_meeting_type_alter_agenda_end_time_and_more', '2025-03-22 00:00:31.543526'),
(82, 'event', '0044_alter_agenda_observation', '2025-03-24 02:38:42.296798'),
(83, 'event', '0045_histagenda_meeting_type_alter_agenda_observation', '2025-03-24 06:48:08.974481'),
(84, 'event', '0046_typeagenda_alter_agenda_meeting_type', '2025-03-28 06:13:51.831775'),
(85, 'django_summernote', '0001_initial', '2025-05-27 07:15:00.260218'),
(86, 'django_summernote', '0002_update-help_text', '2025-05-27 07:15:00.270879'),
(87, 'django_summernote', '0003_alter_attachment_id', '2025-05-27 07:15:00.318723'),
(88, 'event', '0047_agenda_attachment', '2025-05-27 07:15:00.371184');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0bhb5pdc5mnjsra60te33mrxv2h3gup3', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1wmRIL:gk9jckChD0wECiwMqqSjQKeS3mP7TzvhUWBW5ZrXWtY', '2026-08-05 07:23:09.683426'),
('1jptu0oywo1km0cack32jnt3l053vn98', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1uPcV3:jg8tzw439kuXsXgBgQVGArdjONzW_xFXXqoohq92IXk', '2025-06-26 07:37:25.516305'),
('1p53soo5dfc7v32rinfrfm5h6e7a7gaf', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1wROel:2q0yrOqIYPyPiq9KKi8vyZjvhjlumzwBVa2aDbDwRmE', '2026-06-08 06:19:19.427576'),
('24am5mlo3rgvtd3921ou8z50n88szemm', '.eJxVjMsOwiAQRf-FtSFMC2Vw6d5vIDM8pGpoUtqV8d-VpAvdnnPufQlP-1b83tLq5yjOQovTL2MKj1S7iHeqt0WGpW7rzLIn8rBNXpeYnpej_Tso1Mp3rRxGhujshBkxBRhZk1WcdXYajA1utC5P1JkBhTmBJgAFFBjNMIj3B9zfN3U:1uW1id:o7hc2cqcb6LCKwrYHDWdBs6bvL2D523me1pODJ_8TXo', '2025-07-13 23:45:55.947658'),
('3k71ldl0ewby5lnitomh7ji7gm8vs3zy', '.eJxVjMsOwiAQRf-FtSFMC2Vw6d5vIDM8pGpoUtqV8d-VpAvdnnPufQlP-1b83tLq5yjOQovTL2MKj1S7iHeqt0WGpW7rzLIn8rBNXpeYnpej_Tso1Mp3rRxGhujshBkxBRhZk1WcdXYajA1utC5P1JkBhTmBJgAFFBjNMIj3B9zfN3U:1ty2Ks:XReGWaLv_lJQ_E-MEh8oB6IX3b1XQ_OxOzGHhpm278c', '2025-04-11 05:32:54.954924'),
('3vden3fdudlxxv8m7u5484fm9ywnbvk6', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1wtZrt:dCeKn5ZXPc0ICGBsTaIxvCsVPvn5B00koYtzyB-V2Zc', '2026-08-24 23:57:21.495848'),
('448gn2jamapxciea3n31htqk7usjymqi', '.eJxVjMsOwiAQRf-FtSFMC2Vw6d5vIDM8pGpoUtqV8d-VpAvdnnPufQlP-1b83tLq5yjOQovTL2MKj1S7iHeqt0WGpW7rzLIn8rBNXpeYnpej_Tso1Mp3rRxGhujshBkxBRhZk1WcdXYajA1utC5P1JkBhTmBJgAFFBjNMIj3B9zfN3U:1u23mP:PjtpSSSoyQfka1SgbWH2hYXDC7IyJFes-3aL-gvmvV4', '2025-04-22 07:53:57.083641'),
('4hwhj66x79y5xlf2nbmkmniw4f20o2tr', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1uRLBn:EYYJt33KCwRofcX4bYUrhF68YZHdj8KgX6Jt5jEDF40', '2025-07-01 01:32:39.668871'),
('4s3aipqb1ogpw08e2cq1yg9iishy5d1d', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1uYwXK:0QdftT9ozPkvz36EkNGQFXMX1lMWHD8m48hVrSmaf8g', '2025-07-22 00:50:18.822374'),
('8tem2mckhoob5v4hz26gvy94h0exaest', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1vuOnP:6T6XSE6krOvG29ofB4U-rYi_XRLG6GbhippU-IOu2jE', '2026-03-09 05:47:51.400602'),
('bkkn8at66di6xfwi60l837pri338nirk', '.eJxVjMsOwiAQRf-FtSFMC2Vw6d5vIDM8pGpoUtqV8d-VpAvdnnPufQlP-1b83tLq5yjOQovTL2MKj1S7iHeqt0WGpW7rzLIn8rBNXpeYnpej_Tso1Mp3rRxGhujshBkxBRhZk1WcdXYajA1utC5P1JkBhTmBJgAFFBjNMIj3B9zfN3U:1u47L9:QRtuRYB0bN01afhs-ZyQwNGDo_S-GaNKYh2PQDLTNIk', '2025-04-28 00:06:19.635940'),
('eyzmsnwpn85qrdqytl89rgnz041l9vm2', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1uJoXE:ZSEUQ6Qt3M3-kDvzWtofePXPSFgEhU6O_QSgX4WYmV4', '2025-06-10 07:15:40.808853'),
('fpl18afpxpgzh1qutk0krq5dbslrxea6', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZmYAqRpISrsy3l2bdKHb_977LzXSupRx7Wkep6guyqrD78Ykj1Q3EO9Ub01Lq8s8sd4UvdOuhxbT87q7fweFevnWAh7ZmMCAhOzSiQMAeZ-CNxmtJQd0tGQcS0IK0SEQYMhW3Fk4ZvX-ANvOOBs:1tvqgr:ohnWQ5kEizCX0MkvUKuTTXfRwxVMlYTj5jgWeOPtl1Q', '2025-04-05 04:42:33.783855'),
('fptlk09y75ro21sqvgui5ua6dkk0it6w', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1u9xMV:hApEDaywg2x9qIkowIXTzGd28LYn0clCEXvES40UxwQ', '2025-05-14 02:39:51.447257'),
('hhdi84dppkbhxy6nrjwskcqa731yqjvt', '.eJxVjMsOwiAQRf-FtSFMC2Vw6d5vIDM8pGpoUtqV8d-VpAvdnnPufQlP-1b83tLq5yjOQovTL2MKj1S7iHeqt0WGpW7rzLIn8rBNXpeYnpej_Tso1Mp3rRxGhujshBkxBRhZk1WcdXYajA1utC5P1JkBhTmBJgAFFBjNMIj3B9zfN3U:1uPcSU:auY3E5acZrM7Td0U9Qim14BXr0WF7BK9_suv7vTAEnY', '2025-06-26 07:34:46.634954'),
('hroprjz8eu1wpo4fhagb1bj1r6d22z24', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1u2lcv:qygjVBC2qib-lJRfb7xFx67wlQttOc2EQnPWMvFQAbg', '2025-04-24 06:43:05.092500'),
('icf4oqvdpeov2abkxip89v8s0ncz9p4b', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1twVCT:feOo0IL2YjSFrJmNl-2417o9cyAQenrb4dWq8gCebJk', '2025-04-06 23:57:53.224145'),
('l6h2lo728uy1xjx4xyqjktl0t1l0qc9l', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1u1b0C:7pwLCPDpqbw-1PprqHuxm3_mVMfiLhfyliZmZWGeIe4', '2025-04-21 01:10:16.072370'),
('mkoym43hm28k1fi1hypk6c9n8egnl1ei', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1u7q1e:Q-Obaz25GYGJWsjstPHourhtHJ2HwqFSgtuValp_EWc', '2025-05-08 06:25:34.886545'),
('o88w2jd16fk1tl219g0pr3twdzh5tu7z', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1vlT9z:GFG7GlzIIlcija7ovKLItt6AOHdFFIVFSxGN-LQz1e8', '2026-02-12 14:38:15.380107'),
('olixreybdtuua3yzb9xamm7r5xthtjba', '.eJxVjMsOwiAQRf-FtSFMC2Vw6d5vIDM8pGpoUtqV8d-VpAvdnnPufQlP-1b83tLq5yjOQovTL2MKj1S7iHeqt0WGpW7rzLIn8rBNXpeYnpej_Tso1Mp3rRxGhujshBkxBRhZk1WcdXYajA1utC5P1JkBhTmBJgAFFBjNMIj3B9zfN3U:1uJSHO:tlfjggXGWIQmC0ERBuvdw8uMYiYUv2EbEJhE0DQ-zFs', '2025-06-09 07:29:50.755045'),
('qluav472qhpv2cyqwvfx2t4pvv39c5bi', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1uEFpy:9kMIICCXJzM3-HgAftMZR0d9uBhxoGAVqYbNoaxnbQM', '2025-05-25 23:12:02.570668'),
('rd2t8os2i6wfganmk7vwif5my76na0wy', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1uhkSA:3-BiTFr-HmyxZnEM8pJP8hrC09HQLOWmtXAHmzxWASU', '2025-08-15 07:45:22.613566'),
('rz04ujgfkc675f7xrzvuvi65j5gvivq8', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1wCugU:5gbCw7cNSsqmDXUd5j-IESNf8t9nHeETgtP6rzaUjLI', '2026-04-29 07:29:14.557868'),
('tf3tq23vtyxcr7ot686vs7p5nen5soj5', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1uJSQC:-zBaXxUIkB57f4tsr-oSHyG72-CooqOrf1anVwS2a-8', '2025-06-09 07:38:56.676130'),
('ucgn9bm2jhsvp9pya6lo44y29dvongzl', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1w4TcG:xsP69dK45mP90jiDdScRcV0QK016DR7UskXT9VvliKg', '2026-04-06 00:58:00.209998'),
('wm08z5t92m6zgm7srje97wly26ichuh6', '.eJxVjMsOwiAQRf-FtSFMC2Vw6d5vIDM8pGpoUtqV8d-VpAvdnnPufQlP-1b83tLq5yjOQovTL2MKj1S7iHeqt0WGpW7rzLIn8rBNXpeYnpej_Tso1Mp3rRxGhujshBkxBRhZk1WcdXYajA1utC5P1JkBhTmBJgAFFBjNMIj3B9zfN3U:1u9vq2:Qo6NWjaBPrSAPZ18ZUj1BTvOs7Nn8qFUhO4_FzPN-Mw', '2025-05-14 01:02:14.840087'),
('yg1pnjv45toqc191kpbzlsn5qff07woc', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1wRJwb:eToDmnUGgwANCIkX_r4ONS95TSayHnKukwyiNpkdW9k', '2026-06-08 01:17:25.752528'),
('yyq620j1qx6gzlie98n12xkowsh63ucu', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1wm4Ci:MF90C_gGC6yB0SLTqJovEaQ2Q0oYxsmRumFJtwegT0o', '2026-08-04 06:43:48.108660'),
('zlrwy5baw2p9rqxr4ymk0hypa0ur8ec2', '.eJxVjE0OwiAYBe_C2hACbQGX7j0D-f6QqoGktCvj3bVJF7p9M_NeKsG2lrR1WdLM6qysOv1uCPSQugO-Q701Ta2uy4x6V_RBu742luflcP8OCvTyrUcz-FGEbPaRPRJYjA6HIM4HiCwUMg4mozF-AoNkI9BkXAZhh06cen8A_7w46w:1ucb61:sL98I2ARZrMo99U9EzsFxtiy96ntZy4b5PG98A_6Edo', '2025-08-01 02:45:13.721969'),
('zqofx536fk6vcy2lnp0zydx7kjmz4a61', '.eJxVjEEOwiAQRe_C2hBBcBiX7nuGZgYGqRpISrsy3l2bdKHb_977LzXSupRx7TKPU1IXZdThd2OKD6kbSHeqt6Zjq8s8sd4UvdOuh5bked3dv4NCvXzrCB7ZmMCAhOzkxAGAvJfgTUZryQEdLRnHUZBCcggEGLKN7hw5ZfX-ANs1OBo:1wtaUp:l7VRUvB3sMBaunFIQXB0z5oGNuMmEDSBRkn2a8rdLFo', '2026-08-25 00:37:35.872402');

-- --------------------------------------------------------

--
-- Table structure for table `django_summernote_attachment`
--

CREATE TABLE `django_summernote_attachment` (
  `id` bigint NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_agenda`
--

CREATE TABLE `event_agenda` (
  `id` bigint NOT NULL,
  `title` varchar(255) NOT NULL,
  `title_slug` varchar(255) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `is_cancel` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` varchar(20) NOT NULL,
  `observation` longtext,
  `institution_id` bigint NOT NULL,
  `catagenda_id` bigint NOT NULL,
  `meeting_type_id` varchar(255) NOT NULL,
  `attachment` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `event_agenda`
--

INSERT INTO `event_agenda` (`id`, `title`, `title_slug`, `start_time`, `end_time`, `is_cancel`, `is_active`, `created_at`, `updated_at`, `user_id`, `location`, `status`, `observation`, `institution_id`, `catagenda_id`, `meeting_type_id`, `attachment`) VALUES
(7, 'Timor-Leste Economic Performance 2024-Report', 'timor-leste-economic-performance-2024-report', '2025-03-21 08:30:00.000000', '2025-03-21 11:30:00.000000', 0, 1, '2025-03-24 07:10:40.306137', '2025-05-27 07:17:00.112984', 1, 'Ministry of Finance', 'Read', '<p>LA ATENDE</p>', 1, 2, '1', ''),
(8, 'Lansamento Be\'e Moos no Sanitasaun', 'lansamento-bee-moos-no-sanitasaun', '2025-03-21 09:30:00.000000', '2025-03-21 12:00:00.000000', 0, 1, '2025-03-24 07:13:12.375953', '2025-03-28 06:44:19.434740', 2, 'Hera', 'Read', '<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Baseia ba encontro nebe realiza iha dia 13/3/2025&nbsp; nebe propoin husi&nbsp; MOP (DNRAS- BTL ) - UNICEF</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Objectivo</span></strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\"> husi encontro ida nee :</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Konvida Sua Exc. Sr. Samuel Marcal (Ministro das Obras Publicas ) atu marka Prezensa iha dia 21 de Marsu 2025 hodi asina Akordo&nbsp; entre parte rua MOP no UNICEF.&nbsp;</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">&nbsp;</span>Assunto sobre</strong> :</p>\r\n<ol style=\"margin-top: 0cm;\" type=\"1\">\r\n<li class=\"MsoNormal\" style=\"text-align: left;\">servisu bee no saniamento basika no&nbsp;<em>Climate Resilient&nbsp; wate</em>r ( <em>include Children in Schools/ECD and families in HCFs</em>) iha 2025 foka ba Municipio neen&nbsp; &nbsp; hanesan Aileu, Ainaro, Dili, Ermera<strong> &nbsp;Lautem</strong> no Viqueque (hare liu ba&nbsp; area rural)</li>\r\n<li class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Plano Orsamento ba tinan 2025 hamutuk : $1,236,478.27</span></li>\r\n</ol>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Resume :&nbsp;</span></strong></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Plano servisu anual 2025 Aprovado&nbsp; &nbsp;iha <strong>21/3/2025</strong></span></p>', 2, 2, '2', NULL),
(9, 'Komemorasaun loron Mundial Floresta', 'komemorasaun-loron-mundial-floresta', '2025-03-21 14:00:00.000000', '2025-03-21 16:00:00.000000', 0, 1, '2025-03-24 07:14:26.024389', '2025-03-28 06:44:10.022009', 2, 'Area Balak, Suco Ai Teas,Municipio Manatutu', 'Read', '<p>la partisipa</p>', 3, 2, '3', NULL),
(10, 'Inaugural Celebration of Our new AIRBUS A319', 'inaugural-celebration-of-our-new-airbus-a319', '2025-03-21 17:00:00.000000', '2025-03-21 18:00:00.000000', 0, 1, '2025-03-24 07:15:36.262999', '2025-03-28 06:42:12.035633', 2, 'Presidente Nicolau Lobato International Airport, Dili, Timor-Leste', 'Read', '<p>La marka prezensa</p>', 4, 2, '2', NULL),
(11, 'Lansamento Programa PARTISIPA', 'lansamento-programa-partisipa', '2025-03-25 10:00:00.000000', '2025-03-25 12:00:00.000000', 0, 1, '2025-03-24 07:16:26.949392', '2025-03-28 06:43:34.988746', 2, 'Ermera,Gleno', 'Read', '<p>informasaun badak&nbsp; :&nbsp;</p>\r\n<p>Lansamento nee responde ba aprenzentasaun sobre utilizasaun material<em><strong> Fiber Reinforced Concrete (FRC)</strong></em> nebe aprezentasa husi Eng. Santino ho nia ekipa iha dia 11 de Marsu 2025 nebe hetan apoio husi&nbsp; Fundo DFAT liu husi PARTISIPA&nbsp; ba projecto<strong> Rehabilitasaun&nbsp; Estrada Rural Railako Ermera.</strong></p>\r\n<p><strong>pavimento FRC mak&nbsp; </strong>pavimemto betaun simentado nebe&nbsp; halo husi betaun kahur ho fibra sintetiku hanesan ajente nebe&nbsp; halo forsa.</p>\r\n<p>kompozisaun material :&nbsp;</p>\r\n<p>Pavimento FRC = Cement (Simentu) + Sand (raihenek) +Course Aggregate (agregado grosu) + Concrete Fibre + Water (Bee)&nbsp;</p>\r\n<p>plano ba aktividade servisu refere sei finaliza iha fim do Novembro 2025 .</p>\r\n<p>&nbsp;</p>', 5, 2, '3', NULL),
(12, 'The opening ceremony of the 6th Ministerial Meeting of G7+ \"15 years of unity: shaping the future of peace and resilience in the G7+ Countries\"', 'the-opening-ceremony-of-the-6th-ministerial-meeting-of-g7-15-years-of-unity-shaping-the-future-of-peace-and-resilience-in-the-g7-countries', '2025-04-11 09:00:00.000000', '2025-04-11 12:00:00.000000', 0, 1, '2025-04-01 06:30:20.232615', '2025-04-07 01:28:13.138356', 4, 'CCD', 'Read', NULL, 6, 2, '3', NULL),
(13, 'Welcome Dinner in honour of the g7+ delegations visiting for the 6th Ministerial Meeting in Timor-Leste', 'welcome-dinner-in-honour-of-the-g7-delegations-visiting-for-the-6th-ministerial-meeting-in-timor-leste', '2025-04-11 19:30:17.000000', '2025-04-11 21:30:17.000000', 0, 1, '2025-04-07 01:14:52.997595', '2025-04-07 01:27:31.927817', 4, 'CCD', 'Read', NULL, 6, 2, '3', NULL),
(14, 'Opening Ceremony and Gala Dinner \"Empowering Public Finance through Innovation and Collaboration', 'opening-ceremony-and-gala-dinner-empowering-public-finance-through-innovation-and-collaboration', '2025-04-06 18:30:47.000000', '2025-04-06 20:00:47.000000', 0, 1, '2025-04-07 01:31:00.462204', '2025-04-08 06:17:39.888249', 4, 'Hotel Timor,Dili', 'Read', NULL, 7, 2, '3', NULL),
(15, 'Opening Ceremony and Gala Dinner', 'opening-ceremony-and-gala-dinner', '2025-04-06 18:30:00.000000', '2025-04-06 18:30:00.000000', 0, 1, '2025-04-07 01:48:59.152254', '2025-04-07 01:48:59.152301', 4, 'CCD', 'Read', NULL, 7, 2, '3', NULL),
(16, 'Lansamento projeto melloramento sistema fornesimentu Bee moos iha P.A. Balibo, Munisipio Bobonaro', 'lansamento-projeto-melloramento-sistema-fornesimentu-bee-moos-iha-pa-balibo-munisipio-bobonaro', '2025-04-10 10:30:00.000000', '2025-04-10 12:30:00.000000', 0, 1, '2025-04-08 06:11:23.859303', '2025-04-10 06:49:10.473693', 4, 'Administrasaun Posto Balibo', 'Read', '', 8, 1, '2', NULL),
(17, 'an Anzac Day Dawn Service', 'an-anzac-day-dawn-service', '2025-04-25 05:45:00.000000', '2025-04-25 10:10:00.000000', 0, 1, '2025-04-09 01:10:08.164712', '2025-04-09 01:10:20.764106', 4, 'CCLN,Comoro,Dili', 'Read', NULL, 9, 2, '3', NULL),
(18, 'Retiru preparasaun selebra PASKOA ba funsionariu MOP 2025', 'retiru-preparasaun-selebra-paskoa-ba-funsionariu-mop-2025', '2025-04-11 08:00:00.000000', '2025-04-11 12:30:00.000000', 0, 1, '2025-04-10 06:25:01.170439', '2025-04-10 06:29:37.587011', 4, 'Salaun Laline-Larigutu-CNE, Dili', 'Read', NULL, 10, 1, '1', NULL),
(19, 'Komemora aniversario CCI-TL ba dala-15', 'komemora-aniversario-cci-tl-ba-dala-15', '2025-04-16 18:00:00.000000', '2025-04-16 18:00:00.000000', 0, 1, '2025-04-14 05:51:25.864420', '2025-04-14 06:10:21.529209', 4, 'Kampo Futsal Bebora,Dili', 'Read', NULL, 11, 2, '3', NULL),
(20, 'Encontro Coordenação konaba Titulu Rai, hamutuk ho MOP, Ministerio Justisa, MPIE, Sec Estado Terras e Propriedade, Sra. Lucia Lobato', 'encontro-coordenacao-konaba-titulu-rai-hamutuk-ho-mop-ministerio-justisa-mpie-sec-estado-terras-e-propriedade-sra-lucia-lobato', '2025-04-25 15:00:00.000000', '2025-04-25 17:00:00.000000', 0, 1, '2025-04-24 01:10:26.852424', '2025-05-13 05:48:19.459930', 4, 'Piso 10, Sala Executivo Ministério Finanças, Aitarak Laran', 'Read', NULL, 12, 2, '1', NULL),
(21, 'The Opening Ceremony MYEXPO Malaysia Expo Dili', 'the-opening-ceremony-myexpo-malaysia-expo-dili', '2025-05-09 15:00:00.000000', '2025-05-10 15:00:00.000000', 0, 1, '2025-05-06 01:23:28.326199', '2025-05-06 01:23:59.020992', 4, 'CCD', 'Read', NULL, 13, 2, '3', NULL),
(22, 'Reunião Encontro Final konaba preparasaun reunião Técnica e Ministerial PALOP-TL UE', 'reuniao-encontro-final-konaba-preparasaun-reuniao-tecnica-e-ministerial-palop-tl-ue', '2025-05-27 09:30:00.000000', '2025-05-27 12:00:00.000000', 0, 1, '2025-05-26 07:34:17.396065', '2025-05-26 07:34:28.254803', 4, 'MNEC-IED', 'Read', NULL, 14, 2, '1', NULL),
(23, 'Encontro  ho Conselho Consultivo MOP', 'encontro-ho-conselho-consultivo-mop', '2025-04-28 09:00:00.000000', '2025-04-28 13:00:00.000000', 0, 1, '2025-05-26 07:38:06.226078', '2025-05-30 01:51:07.636316', 4, 'Gabinete-MOP', 'Read', NULL, 15, 1, '1', 'agenda_files/Rezultado_ba_CC_MOP.pdf'),
(24, 'Meeting equipa ADB no atu informa progresso projeto estrada iha Hatubuilico-Letefoho Municipio Ermera', 'meeting-equipa-adb-no-atu-informa-progresso-projeto-estrada-iha-hatubuilico-letefoho-municipio-ermera', '2025-06-03 10:00:00.000000', '2025-06-03 11:00:03.000000', 0, 1, '2025-06-02 06:59:52.054573', '2025-06-02 07:00:02.015429', 4, 'Gabinete-MOP', 'Read', NULL, 17, 2, '1', ''),
(25, 'Request for a meeting with Excellency\'s convenience time, to update bilateral cooperation between Timor-Leste and Japan', 'request-for-a-meeting-with-excellencys-convenience-time-to-update-bilateral-cooperation-between-timor-leste-and-japan', '2025-06-03 11:00:00.000000', '2025-06-03 11:30:00.000000', 0, 1, '2025-06-02 07:06:31.424182', '2025-06-02 07:06:41.332869', 4, 'Gabinete-MOP', 'Read', NULL, 16, 2, '1', ''),
(26, 'Reuniao Jornadas Orsamentais tinan 2026', 'reuniao-jornadas-orsamentais-tinan-2026', '2025-06-12 09:00:00.000000', '2025-06-13 17:30:00.000000', 0, 1, '2025-06-12 07:37:06.182670', '2025-06-12 07:37:13.061809', 4, 'Ministerio Finansas Aitarak-laran', 'Read', NULL, 12, 2, '1', ''),
(27, 'Serimonia Selebrasaun 8 aniversario GMN nian', 'serimonia-selebrasaun-8-aniversario-gmn-nian', '2025-06-15 18:00:00.000000', '2025-06-15 20:00:00.000000', 0, 1, '2025-06-12 07:39:47.376405', '2025-06-12 07:47:52.645572', 4, 'Salaun Multiusos Bebora GMN', 'Read', NULL, 18, 2, '3', ''),
(28, 'Solicitasaun Tempo ba Abertura Workshop Konaba \"Formulating National Electricity Code & Development of Net Metering Policy in Timor-Leste\"', 'solicitasaun-tempo-ba-abertura-workshop-konaba-formulating-national-electricity-code-development-of-net-metering-policy-in-timor-leste', '2025-06-01 08:51:03.000000', '2025-06-04 08:52:03.000000', 0, 1, '2025-06-29 23:51:19.882958', '2025-06-29 23:51:19.882995', 4, 'Salaun Enkontru EDTL, E.P. Kaikoli', 'Read', NULL, 19, 1, '3', ''),
(29, 'Request for Participation- Site Visit Monitoring to Solar System installation at the National Institution of Pharmacy and Medical Products (INFPM)', 'request-for-participation-site-visit-monitoring-to-solar-system-installation-at-the-national-institution-of-pharmacy-and-medical-products-infpm', '2025-07-08 15:00:56.000000', '2025-07-08 15:01:56.000000', 0, 1, '2025-07-07 06:19:17.796748', '2025-07-07 06:19:39.155185', 4, 'INFPM', 'Read', NULL, 20, 2, '1', ''),
(30, 'Nomination of Potential Civil Servants for Tibar Port-Operation and Management Service Unit (TP-OMSU) Position', 'nomination-of-potential-civil-servants-for-tibar-port-operation-and-management-service-unit-tp-omsu-position', '2025-07-10 16:00:48.000000', '2025-07-10 16:01:48.000000', 0, 1, '2025-07-07 06:24:22.997539', '2025-07-07 06:24:51.763002', 4, 'Piso 10, Sala Executivo Ministério Finanças, Hudi-laran', 'Read', NULL, 21, 2, '1', ''),
(31, 'Aniversario CNC, I.P Memoria Koletiva dalan ba Rekonsiliasaun', 'aniversario-cnc-ip-memoria-koletiva-dalan-ba-rekonsiliasaun', '2025-07-11 15:46:00.000000', '2025-07-11 15:46:00.000000', 0, 1, '2025-07-07 06:28:20.265323', '2025-07-07 06:31:26.643466', 4, 'Salaun Konferensia CNC, I.P', 'Read', NULL, 22, 2, '3', ''),
(32, '14th Anniversary Celebration \"Digitalization is an Effective Contribution to Banking Development\"', '14th-anniversary-celebration-digitalization-is-an-effective-contribution-to-banking-development', '2025-07-12 15:33:42.000000', '2025-07-12 15:34:42.000000', 0, 1, '2025-07-07 06:36:35.836367', '2025-07-07 06:36:43.727453', 4, 'CCD', 'Read', NULL, 23, 2, '3', ''),
(33, 'Konvite Komemorasaun Loron Mundial Ai-Parapa', 'konvite-komemorasaun-loron-mundial-ai-parapa', '2026-07-28 09:00:00.000000', '2026-07-28 14:00:00.000000', 0, 1, '2026-07-20 01:33:23.407493', '2026-07-24 06:14:25.615867', 1, 'Lagoa BeeMalae, Municipio Bobonaro', 'Read', NULL, 3, 2, '3', 'agenda_files/Convite.pdf'),
(34, 'Serimonia Asinatura akordu Subvensaun entre Governu Timor-Leste no Grup Banco Mundial ba \"Grant Facility for project Preparation\"', 'serimonia-asinatura-akordu-subvensaun-entre-governu-timor-leste-no-grup-banco-mundial-ba-grant-facility-for-project-preparation', '2026-07-20 15:00:00.000000', '2026-07-20 16:30:00.000000', 1, 1, '2026-07-20 01:51:03.699573', '2026-07-20 02:01:52.103341', 1, 'Edificio Ministerio das Finansas, Auditorium Kay Rala Xanana Gusmão', 'Read', NULL, 12, 2, '1', ''),
(35, 'Serimonia Asinatura Akordu \"Grant facility for Project Preparation\"', 'serimonia-asinatura-akordu-grant-facility-for-project-preparation', '2026-07-20 15:00:00.000000', '2026-07-20 16:30:00.000000', 0, 1, '2026-07-20 02:01:14.616899', '2026-07-20 02:01:38.542089', 1, 'Edificio Ministerio das Finansas, Auditorium Kay Rala Xanana Gusmão', 'Read', NULL, 12, 2, '3', 'agenda_files/Convite_MF.pdf'),
(36, 'Housing Finance Market Assessment', 'housing-finance-market-assessment', '2026-07-28 15:30:00.000000', '2026-07-28 16:30:00.000000', 0, 1, '2026-07-21 00:37:03.616975', '2026-07-21 00:37:22.886560', 1, 'Ministry of Public Work Office', 'Read', NULL, 23, 2, '1', 'agenda_files/Convite_BCTL.pdf'),
(37, 'Konvite ba Partisipasaun iha Konsultasaun Publika no Vizita ba Fatin Projeitu, konaba Proposta projeitu Konstrusaun Rezervatoriu Armazenamentu Kombustivel nian husi SACOM Energia,Lda', 'konvite-ba-partisipasaun-iha-konsultasaun-publika-no-vizita-ba-fatin-projeitu-konaba-proposta-projeitu-konstrusaun-rezervatoriu-armazenamentu-kombustivel-nian-husi-sacom-energialda', '2026-07-30 09:00:00.000000', '2026-07-30 12:00:00.000000', 0, 1, '2026-07-24 06:20:39.246207', '2026-07-24 06:20:53.508881', 1, 'Sede Suku Betano, Postu Administrativu Same, Munisipiu Manufahi, Timor-Leste', 'Read', NULL, 24, 2, '1', 'agenda_files/Convite_ANP.pdf'),
(38, 'Inauguration, Blessing and Eucharistic Celebration', 'inauguration-blessing-and-eucharistic-celebration', '2026-07-31 08:45:00.000000', '2026-07-31 12:45:00.000000', 0, 1, '2026-07-24 06:22:48.760624', '2026-07-24 06:23:10.668833', 1, 'Centro de Espiritualidade Inaciana para a Paz e Reconciliação (CEIPAR) Hera, Dili, Timor-Leste', 'Read', NULL, 25, 2, '3', 'agenda_files/Convite_CEIPAR_JESUITAS.pdf'),
(39, 'Launch of Commercial Services of Cabos de Timor-Leste,E.P.', 'launch-of-commercial-services-of-cabos-de-timor-lesteep', '2026-07-28 10:00:00.000000', '2026-07-28 11:40:00.000000', 0, 1, '2026-07-27 02:32:15.668130', '2026-07-27 02:32:23.389745', 1, 'CTL Headquarters Bebonuk, Dili', 'Read', NULL, 26, 2, '2', 'agenda_files/Convite_CTL.pdf'),
(40, 'Cerimonia de Despedida dos Bolseiros de Merito do FDCH', 'cerimonia-de-despedida-dos-bolseiros-de-merito-do-fdch', '2026-08-06 15:30:00.000000', '2026-08-06 17:30:00.000000', 0, 1, '2026-07-28 07:40:13.591746', '2026-07-28 07:54:23.875459', 1, 'Salao GMTV em Bebora, Dili', 'Read', NULL, 27, 2, '3', 'agenda_files/Convite_MPIE.pdf'),
(41, 'V. Excelência para o Jantar de Gala no Âmbito da XIII Reunião de Ministros do Turismo da Comunidade dos Países de Língua Portuguesa - CPLP', 'v-excelencia-para-o-jantar-de-gala-no-ambito-da-xiii-reuniao-de-ministros-do-turismo-da-comunidade-dos-paises-de-lingua-portuguesa-cplp', '2026-07-30 19:00:00.000000', '2026-07-30 19:01:00.000000', 0, 1, '2026-07-28 07:53:49.100870', '2026-07-28 07:54:23.880082', 1, 'Centro de Convenções de Dili (CCD), Dili', 'Read', NULL, 28, 2, '3', 'agenda_files/Convite_MCAE_e_MTA.pdf'),
(42, 'Return to Dili and Availability to meet - Dili Sanitation Project', 'return-to-dili-and-availability-to-meet-dili-sanitation-project', '2026-08-10 10:00:00.000000', '2026-08-10 12:00:00.000000', 0, 1, '2026-07-28 08:01:20.530786', '2026-07-28 08:01:33.442912', 1, 'Ministerio das Obras Publicas', 'Read', NULL, 29, 2, '1', 'agenda_files/Convite_NICOLAS_O_DWYER.pdf'),
(43, 'Serimonia Agradesimentu 40 dias ba Ex-Prezidente Republika no Prezidente FRETILIN', 'serimonia-agradesimentu-40-dias-ba-ex-prezidente-republika-no-prezidente-fretilin', '2026-08-07 20:00:00.000000', '2026-08-08 15:00:00.000000', 0, 1, '2026-08-03 01:32:06.554217', '2026-08-03 01:32:57.917123', 1, 'Catedral Imaculada da Conceição, Vila Verde, Dili', 'Read', NULL, 30, 2, '3', 'agenda_files/Convite_Dr._Lu-Olo.pdf'),
(44, 'Invitation to the Inauguration Ceremony and Symbolic Handover of 12 Community Infrastructure Units', 'invitation-to-the-inauguration-ceremony-and-symbolic-handover-of-12-community-infrastructure-units', '2026-08-06 10:00:00.000000', '2026-08-06 13:30:00.000000', 0, 1, '2026-08-03 23:57:41.723651', '2026-08-03 23:58:13.590388', 1, 'Water Supply System, in Suco Lelaufe, Nitibe, Oecussi Municipality', 'Read', NULL, 31, 2, '3', 'agenda_files/Convite_UNDP.pdf'),
(45, 'Konvite atu Prezide Serimonia Loke Drag Bike Ermera 2026 Comemorasaun 30 de Agostu \"Consulta Popular\"', 'konvite-atu-prezide-serimonia-loke-drag-bike-ermera-2026-comemorasaun-30-de-agostu-consulta-popular', '2026-09-03 07:00:00.000000', '2026-09-03 19:00:00.000000', 0, 1, '2026-08-05 06:10:45.161794', '2026-08-05 06:11:16.063355', 1, 'Gleno Vila, Munisipiu Ermera, Timor-Leste', 'Read', NULL, 32, 2, '3', 'agenda_files/Convite_FMCTL.pdf'),
(46, 'Para Participar nas Comemorações do 17 Aniversario da UEP nos dias 13 e 14 de Agosto de 2026', 'para-participar-nas-comemoracoes-do-17-aniversario-da-uep-nos-dias-13-e-14-de-agosto-de-2026', '2026-08-13 09:00:00.000000', '2026-08-14 09:05:00.000000', 0, 1, '2026-08-11 01:12:38.457009', '2026-08-11 01:15:38.070193', 1, 'Igreja Motael no Quartel da UEP Bairro Pite', 'Read', NULL, 33, 2, '3', 'agenda_files/Convite_PNTL.pdf'),
(47, 'Serimonia Lansamentu Kartaun MasterCard no Inaugurasaun Edifisiu foun BNCTL Sukursal Liquiça', 'serimonia-lansamentu-kartaun-mastercard-no-inaugurasaun-edifisiu-foun-bnctl-sukursal-liquica', '2026-08-14 08:30:00.000000', '2026-08-14 13:00:00.000000', 0, 1, '2026-08-11 01:20:19.913055', '2026-08-11 01:21:37.766999', 1, 'Edifisiu foun BNCTL Sukursal Liquiça iha Aldeia Leopa, Suku Dato, Postu Adm. Liquiça, Munisipiu Liquiça', 'Read', NULL, 1, 2, '2', 'agenda_files/Convite_BNCTL.pdf'),
(48, 'Cerimonia Lançamento Primeira Pedra Construção Esquema Irrigação de Maukolo-Lomea Municipio Covalima', 'cerimonia-lancamento-primeira-pedra-construcao-esquema-irrigacao-de-maukolo-lomea-municipio-covalima', '2026-08-15 09:30:00.000000', '2026-08-15 14:00:00.000000', 0, 1, '2026-08-11 01:26:09.223252', '2026-08-11 01:26:23.893730', 1, 'Maukola, Suco Beco, Postu Adm. de Suai Vila, Municipio de Covalima', 'Read', NULL, 3, 2, '2', 'agenda_files/Convite_MAPPF-1.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `event_catagenda`
--

CREATE TABLE `event_catagenda` (
  `id` bigint NOT NULL,
  `name_category` varchar(200) NOT NULL,
  `name_category_slug` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `event_catagenda`
--

INSERT INTO `event_catagenda` (`id`, `name_category`, `name_category_slug`) VALUES
(1, 'Internal', 'internal'),
(2, 'Eksternal', 'eksternal');

-- --------------------------------------------------------

--
-- Table structure for table `event_commentinformative`
--

CREATE TABLE `event_commentinformative` (
  `id` bigint NOT NULL,
  `created_on` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `informative_id` bigint NOT NULL,
  `problems` longtext NOT NULL DEFAULT (_utf8mb3''),
  `results` longtext NOT NULL DEFAULT (_utf8mb3''),
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_histagenda`
--

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
  `user_id` bigint NOT NULL,
  `institution` varchar(255) DEFAULT NULL,
  `catagenda` varchar(25) DEFAULT NULL,
  `meeting_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `event_histagenda`
--

INSERT INTO `event_histagenda` (`id`, `location_new`, `created_at`, `updated_at`, `end_time`, `end_time_new`, `is_active`, `is_cancel`, `location`, `observation`, `start_time`, `start_time_new`, `status`, `title`, `title_slug`, `user_id`, `institution`, `catagenda`, `meeting_type`) VALUES
(7, 'Ministry of Finance', '2025-03-24 07:10:40.318194', '2025-05-27 07:17:00.123363', '2025-03-21 11:30:00.000000', '2025-03-21 11:30:00.000000', 1, 0, 'Ministry of Finance', '<p>LA ATENDE</p>', '2025-03-21 08:30:00.000000', '2025-03-21 08:30:00.000000', 'Read', 'Timor-Leste Economic Performance 2024-Report', 'timor-leste-economic-performance-2024-report', 1, 'Banco Nacional de Comércio de Timor-Leste (BNCTL)', 'Eksternal', '-'),
(8, 'Hera', '2025-03-24 07:13:12.384965', '2025-03-25 00:44:20.244947', '2025-03-21 12:00:00.000000', '2025-03-21 12:00:00.000000', 1, 0, 'Hera', '<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Baseia ba encontro nebe realiza iha dia 13/3/2025&nbsp; nebe propoin husi&nbsp; MOP (DNRAS- BTL ) - UNICEF</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Objectivo</span></strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\"> husi encontro ida nee :</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Konvida Sua Exc. Sr. Samuel Marcal (Ministro das Obras Publicas ) atu marka Prezensa iha dia 21 de Marsu 2025 hodi asina Akordo&nbsp; entre parte rua MOP no UNICEF.&nbsp;</span></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">&nbsp;</span>Assunto sobre</strong> :</p>\r\n<ol style=\"margin-top: 0cm;\" type=\"1\">\r\n<li class=\"MsoNormal\" style=\"text-align: left;\">servisu bee no saniamento basika no&nbsp;<em>Climate Resilient&nbsp; wate</em>r ( <em>include Children in Schools/ECD and families in HCFs</em>) iha 2025 foka ba Municipio neen&nbsp; &nbsp; hanesan Aileu, Ainaro, Dili, Ermera<strong> &nbsp;Lautem</strong> no Viqueque (hare liu ba&nbsp; area rural)</li>\r\n<li class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Plano Orsamento ba tinan 2025 hamutuk : $1,236,478.27</span></li>\r\n</ol>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><strong><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Resume :&nbsp;</span></strong></p>\r\n<p class=\"MsoNormal\" style=\"text-align: left;\"><span lang=\"PT\" style=\"mso-ansi-language: PT;\">Plano servisu anual 2025 Aprovado&nbsp; &nbsp;iha <strong>21/3/2025</strong></span></p>', '2025-03-21 09:30:00.000000', '2025-03-21 09:30:00.000000', 'Read', 'Lansamento Be\'e Moos no Sanitasaun', 'lansamento-bee-moos-no-sanitasaun', 1, 'United Nations Children\'s Fund (UNICEF)-(DNRAS)', 'Eksternal', '-'),
(9, 'Area Balak, Suco Ai Teas,Municipio Manatutu', '2025-03-24 07:14:26.036764', '2025-03-28 05:52:43.785376', '2025-03-21 16:00:00.000000', '2025-03-21 16:00:00.000000', 1, 0, 'Area Balak, Suco Ai Teas,Municipio Manatutu', '<p>la partisipa</p>', '2025-03-21 14:00:00.000000', '2025-03-21 14:00:00.000000', 'Read', 'Komemorasaun loron Mundial Floresta', 'komemorasaun-loron-mundial-floresta', 1, 'Ministerio da Agricultura Pecuarioa Pesca e Floresta', 'Eksternal', '-'),
(10, 'Presidente Nicolau Lobato International Airport, Dili, Timor-Leste', '2025-03-24 07:15:36.273569', '2025-03-28 05:53:02.966406', '2025-03-21 18:00:00.000000', '2025-03-21 18:00:00.000000', 1, 0, 'Presidente Nicolau Lobato International Airport, Dili, Timor-Leste', '<p>La marka prezensa</p>', '2025-03-21 17:00:00.000000', '2025-03-21 17:00:00.000000', 'Read', 'Inaugural Celebration of Our new AIRBUS A319', 'inaugural-celebration-of-our-new-airbus-a319', 1, 'Aero Dili', 'Eksternal', '-'),
(11, 'Ermera,Gleno', '2025-03-24 07:16:26.957132', '2025-03-26 00:22:49.064935', '2025-03-25 12:00:00.000000', '2025-03-25 12:00:00.000000', 1, 0, 'Ermera,Gleno', '<p>informasaun badak&nbsp; :&nbsp;</p>\r\n<p>Lansamento nee responde ba aprenzentasaun sobre utilizasaun material<em><strong> Fiber Reinforced Concrete (FRC)</strong></em> nebe aprezentasa husi Eng. Santino ho nia ekipa iha dia 11 de Marsu 2025 nebe hetan apoio husi&nbsp; Fundo DFAT liu husi PARTISIPA&nbsp; ba projecto<strong> Rehabilitasaun&nbsp; Estrada Rural Railako Ermera.</strong></p>\r\n<p><strong>pavimento FRC mak&nbsp; </strong>pavimemto betaun simentado nebe&nbsp; halo husi betaun kahur ho fibra sintetiku hanesan ajente nebe&nbsp; halo forsa.</p>\r\n<p>kompozisaun material :&nbsp;</p>\r\n<p>Pavimento FRC = Cement (Simentu) + Sand (raihenek) +Course Aggregate (agregado grosu) + Concrete Fibre + Water (Bee)&nbsp;</p>\r\n<p>plano ba aktividade servisu refere sei finaliza iha fim do Novembro 2025 .</p>\r\n<p>&nbsp;</p>', '2025-03-25 10:00:00.000000', '2025-03-25 10:00:00.000000', 'Pending', 'Lansamento Programa PARTISIPA', 'lansamento-programa-partisipa', 1, 'PARTISIPA', 'Eksternal', '-'),
(16, 'Administrasaun Posto Balibo', '2025-04-08 06:11:23.874012', '2025-04-08 06:11:23.874034', '2025-04-10 12:30:00.000000', '2025-04-10 12:30:00.000000', 1, 0, 'Administrasaun Posto Balibo', NULL, '2025-04-10 10:30:00.000000', '2025-04-10 10:30:00.000000', 'Pending', 'Lansamento projeto melloramento sistema fornesimentu Bee moos iha P.A. Balibo, Munisipio Bobonaro', 'lansamento-projeto-melloramento-sistema-fornesimentu-bee-moos-iha-pa-balibo-munisipio-bobonaro', 4, 'BTL.EP', 'Internal', 'Lansamentu');

-- --------------------------------------------------------

--
-- Table structure for table `event_informative`
--

CREATE TABLE `event_informative` (
  `id` bigint NOT NULL,
  `title` varchar(255) NOT NULL,
  `title_slug` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_done` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `is_comment` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_requestagenda`
--

CREATE TABLE `event_requestagenda` (
  `id` bigint NOT NULL,
  `title` varchar(255) NOT NULL,
  `title_slug` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `catagenda_id` bigint DEFAULT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `institution_id` bigint DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_typeagenda`
--

CREATE TABLE `event_typeagenda` (
  `id` bigint NOT NULL,
  `name_type` varchar(200) NOT NULL,
  `name_type_slug` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `event_typeagenda`
--

INSERT INTO `event_typeagenda` (`id`, `name_type`, `name_type_slug`) VALUES
(1, 'Enkontru', 'enkontru'),
(2, 'Lansamentu', 'lansamentu'),
(3, 'Seluk-Seluk', 'seluk-seluk');

-- --------------------------------------------------------

--
-- Table structure for table `event_yearagenda`
--

CREATE TABLE `event_yearagenda` (
  `id` bigint NOT NULL,
  `year` int NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `event_yearagenda`
--

INSERT INTO `event_yearagenda` (`id`, `year`, `is_active`) VALUES
(1, 2025, 1),
(2, 2024, 0),
(3, 2023, 0),
(4, 2022, 0),
(5, 2026, 1);

-- --------------------------------------------------------

--
-- Table structure for table `institute_attendence`
--

CREATE TABLE `institute_attendence` (
  `id` bigint NOT NULL,
  `name_attendence` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `institute_departmentadn`
--

CREATE TABLE `institute_departmentadn` (
  `id` bigint NOT NULL,
  `name_department` varchar(255) DEFAULT NULL,
  `unitadn_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `institute_institution`
--

CREATE TABLE `institute_institution` (
  `id` bigint NOT NULL,
  `name_institution` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `institute_institution`
--

INSERT INTO `institute_institution` (`id`, `name_institution`) VALUES
(1, 'Banco Nacional de Comércio de Timor-Leste (BNCTL)'),
(2, 'United Nations Children\'s Fund (UNICEF)-(DNRAS)'),
(3, 'Ministerio da Agricultura Pecuarioa Pesca e Floresta'),
(4, 'Aero Dili'),
(5, 'PARTISIPA'),
(6, 'G7+'),
(7, 'FreeBalance International Steering Committee'),
(8, 'BTL.EP'),
(9, 'Embassy New Zealand'),
(10, 'Gabinete DGAF'),
(11, 'CCI-TL'),
(12, 'Ministerio das Financas'),
(13, 'Embassy Malaysia'),
(14, 'Ministerio dos Negocios e Estrangeiros'),
(15, 'Gabinete MOP'),
(16, 'Embassy Japan'),
(17, 'Asean Development Bank (ADB)'),
(18, 'GMN-TV'),
(19, 'DGREAS'),
(20, 'Institution of Pharmacy and Medical Products (INFPM)'),
(21, 'Project Management Unit-Tibar Bay Port'),
(22, 'CNC.IP'),
(23, 'Banco Nacional de Timor-Leste (BCTL)'),
(24, 'Autoridade Nacional Petroleo'),
(25, 'Centro de Espiritualidade Inaciana para a Paz e Reconiliação (CEIPAR-JESUITAS)'),
(26, 'Cabos de Timor-Leste, E.P.'),
(27, 'Ministerio do Planeamento e Investimento Estrategico'),
(28, 'Ministerio Coordenador dos Asuntos Economicos e Ministerio do Turismo e Ambiente'),
(29, 'NICOLAS 0 DWYER'),
(30, 'Familia Nobre Guterres no Fretilin'),
(31, 'United Nations Development Programme (UNDP)'),
(32, 'Federação de Motociclismo de Timor-Leste'),
(33, 'Polisia Nacional de Timor-Leste (PNTL)');

-- --------------------------------------------------------

--
-- Table structure for table `institute_unitadn`
--

CREATE TABLE `institute_unitadn` (
  `id` bigint NOT NULL,
  `name_unit` varchar(255) DEFAULT NULL,
  `abreviation` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reports_logo`
--

CREATE TABLE `reports_logo` (
  `id` bigint NOT NULL,
  `logo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `reports_logo`
--

INSERT INTO `reports_logo` (`id`, `logo`) VALUES
(7, 'logo/logo-mop.png');

-- --------------------------------------------------------

--
-- Table structure for table `reports_mensual`
--

CREATE TABLE `reports_mensual` (
  `id` bigint NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `name_slug` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reports_semestral`
--

CREATE TABLE `reports_semestral` (
  `id` bigint NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `name_slug` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reports_trimestral`
--

CREATE TABLE `reports_trimestral` (
  `id` bigint NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `name_slug` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authentication_user`
--
ALTER TABLE `authentication_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `authentication_user_groups`
--
ALTER TABLE `authentication_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `authentication_user_groups_user_id_group_id_8af031ac_uniq` (`user_id`,`group_id`),
  ADD KEY `authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `authentication_user_user_permissions`
--
ALTER TABLE `authentication_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `authentication_user_user_user_id_permission_id_ec51b09f_uniq` (`user_id`,`permission_id`),
  ADD KEY `authentication_user__permission_id_ea6be19a_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_authentication_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `django_summernote_attachment`
--
ALTER TABLE `django_summernote_attachment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `event_agenda`
--
ALTER TABLE `event_agenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `title_slug` (`title_slug`),
  ADD KEY `event_agenda_user_id_03c3c67b_fk_authentication_user_id` (`user_id`),
  ADD KEY `event_agenda_institution_id_a6ce7188_fk_institute_institution_id` (`institution_id`),
  ADD KEY `event_agenda_catagenda_id_11e15102_fk_event_catagenda_id` (`catagenda_id`);

--
-- Indexes for table `event_catagenda`
--
ALTER TABLE `event_catagenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name_category` (`name_category`),
  ADD UNIQUE KEY `name_category_slug` (`name_category_slug`);

--
-- Indexes for table `event_commentinformative`
--
ALTER TABLE `event_commentinformative`
  ADD PRIMARY KEY (`id`),
  ADD KEY `event_commentinforma_informative_id_116a69a0_fk_event_inf` (`informative_id`),
  ADD KEY `event_commentinforma_user_id_e0c51b0e_fk_authentic` (`user_id`);

--
-- Indexes for table `event_histagenda`
--
ALTER TABLE `event_histagenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `title_slug` (`title_slug`),
  ADD KEY `event_histagenda_user_id_40e3c3f9_fk_authentication_user_id` (`user_id`);

--
-- Indexes for table `event_informative`
--
ALTER TABLE `event_informative`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `title_slug` (`title_slug`),
  ADD KEY `event_informative_user_id_0bc0c75a_fk_authentication_user_id` (`user_id`);

--
-- Indexes for table `event_requestagenda`
--
ALTER TABLE `event_requestagenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `title_slug` (`title_slug`),
  ADD KEY `event_requestagenda_user_id_ef784f47_fk_authentication_user_id` (`user_id`),
  ADD KEY `event_requestagenda_catagenda_id_cd1b6485_fk_event_catagenda_id` (`catagenda_id`),
  ADD KEY `event_requestagenda_institution_id_2f1cf5c3_fk_institute` (`institution_id`);

--
-- Indexes for table `event_typeagenda`
--
ALTER TABLE `event_typeagenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name_type` (`name_type`),
  ADD UNIQUE KEY `name_type_slug` (`name_type_slug`);

--
-- Indexes for table `event_yearagenda`
--
ALTER TABLE `event_yearagenda`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `institute_attendence`
--
ALTER TABLE `institute_attendence`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `institute_departmentadn`
--
ALTER TABLE `institute_departmentadn`
  ADD PRIMARY KEY (`id`),
  ADD KEY `institute_department_unitadn_id_351f427c_fk_institute` (`unitadn_id`);

--
-- Indexes for table `institute_institution`
--
ALTER TABLE `institute_institution`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `institute_unitadn`
--
ALTER TABLE `institute_unitadn`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reports_logo`
--
ALTER TABLE `reports_logo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reports_mensual`
--
ALTER TABLE `reports_mensual`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name_slug` (`name_slug`);

--
-- Indexes for table `reports_semestral`
--
ALTER TABLE `reports_semestral`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name_slug` (`name_slug`);

--
-- Indexes for table `reports_trimestral`
--
ALTER TABLE `reports_trimestral`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name_slug` (`name_slug`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authentication_user`
--
ALTER TABLE `authentication_user`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `authentication_user_groups`
--
ALTER TABLE `authentication_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `authentication_user_user_permissions`
--
ALTER TABLE `authentication_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `django_summernote_attachment`
--
ALTER TABLE `django_summernote_attachment`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `event_agenda`
--
ALTER TABLE `event_agenda`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `event_catagenda`
--
ALTER TABLE `event_catagenda`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `event_commentinformative`
--
ALTER TABLE `event_commentinformative`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `event_informative`
--
ALTER TABLE `event_informative`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `event_requestagenda`
--
ALTER TABLE `event_requestagenda`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `event_typeagenda`
--
ALTER TABLE `event_typeagenda`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `event_yearagenda`
--
ALTER TABLE `event_yearagenda`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `institute_attendence`
--
ALTER TABLE `institute_attendence`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `institute_departmentadn`
--
ALTER TABLE `institute_departmentadn`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `institute_institution`
--
ALTER TABLE `institute_institution`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `institute_unitadn`
--
ALTER TABLE `institute_unitadn`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reports_logo`
--
ALTER TABLE `reports_logo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `reports_mensual`
--
ALTER TABLE `reports_mensual`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reports_semestral`
--
ALTER TABLE `reports_semestral`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reports_trimestral`
--
ALTER TABLE `reports_trimestral`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authentication_user_groups`
--
ALTER TABLE `authentication_user_groups`
  ADD CONSTRAINT `authentication_user__user_id_30868577_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`),
  ADD CONSTRAINT `authentication_user_groups_group_id_6b5c44b7_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `authentication_user_user_permissions`
--
ALTER TABLE `authentication_user_user_permissions`
  ADD CONSTRAINT `authentication_user__permission_id_ea6be19a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `authentication_user__user_id_736ebf7e_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`);

--
-- Constraints for table `event_agenda`
--
ALTER TABLE `event_agenda`
  ADD CONSTRAINT `event_agenda_catagenda_id_11e15102_fk_event_catagenda_id` FOREIGN KEY (`catagenda_id`) REFERENCES `event_catagenda` (`id`),
  ADD CONSTRAINT `event_agenda_institution_id_a6ce7188_fk_institute_institution_id` FOREIGN KEY (`institution_id`) REFERENCES `institute_institution` (`id`),
  ADD CONSTRAINT `event_agenda_user_id_03c3c67b_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`);

--
-- Constraints for table `event_commentinformative`
--
ALTER TABLE `event_commentinformative`
  ADD CONSTRAINT `event_commentinforma_informative_id_116a69a0_fk_event_inf` FOREIGN KEY (`informative_id`) REFERENCES `event_informative` (`id`),
  ADD CONSTRAINT `event_commentinforma_user_id_e0c51b0e_fk_authentic` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`);

--
-- Constraints for table `event_histagenda`
--
ALTER TABLE `event_histagenda`
  ADD CONSTRAINT `event_histagenda_user_id_40e3c3f9_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`);

--
-- Constraints for table `event_informative`
--
ALTER TABLE `event_informative`
  ADD CONSTRAINT `event_informative_user_id_0bc0c75a_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`);

--
-- Constraints for table `event_requestagenda`
--
ALTER TABLE `event_requestagenda`
  ADD CONSTRAINT `event_requestagenda_catagenda_id_cd1b6485_fk_event_catagenda_id` FOREIGN KEY (`catagenda_id`) REFERENCES `event_catagenda` (`id`),
  ADD CONSTRAINT `event_requestagenda_institution_id_2f1cf5c3_fk_institute` FOREIGN KEY (`institution_id`) REFERENCES `institute_institution` (`id`),
  ADD CONSTRAINT `event_requestagenda_user_id_ef784f47_fk_authentication_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentication_user` (`id`);

--
-- Constraints for table `institute_departmentadn`
--
ALTER TABLE `institute_departmentadn`
  ADD CONSTRAINT `institute_department_unitadn_id_351f427c_fk_institute` FOREIGN KEY (`unitadn_id`) REFERENCES `institute_unitadn` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
