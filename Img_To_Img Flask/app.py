from flask import Flask, jsonify

from api.user import user_api
from api.image import image_api
from api.train import train_api
from api.location import location_api
from api.GetCustomerLocation import location_bp # 用户获得自己的定位
from flask_migrate import Migrate as migrate
from flask_jwt_extended import JWTManager
from mapper.extensions import cache
from flask_cors import CORS
import config
from api import map_bp
from api.ShowImages import show_images_bp #图片相册
from api.review import review_api #评论
from api.chatAi import chatai_api

app=Flask(__name__)
# 允许iframe嵌入，防止浏览器阻止iframe加载，加载地图需要
@app.after_request
def allow_iframe(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'  #或者'SAMEORIGIN'
    return response
app.register_blueprint(user_api,url_prefix='/user')
app.register_blueprint(image_api,url_prefix='/image')
app.register_blueprint(train_api,url_prefix='/train')
app.register_blueprint(location_api,url_prefix='/location')

# 注册新加的定位蓝图 (location_bp) —— 前缀已经在 blueprint 里定义
app.register_blueprint(location_bp)
app.register_blueprint(map_bp)
app.register_blueprint(show_images_bp, url_prefix='/ShowImages')
app.register_blueprint(review_api,url_prefix='/review')
app.register_blueprint(chatai_api, url_prefix='/api')


#连接mysql数据库
app.config.from_object(config.MysqlConfig)
from model.models import db
db.init_app(app)
grate = migrate(app,db)


# 配置Redis
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0

# 初始化缓存
cache.init_app(app)

#token配置
app.config['JWT_SECRET_KEY'] = "default-insecure-secret" #配置密钥
app.config["JWT_HEADER_TYPE"] = "" #允许不带类型前缀
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_HEADER_NAME"] = "Authorization"  # 默认就是Authorization
jwt = JWTManager(app)  # 必须在配置后初始化

#启动跨域资源共享
CORS(app)

if __name__ == '__main__':
    app.run('127.0.0.1',8010,debug=True)
