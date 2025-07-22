#轮流展示图片（展示本地文件夹）
import os
from flask import Blueprint, jsonify, send_from_directory

# 定义蓝图
show_images_bp = Blueprint('ShowImages', __name__)

# 图片目录
IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'images')
# 支持的后缀
EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}

@show_images_bp.route('/list', methods=['GET'])
def list_images():
    """
    返回 images 目录下所有图片文件名（不含后缀）及原始文件名列表
    """
    files = [f for f in os.listdir(IMAGES_DIR)
             if os.path.splitext(f.lower())[1] in EXTENSIONS]
    files.sort()
    data = [
        {'name': os.path.splitext(f)[0], 'filename': f}
        for f in files
    ]
    return jsonify(data)

@show_images_bp.route('/<path:filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(IMAGES_DIR, filename)#返回图片二进制，相当于将所有图片数据给前端