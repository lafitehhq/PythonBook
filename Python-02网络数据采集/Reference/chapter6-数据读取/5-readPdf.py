# 使用pdfminer处理pdf格式文件
# Todo:http://blog.csdn.net/MrLevo520/article/details/52136414

# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from io import StringIO
# from io import open
# from urllib.request import urlopen
#
# def readPDF(pdfFile):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, laparams=laparams)
#
#     process_pdf(rsrcmgr, device, pdfFile)
#     device.close()
#
#     content = retstr.getvalue()
#     retstr.close()
#     return content
#
# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = readPDF(pdfFile)
# print(outputString)
# pdfFile.close()

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfdevice import PDFDevice
import urllib
from urllib.request import urlopen
from io import StringIO

def Pdf2Txt(DataIO,Save_path):
    #来创建一个pdf文档分析器
    parser = PDFParser(DataIO)
    #创建一个PDF文档对象存储文档结构
    document = PDFDocument(parser)
    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共赏资源
        rsrcmgr=PDFResourceManager()
        # 设定参数进行分析
        laparams=LAParams()
        # 创建一个PDF设备对象
        # device=PDFDevice(rsrcmgr)
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout=device.get_result()
            for x in layout:
                try:
                    if(isinstance(x,LTTextBoxHorizontal)):
                        with open('%s'%(Save_path),'a') as f:
                            #参数a，表示不会覆盖，直接追加写，和w不一样
                            f.write(x.get_text().encode('utf-8')+'\n')
                except:
                    print("Failed!")


url = "http://pythonscraping.com/pages/warandpeace/chapter1.pdf"
html = urlopen(url).read()
DataIO = StringIO(html)
Pdf2Txt(DataIO, 'b2.txt')

# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = readPDF(pdfFile)
# print(outputString)