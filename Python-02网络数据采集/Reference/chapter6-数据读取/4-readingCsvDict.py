# 使用csv.DictReader()读取csv文件

from urllib.request import urlopen
from io import StringIO
import csv

# 使用BeautifulSoup获取网页源代码并把源代码转换成字符串
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
# StringIO()方法：将字符串封装成StringIO对象
dataFile = StringIO(data)

# csv.DictReader()：把CSV文件每一行转换成Python的字典对象返回
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
    print(row)