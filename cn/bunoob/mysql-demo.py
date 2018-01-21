# MySQL数据库连接
import pymysql

# 打开数据库连接
db = pymysql.connect('192.168.0.111', 'root', 'root', 'wechat')

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

print("Database version: {0}".format(data))

# 关闭数据库连接
db.close()
