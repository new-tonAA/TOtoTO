from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()
# Models
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False, comment="用户名")
    password = db.Column(db.String(128), nullable=False,comment="密码")
    nickname = db.Column(db.String(10), nullable=True, comment="昵称")
    email = db.Column(db.String(128), unique=True,nullable=True,comment="邮箱")
    phone = db.Column(db.String(11), unique=True, comment="电话")
    role=db.Column(db.Integer, default=0,nullable=False,comment="身份")  #0表示使用用户，1表示管理员
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow,comment="更新时间")

    records=db.relationship('Record',backref='record_creator',lazy=True)
    categories = db.relationship('ImageCategory',backref='category_creator',lazy=True)

class Record(db.Model):
    __tablename__='record'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment="创建者")  #这个记录是由id为user.id的用户产生的
    user_image= db.Column(db.String(256), nullable=False, comment="用户发出的图片") #用户发出的图片
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow,comment="修改时间")

    images = db.relationship("Image", secondary="record_to_image", backref="records")


#中间表格
class RecordToImage(db.Model):
    __tablename__ = "record_to_image"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    record_id=db.Column(db.Integer,db.ForeignKey('record.id')) #记录
    image_id = db.Column(db.Integer, db.ForeignKey('image.id')) #图片
    distance = db.Column(db.Float(precision=3), default=-1, comment="相似度(距离)")

class ImageCategory(db.Model):
    __tablename__ = "image_category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_user=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment="创建者")
    name=db.Column(db.String(32),unique=True,comment="图片类型名")
    address=db.Column(db.String(128),comment="地址")
    longitude=db.Column(db.String(16),default=-1,comment="经度")
    latitude=db.Column(db.String(16),default=-1,comment="纬度")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")

class Image(db.Model):
    __tablename__='image'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_name=db.Column(db.String(32), nullable=True, comment="图片名")
    image = db.Column(db.String(256), nullable=False, unique=True, comment="图片")  #图片的URL长度不能超过256
    category = db.Column(db.Integer, default=0,nullable=True, comment="图片类型")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, comment="创建时间")
    update_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")

class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(45),nullable=False, comment="评论内容")
    create_time = db.Column(db.DateTime, default=datetime.utcnow,
                            nullable=False, comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.utcnow,
                            onupdate=datetime.utcnow, nullable=False,comment="更新时间")
