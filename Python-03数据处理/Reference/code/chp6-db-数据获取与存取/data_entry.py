#-*-coding:utf-8_-*-

"""
Description：
利用dataset模块将sqlite数据存储到指定路径

拓展：
①：dataset模块对数据库连接：http://dataset.readthedocs.io/en/latest/
②：sqlite3模块对数据库连接：http://www.runoob.com/sqlite/sqlite-python.html
③：sqlalchemy模块对数据库连接：http://www.itkeyword.com/doc/8449659962044067x724/python-sql-sql-server
"""

import dataset

# db = dataset.connect('sqlite:///:memory:') # sqlite 将数据存储到内存中
db = dataset.connect('sqlite:///C:\sqlite\data_wrangling.db')  # sqlite 将数据存储到C盘指定目录中

my_data_source = {  # 创建一个 Python 字典，里面是我们要保存的数据。
    'url':
    'http://www.tsmplug.com/football/premier-league-player-salaries-club-by-club/',
    'description': 'Premier League Club Salaries',
    'topic': 'football',
    'verified': False,
}

table = db['data_sources']  # 创建名为data_sources 的新表
table.insert(my_data_source)  # 将第一个数据源插入新表

another_data_source = {
    'url':
    'http://www.premierleague.com/content/premierleague/en-gb/players/index.html',
    'description': 'Premier League Stats',
    'topic': 'football',
    'verified': True,
}

table.insert(another_data_source)
sources = db['data_sources'].all()  # 显示保存在data_sources 表中的所有数据源

print sources

