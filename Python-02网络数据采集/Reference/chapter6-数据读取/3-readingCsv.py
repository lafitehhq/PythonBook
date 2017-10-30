# 使用csv.reader()读取csv文件

from urllib.request import urlopen
from io import StringIO
import csv

# 使用BeautifulSoup获取网页源代码并把源代码转换成字符串
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')  # read()：从网上文件读成一个字符串;.decode()：对字符串以ascii格式进行编码
# StringIO()方法：将字符串封装成StringIO对象
dataFile = StringIO(data)

# csv.reader()：把csv文件某行某列中的值返回
csvReader = csv.reader(dataFile)  # csv.reader()：对StringIO对象转换成可迭代的csvReader对象
for row2 in csvReader:
	print("The album \""+row2[0]+"\" was released in "+str(row2[1]))
