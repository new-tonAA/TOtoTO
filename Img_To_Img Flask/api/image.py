from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from mapper.location import Location
from model.models import Image as modelsImage, Record as modelsRecord, RecordToImage as modelsRecordToImage
from mapper.image import Image as mapperImage
from mapper.record import Record as mapperRecord
from mapper.user import User as mapperUser
from mapper.record_to_image import RecordToImage as mapperRecordToImage
from werkzeug.utils import secure_filename
from utils import add_image as add
import utils.faiss_utils as search
import os.path
import numpy as np
import faiss
from server.chatAi import ChatAI


# 初始化 ChatAI 实例（Moonshot）
chat_ai = ChatAI(api_key="sk-75pLv0r1m0IScRESVhCzA9Lh1K65Io3KvVBxkC8o5FVpVRkI")

image_api=Blueprint('image',__name__)

@image_api.route('/add',methods=['POST'])
@jwt_required()
def add_image(): #管理员增加图片到数据库中
    identity = get_jwt_identity()
    role = mapperUser.findByusername(identity).role

    # 获取图片类型
    category = request.form.to_dict().get('category')
    if role != 1:
        return jsonify({"message": "只有管理员可以访问"}), 403
    if 'image' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    img=add.get_url(image,"Test")

    if not img:
        return jsonify({'message': '图片为空'}), 400
    if len(img)>256:
        return jsonify({'message':'图片URL过长'}),400

    image=modelsImage(
        image=img,
        category=category
    )

    mapperImage.add_image(image)
    return jsonify({'message':'Image adds successfully'}),200


@image_api.route('/search', methods=['GET','POST']) # API接口：提交查询，终端使用的是POST方法
@jwt_required(optional=True)
def search_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 加载预计算的特征
    data = np.load(f'image_features.npz', allow_pickle=True)  # 加载训练结果.npz文件
    paths = data['paths']  # 从文件中得出图片路径
    vectors = data['vectors']  # 从文件中得出图片向量
    types = data['types'] # 图片类型

    # 3.构建Faiss索引
    d = 2048  # 特征向量的维度（ResNet-50提取的特征向量维度为 2048）
    index = faiss.IndexFlatL2(d)  # 创造一个索引对象进行相似性搜索
    index.add(vectors)

    # 获取安全的文件名并提取扩展名
    original_filename = secure_filename(image.filename)
    _, ext = os.path.splitext(original_filename)
    # 生成动态文件名（保留原扩展名）
    query_filename = f"query{ext}"
    query_path = os.path.join('.', query_filename)
    image.save(query_path)

    # 执行搜索
    try:
        results = search.search_topk(query_path, index, paths, types, k=3)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    # 构建响应
    # 将p的值(原本是id),通过数据库查询找到相应的URL
    response = [{'category': int(t), 'image': mapperImage.find_imageUrlById(p), 'distance': d} for t, p, d in results]

    identity = get_jwt_identity()
    if not identity:
        print("未登录，没有访问记录")
        return jsonify({'message': '搜索成功',
                        'responses': response}), 200
    else:
        image.seek(0)  # 重置指针，以便后续操作能重新读取

        img = add.get_url(image, "Test")

        if not img:
            return jsonify({'message': '图片为空'}), 400

        if len(img) > 256:
            return jsonify({'message': '图片URL过长','results': response}), 200


        userId=mapperUser.findByusername(identity).id
        record= modelsRecord (
            create_user = userId,
            user_image = img,
        )
        recordId = mapperRecord.add_record(record).id

        for t, p, d in results:
            connection = modelsRecordToImage(
                record_id=recordId,
                image_id=p,
                distance=d
            )
            mapperRecordToImage.add_connection(connection)

        createTime=mapperRecord.findByRecordId(recordId).create_time #返回创建时间
        #return jsonify({'message': '搜索成功', 'recordId': recordId, 'create_time': createTime.isoformat(),
         #               'responses': response}), 200
        # 用后端纯调用接口获取文本描述
        place_name = ''
        if results:
            first_category_id = results[0][0]
            place_name = Location.findTypeNameByType(first_category_id) or ''

        place_description = ''
        if place_name:
            place_description = chat_ai.get_description(place_name)

        return jsonify({
            'message': '搜索成功',
            'recordId': recordId,
            'create_time': createTime.isoformat(),
            'responses': response,
            'map_url': f'/map/record/{recordId}',  # 提供给前端地图使用
            'place_description': place_description  # 把AI生成的描述返回前端
        }), 200


@image_api.route('/record', methods=['GET'])
@jwt_required(optional=True)
def show_record(): #获取图片
    identity = get_jwt_identity()
    if not identity:
        print("未登录，没有访问记录")
        return jsonify({"message":None}),401

    userId = mapperUser.findByusername(identity).id

    all_records=mapperRecord.findByUserId(userId); #获取所有图片

    all_createtime=[]

    for i in range(len(all_records)):
        order = i + 1
        createtime={
            'order':order,
            'id': all_records[i].id,
            'createtime': all_records[i].create_time.isoformat()
        }
        all_createtime.append(createtime)

    return jsonify({'message':'获取记录成功', "all_createtime":all_createtime}),200

@image_api.route('/record/<int:hid>',methods=['GET']) #定义动态路由/history/<hid>,其中<int:hid>表示接受整数类型的参数hid（历史记录 ID）
@jwt_required()
def view_record(hid):  #hid表示记录的id
    #获取记录
    connections = mapperRecordToImage.findByrecordId(hid)
    record = mapperRecord.findByRecordId(hid)

    response = [{'image':mapperImage.find_imageUrlById(con.image_id),'distance':con.distance} for con in connections]
    #return jsonify({"message":'获取记录信息成功', "record":record.user_image,"responses":response}),200
    return jsonify({
        "message": '获取记录信息成功',
        "record": record.user_image,
        "responses": response,
        "map_url": f'/map/record/{hid}'  # 新增这个字段
    }), 200

