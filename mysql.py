'''
mysql.py
pymysql 操作数据库基本流程
'''
import pymysql

#连接数据库
db = pymysql.connect(host = 'localhost',
                    port = 3306,
                    user = 'root',
                    password='123456',
                    database = 'stu',
                    charset='utf8')

#获取游标
cur = db.cursor()

#执行语句
sql='insert into interest' \
    ' values (4,"Emma","draw","c",14800,"xxxx");'
cur.execute(sql)

#提交到数据库
db.commit()

#关闭游标
cur.close()

#关闭连接
db.close()

