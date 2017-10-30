# 使用zipfile处理word格式文件
# Todo

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

# 把一个远程Word文档读成一个二进制文件对象
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)

# 用zipfile标准库解压二进制文件对象装换成XML
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8')) # 打印验证XML转换是否成功

# 使用BeautifulSoup对csv文件用指定编码格式编码
wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'lxml')

textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)