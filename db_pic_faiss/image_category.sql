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

 Date: 23/06/2025 19:41:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for image_category
-- ----------------------------
DROP TABLE IF EXISTS `image_category`;
CREATE TABLE `image_category`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `create_user` int NOT NULL COMMENT '创建者',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `name` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '图片类型名',
  `longitude` varchar(16) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '经度',
  `latitude` varchar(16) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '纬度',
  `address` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '地址',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE,
  INDEX `create_user`(`create_user` ASC) USING BTREE,
  CONSTRAINT `image_category_ibfk_1` FOREIGN KEY (`create_user`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of image_category
-- ----------------------------
INSERT INTO `image_category` VALUES (1, 4, '2025-06-09 06:31:54', '2025-06-09 06:31:54', '华南理工大学大学城校区教学区河流', '113.4011', '23.051', '华南理工大学(大学城校区), 382, 大学城外环东路, 小谷围街道, 番禺区, 广州市, 广东省, 510006, 中国');
INSERT INTO `image_category` VALUES (2, 4, '2025-06-09 06:43:43', '2025-06-09 06:43:43', '华南理工大学大学城校区第二饭堂', '113.398', '23.0545', 'T11第二饭堂, 大学城中环东路, 广州大学城, 小谷围街道, 番禺区, 广州市, 广东省, 511400, 中国');
INSERT INTO `image_category` VALUES (3, 4, '2025-06-09 06:49:06', '2025-06-09 06:49:06', '华南理工大学大学城校区麦当劳', '113.397', '23.05379', '华南理工大学(大学城校区), 382, 大学城外环东路, 广州大学城, 小谷围街道, 番禺区, 广州市, 广东省, 510006, 中国');
INSERT INTO `image_category` VALUES (4, 4, '2025-06-09 06:50:48', '2025-06-09 06:50:48', '华南理工大学大学城校区第三饭堂', '113.39760', '23.05037', '华南理工大学(大学城校区), 382, 大学城外环东路, 广州大学城, 小谷围街道, 番禺区, 广州市, 广东省, 510006, 中国');
INSERT INTO `image_category` VALUES (5, 4, '2025-06-09 06:52:21', '2025-06-09 06:52:21', '华南理工大学大学城校区教学区篮球场', '113.398333', '23.049167', '华南理工大学(大学城校区), 382, 大学城外环东路, 广州大学城, 小谷围街道, 番禺区, 广州市, 广东省, 510006, 中国');
INSERT INTO `image_category` VALUES (6, 4, '2025-06-09 07:07:24', '2025-06-09 07:07:24', '华南理工大学大学城校区教学区田径场', '113.398611', '23.048611', '大学城华工南路, 广州大学城, 小谷围街道, 番禺区, 广州市, 广东省, 511400, 中国');
INSERT INTO `image_category` VALUES (7, 4, '2025-06-09 07:07:57', '2025-06-09 07:07:57', '华南理工大学大学城校区图书馆', '113.400000', '23.048889', '华南理工大学(大学城校区), 382, 大学城外环东路, 小谷围街道, 番禺区, 广州市, 广东省, 510006, 中国');
INSERT INTO `image_category` VALUES (8, 4, '2025-06-09 07:08:35', '2025-06-09 07:08:35', '华南理工大学大学城校区第一饭堂', '113.397222', '23.051000', 'T8第一饭堂, 大学城中环东路, 广州大学城, 小谷围街道, 番禺区, 广州市, 广东省, 511400, 中国');
INSERT INTO `image_category` VALUES (9, 4, '2025-06-09 07:10:10', '2025-06-09 07:10:10', '华南理工大学大学城校区音乐厅', '113.399167', '23.048611', '华南理工大学(大学城校区), 382, 大学城外环东路, 小谷围街道, 番禺区, 广州市, 广东省, 510006, 中国');

SET FOREIGN_KEY_CHECKS = 1;
