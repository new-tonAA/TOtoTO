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

 Date: 08/06/2025 13:43:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for record_to_image
-- ----------------------------
DROP TABLE IF EXISTS `record_to_image`;
CREATE TABLE `record_to_image`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `record_id` int NULL DEFAULT NULL,
  `image_id` int NULL DEFAULT NULL,
  `distance` float NULL DEFAULT NULL COMMENT '相似度(距离)',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `image_id`(`image_id` ASC) USING BTREE,
  INDEX `record_id`(`record_id` ASC) USING BTREE,
  CONSTRAINT `record_to_image_ibfk_1` FOREIGN KEY (`image_id`) REFERENCES `image` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `record_to_image_ibfk_2` FOREIGN KEY (`record_id`) REFERENCES `record` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 112 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
