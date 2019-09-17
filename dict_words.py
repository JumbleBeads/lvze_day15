'''
host ：主机地址,本地 localhost
port ：端口号,默认3306
user ：用户名
password ：密码
database ：库
charset ：编码方式,推荐使用 utf8
'''
import pymysql

f = open('dict.txt')

#连接数据库
db = pymysql.connect(user = 'root',passwd = '123456',database = 'stu',charset = 'utf8')

#获取游标
cur = db.cursor()

sql = "insert into words (word,mean) values(%s,%s);"

for line in f:
    tmp = line.split(' ',1)
    word = tmp[0]
    mean = tmp[1].strip()
    cur.execute(sql,[word,mean])


try:
    db.commit()#同步数据
except:
    db.rollback()




cur.close()
db.close()