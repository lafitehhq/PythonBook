import pygal

# NOTE: you'll need the 'ranked' table from Chp 9 with the ISO codes added
# (see: add_iso_data.py)

worldmap_chart = pygal.Worldmap()  # pygal库中 map.world模块的 World 类返回地图对象。
worldmap_chart.title = 'Child Labor Worldwide'

cl_dict = {}
for r in ranked.rows:
    cl_dict[r.get('country_code_complete').lower()] = r.get('Total (%)')  # cl_dict保存着一个字典，键是国家编码，值是童工百分比。

worldmap_chart.add('Total Child Labor (%)', cl_dict)  # 根据pygal 的文档，这行代码传递数据的标签和数据字典到函数中。
worldmap_chart.render()  # 调用地图的render 方法来展示地图。
