from model.models import User as modelsUser
from model.models import db


#数据库账号信息
class User():
    def findByusername(username):
        Result = modelsUser.query.filter_by(username=username).first()
        return Result

    def findByemail(email):
        Result = modelsUser.query.filter_by(email=email).first()
        return Result

    #修改邮箱信息
    def modifyByusername(username,email):
        # 查询要更新的记录
        user = modelsUser.query.filter_by(username=username).first()
        if user is None:
            return False  # 用户不存在

        try:
            user.email=email #修改邮箱
            db.session.commit() #上交修改内容
            return True
        except Exception as e:
            db.session.rollback() #出错时回滚
            print(f"修改邮箱失败:{str(e)}")
            return False

    #注册增加账号信息
    def add_user(data):
        db.session.add(data)
        db.session.commit()
        return data.id
