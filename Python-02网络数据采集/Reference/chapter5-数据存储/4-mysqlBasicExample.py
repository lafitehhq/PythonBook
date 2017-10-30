# 使用pymysql链接数据库并执行禅熏操作
# http://www.jb51.net/article/104820.htm

import pymysql

"""
connect方法常用参数:
    host: 数据库主机名.默认是用本地主机
    user: 数据库登陆名.默认是当前用户
    passwd: 数据库登陆的秘密.默认为空
    db: 要使用的数据库名.没有默认值
    port: MySQL服务使用的TCP端口.默认是3306
    charset: 数据库编码
"""

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='Vanke', charset='utf8')
cur = conn.cursor()
cur.execute("USE vanke")

cur.execute("SELECT * FROM organization")

# 获取所有记录
organization = cur.fetchall()
print(type(organization))
for org in organization:
    print(org)


cur.close()
conn.close()