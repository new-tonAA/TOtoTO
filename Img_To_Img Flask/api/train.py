from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from mapper.user import User as mapperUser
import numpy as np
import os

from mapper.image import Image as mapperImage
from utils import train_utils

train_api=Blueprint('train',__name__)

@train_api.route('/get', methods=['GET'])
@jwt_required()  #必须要携带令牌才能使用，无效或者没有令牌会导致401错误
def get_image(): #获取图片，对搜图训练进行代码优化
    identity = get_jwt_identity()
    role = mapperUser.findByusername(identity).role

    if role != 1:
        return jsonify({"message":"只有管理员可以访问"}),403

    # 检查NPZ文件是否存在
    if not os.path.exists('image_features.npz'):
        # 文件不存在，只处理新图片
        print("NPZ file not found, processing new images only")
        old_paths = np.array([], dtype=object)
        old_vectors = np.array([])
        old_types = np.array([])
    else:
        old_data = np.load('image_features.npz', allow_pickle=True)
        old_paths = old_data['paths']  # 旧路径
        old_types = old_data['types']
        old_vectors = old_data['vectors']  # 旧特征向量
        old_data.close()

        indices_to_delete = []

        for index in range(len(old_paths)):
            img = mapperImage.find_imageUrlById(old_paths[index])
            if img is None:
                print(f"img {old_paths[index]} doesn't exist")
                indices_to_delete.append(index)

        # 删除数据
        old_paths = np.delete(old_paths, indices_to_delete)
        old_vectors = np.delete(old_vectors,indices_to_delete,axis=0)
        old_types = np.delete(old_types,indices_to_delete)

    all_images = mapperImage.get_image(old_paths)  # 获取除old_path以外所有图片

    images = [{
        'id':img.id,
        'url': img.image,
        'type':img.category
    } for img in all_images]  # 将图片变成字典

    new_paths = []  # 存储图像路径
    new_vectors = []# 存储图像向量
    new_types = [] #新图片类型

    for i in range(len(images)):
        vec = train_utils.extract_vector_from_url(images[i]['url'])
        if vec is not None:
            new_paths.append(images[i]['id'])
            new_vectors.append(vec)
            new_types.append(images[i]['type'])
            print(f"Processed: {images[i]['id'],images[i]['url'],images[i]['type']}")
        else:
             print(f"Failed to extract features from: {images[i]['id'],images[i]['url'],images[i]['type']}")

    if not new_paths:
        np.savez_compressed(f'image_features.npz', paths=old_paths, vectors=old_vectors, types=old_types)
        return jsonify({"error": "No valid new images processed"}),200

    new_vectors=np.array(new_vectors)

    print("OK4.0")

    paths = []  # 存储图像路径
    vectors = []# 存储图像向量
    types = [] #存储图片类型

    if len(old_paths) != 0:
        new_vectors = np.array(new_vectors)
        paths = np.concatenate((old_paths,new_paths))
        types =np.concatenate((old_types,new_types))
        #转化为numpy数组
        paths = np.array(paths, dtype=object)
        vectors = np.vstack((old_vectors, new_vectors))
        types = np.array(types, dtype=object)
    else:
        print("old_paths is nothing")
        paths = np.array(new_paths, dtype=object)
        vectors = np.vstack(new_vectors)
        types = np.array(new_types, dtype=object)

    print(paths, vectors, types)
    # 保存合并后的数据（覆盖旧文件）
    np.savez_compressed(f'image_features.npz', paths=paths, vectors=vectors, types=types)
    return jsonify({"message":"OK"}),200