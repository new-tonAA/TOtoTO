from flask import Blueprint, jsonify, request
from model.models import User as modelsUser
from mapper.user import User as mapperUser
from utils.User.SendEmail_utils import SendEmail
from mapper.extensions import cache
from flask_jwt_extended import jwt_required, get_jwt_identity
import utils.User.security as security

user_api = Blueprint('user_api', __name__)

@user_api.route('/userInfo',methods=['GET'])
@jwt_required(optional=True)
def get_user_info():
    identity = get_jwt_identity()
    
    print(identity)
    if not identity:
        return jsonify({"message":"未登录"}),200
    user = mapperUser.findByusername(identity)
    if not user:
        return jsonify({"message":"用户信息不存在"}),400
    else:
        return jsonify({"message":"获取用户数据信息",
                        "username":user.username,
                        "email":user.email,
                        "phone":user.phone,
                        "role":user.role,}),200



@user_api.route('/register',methods=['POST'])
def register():   #注册
    data=request.form.to_dict() #获取数据库前端

    if not data:
        return jsonify({'error':'没有输入账号和密码'}),401
    if not data.get('username') or not data.get('password') or not data.get('repassword'):
        return jsonify({'error':'填入的数据不完整'}),401
    if data.get('password') != data.get('repassword'):
        return jsonify({'error':'前后密码输入不一致'}),401
    if len(data.get('password')) < 5 and len(data.get('password')) > 16:
        return jsonify({'error': '密码要求在5到16个字符之间'}), 401
    if mapperUser.findByusername(data['username']):
        return jsonify({'error':'用户名已存在'}),401

    pd = security.get_password_hash(data.get('password'))

    user= modelsUser(
        username=data.get('username'),
        nickname=data.get('nickname',''),
        password=pd,
        role=data.get('role',0)
    )

    try:
        mapperUser.add_user(user)  #数据库操作
        return jsonify({'message':'User registered successfully'}),200
    except InterruptedError as e:
        return jsonify({'error': e}),401

@user_api.route('/login',methods=['GET'])
def login():  #登录
    data=request.args.to_dict()
    if not data:
        return jsonify({'error':'没有输入账号和密码'}),401
    if not data.get('username') or not data.get('password'):
        return jsonify({'error':'填入的数据不完整'}),401

    user=mapperUser.findByusername(data.get('username'))
    if not user:
        return jsonify({'error':'用户名不存在'}),401
    elif not security.verify_password(data.get('password'),user.password):
        return jsonify({'error':'密码不正确'}),401
    else:
        token = security.create_token(user.username)

    return jsonify({'message':'登录成功','token':token}),200

@user_api.route('/login/email',methods=['GET'])
def email(): #忘记密码或者用户名时进行邮箱验证，获取email
    data=request.args.to_dict()  #request.form只接收POST/PUT/PATCH请求，args获取GET参数
    if not request.args.get('email'):
        return jsonify({"error":"未填写邮箱"}),401

    user=mapperUser.findByemail(data.get('email'))
    if not user:
        return jsonify({"error":"用户不存在"}),401

    verification_code = SendEmail(data.get('email'))

    if verification_code == None:
        return jsonify({"error":"邮箱发送失败"}),401

    data = {
        'verification': verification_code,
        'email':user.email,
        'username': user.username
    }
    cache.set('user_data', data, timeout=120)
    return jsonify({"message":"验证码已经发送"}),200

@user_api.route('/register/email',methods=['GET'])  #注册时可以绑定邮箱
def register_email():
    data=request.args.to_dict()
    if not data.get('email'):
        return jsonify({"error": "未填写邮箱"}), 401

    user=mapperUser.findByemail(data.get('email'))
    if user:
        return jsonify({"error":"邮箱已经绑定"}),401

    verification_code = SendEmail(data.get('email'))

    if verification_code == None:
        return jsonify({"error": "邮箱发送失败"}), 401

    data = {
        'verification': verification_code,
        'email': data.get('email'),
        'username':data.get('username')
    }
    cache.set('user_data', data, timeout=120)
    return jsonify({"message": "验证码已经发送"}), 200

@user_api.route('/register/verify',methods=['PATCH'])
def register_verify():
    data = request.form.to_dict()
    verify = data.get('verify')
    email = data.get('email')

    if cache.has('user_data'):
        cache_data = cache.get('user_data')
    else:
        return jsonify({"error":"验证码已过期"}),401

    verification = cache_data.get('verification')
    cache_email = cache_data.get('email')
    username = cache_data.get('username')

    if verify != verification:
        return jsonify({"error": "验证码不通过"}), 401

    if email != cache_email:
        return jsonify({"error": "邮箱不要更改"}), 401

    if mapperUser.modifyByusername(username,email):
        return jsonify({"message":"邮箱绑定成功"}),200
    else:
        return jsonify({"message": "邮箱绑定失败"}),401


@user_api.route('/verify',methods=['GET'])
def verify():  #verify验证码 email+verify
    data=request.args.to_dict()
    verify=data.get('verify')
    email=data.get('email')

    if cache.has('user_data'):
        cache_data = cache.get('user_data')
    else:
        return jsonify({"error":"验证码已过期"}),401

    verification = cache_data.get('verification')
    cache_email=cache_data.get('email')
    username=cache_data.get('username')

    if verify != verification:
        return jsonify({"error":"验证码不通过"}),401

    if email != cache_email:
        return jsonify({"error":"邮箱不要更改"}),401

    token =security.create_token(username)
    return jsonify({'message': '登录成功', 'token': token}),200