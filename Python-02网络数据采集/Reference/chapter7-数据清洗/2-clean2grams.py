# 对网页链接格式进行处理2.0：把文本内容分解成n个单词长度的词组

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    input = re.sub('\n+', " ", input)  # 先用一些正则表达式来移除转义字符（\n）
    input = re.sub('\[[0-9]*\]', "", input)  # 把内容中的一个或多个换行符替换成空格
    input = re.sub(' +', " ", input)  # 把连续的多个空格替换成一个空格，确保所有单词之间只有一个空格
    input = bytes(input, "UTF-8")  # 把内容转换成 UTF-8 格式以消除转义字符
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)  #  import string 和 string.punctuation来获取Python所有的标点符号。item.strip(string.punctuation) 对内容两端的任何标点符号都会被去掉，但带连字符的单词（连字符在单词内部）仍然会保留
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
#ngrams = getNgrams(content, 2)
#print(ngrams)
#print("2-grams count is: "+str(len(ngrams)))

ngrams = getNgrams(content, 2)
# collections 库里面有一个 OrderedDict解决：Python中字典是无序的，不能像数组一样直接对 n-gram 序列频率进行排序。字典内部元素的位置不是固定的，排序之后再次使用时还是会变化
# 用排序函数sorted把序列频率转换成OrderedDict对象，并按照频率值排序
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)