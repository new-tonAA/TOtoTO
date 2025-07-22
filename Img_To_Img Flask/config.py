class MysqlConfig(object):
    #sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = # connect to your own database
    #设置每次请求结束后会自动提交数据库的改动，一般设置手动保存
    SQLALCHEMY_COMMIT_ON_TEARDOWN=False
    #设置sqlachemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS=True
