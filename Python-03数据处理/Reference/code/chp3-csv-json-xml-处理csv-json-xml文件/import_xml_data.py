# -*-coding:utf8-*-

"""
Description：  
打开JSON文件并将其转换成由字典组成的列表

拓展：
ElementTree库：https://docs.python.org/2/library/xml.etree.elementtree.html
①：文件的扩展名是 .xml或.html或.xhtml都可以用XML解析器来解析。  
②：<Observation />、<Dim />和<Display /> 都是标签。标签（或节点）以层次化和结构化的方式保存数据  
③：在 XML 文件中有两个位置可以保存数据值：一个位置是在两个标签之间；另一个位置是标签的属性
④：在 JSON中可用键 / 值对来保存数据，在 XML 中保存数据可以是两个一组甚至三四个一组
⑤：Display标签值 保存在开始标签和结束标签之间。
⑥：Dim节点 有两个不同的属性（Category 和 Code），两个属性都有对应的值。
⑦：XML文件的核心结构：
<GHO> 
    <Data> 
        <Observation> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Value> 
                <Display> 
                </Display> 
            </Value> 
        </Observation> 
        <Observation> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Dim /> 
            <Value> 
                <Display> 
                </Display> 
            </Value> 
        </Observation> 
    </Data> 
</GHO>
⑧：find 和 findall 的区别在于，find 返回的是匹配的第一个元素，而 findall 返回的是匹配的所有元素。我们知道只有一
个 Data 元素，所以我们用的是 find 而不是 findall。如果有不止一个元素，要用findall方法获取所有匹配元素的列表，然后遍历这些元素。
"""

from xml.etree import ElementTree as ET

tree = ET.parse('../../data/chp3/data-text.xml')  # ET类的parse方法对传入文件中的数据进行解析，返回一个 Python对象（整个 XML对象）并保存在变量 tree 中
root = tree.getroot()  # getroot函数来获取树的根元素,根节点是第一个XML 标签
print root  # 输出的是 XML树中根元素/最外层标签
print '-'*20
print dir(root)
print '-'*20
print list(root)  # 得到由Element对象构成的列表（元素指的是XML节点）；列表包含的 Element 对象分别叫作 QueryParameter、Copyright、Disclaimer、Metadata 和Data。
print '-'*20

data = root.find('Data')  # 根元素的 find 方法可以利用标签名来搜索子元素，该句表示获取 Data 元素的子元素
print data
print '-'*20


all_data = []  # 创建用来保存数据的空列表


for observation in data:
    record = {}  # 创建用来保存数据的空字典

    for item in observation:
        lookup_key = item.attrib.keys()[0]  # 调用attrib()都会得到包含一个或多个键值对的字典;.keys()输出的是每一个属性字典的键;对于同时具有 Category 和 Code 的元素;结尾添加[0]表示需要用 Category 的值作为键，用 Code 的值作为值，即索引（indexing），返回的是列表的第一个元素

        if lookup_key == 'Numeric':  # 当 lookup_key 等于 Numeric 时，望使用 Numeric 作为新字典的键，而不是用它对应的值作为新字典的键（就像Category 键那样）
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]  # 在内层 for 循环中创建一个新变量 rec_key，用来保存 item.attrib[lookup_key] 返回的值
            rec_value = item.attrib['Code']

        record[rec_key] = rec_value
    all_data.append(record)  # 列表的append 方法向列表中添加元素将每一条数据记录添加到 all_data 列表

print all_data  # 得到一个长列表，列表的元素是每一条数据记录组成的字典，与CSV 例子中的相同：
