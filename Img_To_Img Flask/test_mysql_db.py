import pymysql

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='NewtonAA47',
        database='db_pic_faiss'
    )
    print("数据库连接成功！")
except Exception as e:
    print("数据库连接失败：", e)
