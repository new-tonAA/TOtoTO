/*
 Navicat Premium Dump SQL

 Source Server         : practice
 Source Server Type    : MySQL
 Source Server Version : 80404 (8.4.4)
 Source Host           : localhost:3306
 Source Schema         : db_pic_faiss

 Target Server Type    : MySQL
 Target Server Version : 80404 (8.4.4)
 File Encoding         : 65001

 Date: 23/06/2025 19:40:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for image
-- ----------------------------
DROP TABLE IF EXISTS `image`;
CREATE TABLE `image`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `image_name` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '图片名',
  `image` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '图片',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `category` int NULL DEFAULT NULL COMMENT '图片类型',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `image`(`image` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 128 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of image
-- ----------------------------
INSERT INTO `image` VALUES (1, NULL, 'https://github.com/foxfur-ry/Images/blob/main/battlecats/20250522201904368.jpg?raw=true', '2025-05-22 12:23:05', '2025-05-22 12:23:05', 0);
INSERT INTO `image` VALUES (2, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201857292.jpg', '2025-05-22 12:23:39', '2025-05-22 12:23:39', 0);
INSERT INTO `image` VALUES (3, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201846189.jpg', '2025-05-22 12:24:05', '2025-05-22 12:24:05', 0);
INSERT INTO `image` VALUES (4, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201846188.jpg', '2025-05-22 12:25:26', '2025-05-22 12:25:26', 0);
INSERT INTO `image` VALUES (5, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201846187.jpg', '2025-05-22 12:25:51', '2025-05-22 12:25:51', 0);
INSERT INTO `image` VALUES (6, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201846186.jpg', '2025-05-22 12:26:17', '2025-05-22 12:26:17', 0);
INSERT INTO `image` VALUES (8, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201814966.jpg', '2025-05-22 12:30:52', '2025-05-22 12:30:52', 0);
INSERT INTO `image` VALUES (9, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201810939.jpg', '2025-05-22 12:32:03', '2025-05-22 12:32:03', 0);
INSERT INTO `image` VALUES (10, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201805776.jpg', '2025-05-22 12:33:21', '2025-05-22 12:33:21', 0);
INSERT INTO `image` VALUES (11, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201801309.jpg', '2025-05-22 12:33:55', '2025-05-22 12:33:55', 0);
INSERT INTO `image` VALUES (12, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201756828.jpg', '2025-05-22 12:34:26', '2025-05-22 12:34:26', 0);
INSERT INTO `image` VALUES (13, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201751871.jpg', '2025-05-22 12:34:51', '2025-05-22 12:34:51', 0);
INSERT INTO `image` VALUES (14, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201746720.jpg', '2025-05-22 12:35:23', '2025-05-22 12:35:23', 0);
INSERT INTO `image` VALUES (15, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201742447.jpg', '2025-05-22 12:36:17', '2025-05-22 12:36:17', 0);
INSERT INTO `image` VALUES (16, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201737693.jpg', '2025-05-22 12:36:46', '2025-05-22 12:36:46', 0);
INSERT INTO `image` VALUES (17, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201732480.jpg', '2025-05-22 12:37:09', '2025-05-22 12:37:09', 0);
INSERT INTO `image` VALUES (18, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201727530.jpg', '2025-05-22 12:38:01', '2025-05-22 12:38:01', 0);
INSERT INTO `image` VALUES (19, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201722613.jpg', '2025-05-22 12:38:33', '2025-05-22 12:38:33', 0);
INSERT INTO `image` VALUES (20, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201717996.jpg', '2025-05-22 12:39:06', '2025-05-22 12:39:06', 0);
INSERT INTO `image` VALUES (21, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201711424.jpg', '2025-05-22 12:39:35', '2025-05-22 12:39:35', 0);
INSERT INTO `image` VALUES (22, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201706343.jpg', '2025-05-22 12:40:24', '2025-05-22 12:40:24', 0);
INSERT INTO `image` VALUES (23, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201701890.jpg', '2025-05-22 12:40:56', '2025-05-22 12:40:56', 0);
INSERT INTO `image` VALUES (24, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201656424.jpg', '2025-05-22 12:41:33', '2025-05-22 12:41:33', 0);
INSERT INTO `image` VALUES (25, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201651777.jpg', '2025-05-22 12:42:05', '2025-05-22 12:42:05', 0);
INSERT INTO `image` VALUES (26, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201632527.jpg', '2025-05-22 12:42:46', '2025-05-22 12:42:46', 0);
INSERT INTO `image` VALUES (27, NULL, 'https://github.com/foxfur-ry/Images/blob/main/battlecats/20250522201625422.jpg?raw=true', '2025-05-22 12:43:22', '2025-05-22 12:43:22', 0);
INSERT INTO `image` VALUES (28, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250522201602831.jpg', '2025-05-22 12:43:52', '2025-05-22 12:43:52', 0);
INSERT INTO `image` VALUES (29, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250523121259049.jpg', '2025-05-23 04:13:58', '2025-05-23 04:13:58', 0);
INSERT INTO `image` VALUES (30, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/image/20250522142219526.jpg', '2025-05-24 09:44:37', '2025-05-24 09:44:37', 0);
INSERT INTO `image` VALUES (31, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250527114754.jpg', '2025-05-27 03:47:58', '2025-05-27 03:47:58', 0);
INSERT INTO `image` VALUES (32, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250527115555.jpg', '2025-05-27 03:55:58', '2025-05-27 03:55:58', 0);
INSERT INTO `image` VALUES (33, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/battlecats/20250527115834.jpg', '2025-05-27 03:58:38', '2025-05-27 03:58:38', 0);
INSERT INTO `image` VALUES (40, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607141951.jpg', '2025-06-07 06:19:57', '2025-06-07 06:19:57', 1);
INSERT INTO `image` VALUES (41, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607142141.jpg', '2025-06-07 06:21:46', '2025-06-07 06:21:46', 1);
INSERT INTO `image` VALUES (42, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607142344.jpg', '2025-06-07 06:23:51', '2025-06-07 06:23:51', 1);
INSERT INTO `image` VALUES (43, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607142410.jpg', '2025-06-07 06:24:16', '2025-06-07 06:24:16', 1);
INSERT INTO `image` VALUES (44, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607142448.jpg', '2025-06-07 06:24:52', '2025-06-07 06:24:52', 1);
INSERT INTO `image` VALUES (45, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607144635.jpg', '2025-06-07 06:46:42', '2025-06-07 06:46:42', 1);
INSERT INTO `image` VALUES (46, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150127.jpg', '2025-06-07 07:01:31', '2025-06-07 07:01:31', 2);
INSERT INTO `image` VALUES (47, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150144.jpg', '2025-06-07 07:01:48', '2025-06-07 07:01:48', 2);
INSERT INTO `image` VALUES (48, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150157.jpg', '2025-06-07 07:02:02', '2025-06-07 07:02:02', 2);
INSERT INTO `image` VALUES (49, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150215.jpg', '2025-06-07 07:02:20', '2025-06-07 07:02:20', 2);
INSERT INTO `image` VALUES (50, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150232.jpg', '2025-06-07 07:02:35', '2025-06-07 07:02:35', 2);
INSERT INTO `image` VALUES (51, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150245.jpg', '2025-06-07 07:02:49', '2025-06-07 07:02:49', 2);
INSERT INTO `image` VALUES (52, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150300.jpg', '2025-06-07 07:03:04', '2025-06-07 07:03:04', 2);
INSERT INTO `image` VALUES (53, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150324.jpg', '2025-06-07 07:03:30', '2025-06-07 07:03:30', 2);
INSERT INTO `image` VALUES (54, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607150341.jpg', '2025-06-07 07:03:45', '2025-06-07 07:03:45', 2);
INSERT INTO `image` VALUES (55, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607161505.jpg', '2025-06-07 08:15:08', '2025-06-07 08:15:08', 1);
INSERT INTO `image` VALUES (56, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607161523.jpg', '2025-06-07 08:15:29', '2025-06-07 08:15:29', 1);
INSERT INTO `image` VALUES (57, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607161541.jpg', '2025-06-07 08:15:44', '2025-06-07 08:15:44', 1);
INSERT INTO `image` VALUES (58, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607161559.jpg', '2025-06-07 08:16:02', '2025-06-07 08:16:02', 1);
INSERT INTO `image` VALUES (59, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607161620.jpg', '2025-06-07 08:16:24', '2025-06-07 08:16:24', 1);
INSERT INTO `image` VALUES (60, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607161638.jpg', '2025-06-07 08:16:41', '2025-06-07 08:16:41', 1);
INSERT INTO `image` VALUES (61, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607161658.jpg', '2025-06-07 08:17:01', '2025-06-07 08:17:01', 1);
INSERT INTO `image` VALUES (62, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162139.jpg', '2025-06-07 08:21:43', '2025-06-07 08:21:43', 3);
INSERT INTO `image` VALUES (63, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162153.jpg', '2025-06-07 08:21:56', '2025-06-07 08:21:56', 3);
INSERT INTO `image` VALUES (64, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162206.jpg', '2025-06-07 08:22:10', '2025-06-07 08:22:10', 3);
INSERT INTO `image` VALUES (65, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162220.jpg', '2025-06-07 08:22:23', '2025-06-07 08:22:23', 3);
INSERT INTO `image` VALUES (66, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162235.jpg', '2025-06-07 08:22:39', '2025-06-07 08:22:39', 3);
INSERT INTO `image` VALUES (67, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162249.jpg', '2025-06-07 08:22:52', '2025-06-07 08:22:52', 3);
INSERT INTO `image` VALUES (68, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162302.jpg', '2025-06-07 08:23:05', '2025-06-07 08:23:05', 3);
INSERT INTO `image` VALUES (69, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162315.jpg', '2025-06-07 08:23:19', '2025-06-07 08:23:19', 3);
INSERT INTO `image` VALUES (70, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162333.jpg', '2025-06-07 08:23:36', '2025-06-07 08:23:36', 3);
INSERT INTO `image` VALUES (71, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162351.jpg', '2025-06-07 08:23:56', '2025-06-07 08:23:56', 3);
INSERT INTO `image` VALUES (72, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162410.jpg', '2025-06-07 08:24:13', '2025-06-07 08:24:13', 3);
INSERT INTO `image` VALUES (73, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162427.jpg', '2025-06-07 08:24:32', '2025-06-07 08:24:32', 3);
INSERT INTO `image` VALUES (74, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162445.jpg', '2025-06-07 08:24:49', '2025-06-07 08:24:49', 3);
INSERT INTO `image` VALUES (75, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162503.jpg', '2025-06-07 08:25:07', '2025-06-07 08:25:07', 3);
INSERT INTO `image` VALUES (76, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162531.jpg', '2025-06-07 08:25:35', '2025-06-07 08:25:35', 3);
INSERT INTO `image` VALUES (77, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162548.jpg', '2025-06-07 08:25:51', '2025-06-07 08:25:51', 3);
INSERT INTO `image` VALUES (78, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162604.jpg', '2025-06-07 08:26:08', '2025-06-07 08:26:08', 3);
INSERT INTO `image` VALUES (79, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162623.jpg', '2025-06-07 08:26:26', '2025-06-07 08:26:26', 3);
INSERT INTO `image` VALUES (80, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162642.jpg', '2025-06-07 08:26:46', '2025-06-07 08:26:46', 3);
INSERT INTO `image` VALUES (81, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162658.jpg', '2025-06-07 08:27:01', '2025-06-07 08:27:01', 3);
INSERT INTO `image` VALUES (82, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607162712.jpg', '2025-06-07 08:27:16', '2025-06-07 08:27:16', 3);
INSERT INTO `image` VALUES (83, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607164806.jpg', '2025-06-07 08:48:12', '2025-06-07 08:48:12', 4);
INSERT INTO `image` VALUES (84, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607164822.jpg', '2025-06-07 08:48:27', '2025-06-07 08:48:27', 4);
INSERT INTO `image` VALUES (85, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607164836.jpg', '2025-06-07 08:48:39', '2025-06-07 08:48:39', 4);
INSERT INTO `image` VALUES (86, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607164850.jpg', '2025-06-07 08:48:53', '2025-06-07 08:48:53', 4);
INSERT INTO `image` VALUES (87, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607164910.jpg', '2025-06-07 08:49:13', '2025-06-07 08:49:13', 4);
INSERT INTO `image` VALUES (88, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607164923.jpg', '2025-06-07 08:49:27', '2025-06-07 08:49:27', 4);
INSERT INTO `image` VALUES (89, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191326.jpg', '2025-06-07 11:13:29', '2025-06-07 11:13:29', 5);
INSERT INTO `image` VALUES (90, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191341.jpg', '2025-06-07 11:13:44', '2025-06-07 11:13:44', 5);
INSERT INTO `image` VALUES (91, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191353.jpg', '2025-06-07 11:13:57', '2025-06-07 11:13:57', 5);
INSERT INTO `image` VALUES (92, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191405.jpg', '2025-06-07 11:14:09', '2025-06-07 11:14:09', 5);
INSERT INTO `image` VALUES (93, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191427.jpg', '2025-06-07 11:14:30', '2025-06-07 11:14:30', 5);
INSERT INTO `image` VALUES (94, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191439.jpg', '2025-06-07 11:14:43', '2025-06-07 11:14:43', 5);
INSERT INTO `image` VALUES (95, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191458.jpg', '2025-06-07 11:15:01', '2025-06-07 11:15:01', 6);
INSERT INTO `image` VALUES (96, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191510.jpg', '2025-06-07 11:15:14', '2025-06-07 11:15:14', 6);
INSERT INTO `image` VALUES (97, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191526.jpg', '2025-06-07 11:15:30', '2025-06-07 11:15:30', 6);
INSERT INTO `image` VALUES (98, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191541.jpg', '2025-06-07 11:15:44', '2025-06-07 11:15:44', 6);
INSERT INTO `image` VALUES (99, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191557.jpg', '2025-06-07 11:16:01', '2025-06-07 11:16:01', 6);
INSERT INTO `image` VALUES (100, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191611.jpg', '2025-06-07 11:16:14', '2025-06-07 11:16:14', 6);
INSERT INTO `image` VALUES (101, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191629.jpg', '2025-06-07 11:16:32', '2025-06-07 11:16:32', 6);
INSERT INTO `image` VALUES (102, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191646.jpg', '2025-06-07 11:16:50', '2025-06-07 11:16:50', 6);
INSERT INTO `image` VALUES (103, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191713.jpg', '2025-06-07 11:17:16', '2025-06-07 11:17:16', 7);
INSERT INTO `image` VALUES (104, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191731.jpg', '2025-06-07 11:17:34', '2025-06-07 11:17:34', 7);
INSERT INTO `image` VALUES (105, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191747.jpg', '2025-06-07 11:17:50', '2025-06-07 11:17:50', 7);
INSERT INTO `image` VALUES (106, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607191804.jpg', '2025-06-07 11:18:08', '2025-06-07 11:18:08', 7);
INSERT INTO `image` VALUES (107, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192048.jpg', '2025-06-07 11:20:51', '2025-06-07 11:20:51', 7);
INSERT INTO `image` VALUES (108, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192119.jpg', '2025-06-07 11:21:23', '2025-06-07 11:21:23', 7);
INSERT INTO `image` VALUES (109, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192139.jpg', '2025-06-07 11:21:42', '2025-06-07 11:21:42', 7);
INSERT INTO `image` VALUES (110, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192155.jpg', '2025-06-07 11:21:58', '2025-06-07 11:21:58', 7);
INSERT INTO `image` VALUES (111, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192211.jpg', '2025-06-07 11:22:14', '2025-06-07 11:22:14', 7);
INSERT INTO `image` VALUES (112, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192227.jpg', '2025-06-07 11:22:30', '2025-06-07 11:22:30', 7);
INSERT INTO `image` VALUES (113, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192245.jpg', '2025-06-07 11:22:47', '2025-06-07 11:22:47', 7);
INSERT INTO `image` VALUES (114, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192309.jpg', '2025-06-07 11:23:12', '2025-06-07 11:23:12', 7);
INSERT INTO `image` VALUES (115, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192325.jpg', '2025-06-07 11:23:28', '2025-06-07 11:23:28', 7);
INSERT INTO `image` VALUES (116, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192344.jpg', '2025-06-07 11:23:47', '2025-06-07 11:23:47', 8);
INSERT INTO `image` VALUES (117, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192358.jpg', '2025-06-07 11:24:02', '2025-06-07 11:24:02', 8);
INSERT INTO `image` VALUES (118, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192422.jpg', '2025-06-07 11:24:25', '2025-06-07 11:24:25', 8);
INSERT INTO `image` VALUES (119, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192454.jpg', '2025-06-07 11:24:58', '2025-06-07 11:24:58', 8);
INSERT INTO `image` VALUES (120, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192509.jpg', '2025-06-07 11:25:13', '2025-06-07 11:25:13', 8);
INSERT INTO `image` VALUES (121, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192529.jpg', '2025-06-07 11:25:33', '2025-06-07 11:25:33', 8);
INSERT INTO `image` VALUES (122, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192545.jpg', '2025-06-07 11:25:48', '2025-06-07 11:25:48', 8);
INSERT INTO `image` VALUES (123, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192719.jpg', '2025-06-07 11:27:23', '2025-06-07 11:27:23', 9);
INSERT INTO `image` VALUES (124, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192740.jpg', '2025-06-07 11:27:44', '2025-06-07 11:27:44', 9);
INSERT INTO `image` VALUES (125, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192754.jpg', '2025-06-07 11:27:57', '2025-06-07 11:27:57', 9);
INSERT INTO `image` VALUES (126, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192807.jpg', '2025-06-07 11:28:10', '2025-06-07 11:28:10', 9);
INSERT INTO `image` VALUES (127, NULL, 'https://raw.githubusercontent.com/foxfur-ry/Images/refs/heads/main/Img_To_Img/20250607192830.jpg', '2025-06-07 11:28:34', '2025-06-07 11:28:34', 9);

SET FOREIGN_KEY_CHECKS = 1;
