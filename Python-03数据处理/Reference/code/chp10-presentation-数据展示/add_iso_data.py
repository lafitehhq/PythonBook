import json

# NOTE: you will need the 'ranked' table we first created in Chapter 9.

country_codes = json.loads(open('../../data/chp10/iso-2-cleaned.json', 'rb').read())  # 加载从GitHub用户@lukes仓库下载的文件iso-2.json中的字符串
country_dict = {}

for c in country_codes:
    country_dict[c.get('name')] = c.get('alpha-2')  # 创建国家字典，键是国家名称，值是ISO 编码。

def get_country_code(row):
    return country_dict.get(row['Countries and areas'])  # 定义新的函数get_country_code，接受一行数据，使用country_dict 返回国家编码。如果没有对应键，返回None。

ranked = ranked.compute([(agate.Formula(text_type, get_country_code),
                          'country_code')])

for r in ranked.where(lambda x: x.get('country_code') is None).rows:  # 查看没有匹配到的数据，做进一步的研究。
    print r['Countries and areas']
