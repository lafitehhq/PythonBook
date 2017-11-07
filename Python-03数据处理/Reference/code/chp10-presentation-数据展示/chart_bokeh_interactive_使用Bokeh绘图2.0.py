
"""
Description:
    使用 Bokeh，基于各国家创建一个 CPI 和童工数据的散点图。
拓展：
①：Bokeh 有一个很好的示例库（http://bokeh.pydata.org/en/latest/docs/gallery.html）和可用的代
码来帮助你上手。建议你花些时间在图表上，尝试一下Bokeh。
"""

from bokeh.plotting import ColumnDataSource, figure, show, output_file  # 导入我们用过的主要的库，并导入 ColumnDataSource和HoverTool 类。
from bokeh.models import HoverTool

# NOTE: For this chart, you will also need the 'africa_cpi_cl' table from
# Chapter 9.


TOOLS = "pan,reset,hover"  # 为最终的图表定义你想要使用的工具（http://bokeh.pydata.org/en/latest/docs/user_guide/tools.html#specifying-tools）。这行代码添加了hover，所以可以使用悬停方法。


def scatter_point(chart, x, y, source, marker_type):  # 把source 添加到必需的参数中。这会存储国家名称信息。
    chart.scatter(x, y, source=source, marker=marker_type,
                  line_color="#6666ee", fill_color="#ee6666",
                  fill_alpha=0.7, size=10)  # 图表的 scatter 方法需要两个必需的参数（x 轴和 y 轴）和一些不同的关键参数，为这些点添加样式（包括颜色、透明度、大小）。这行代码传递了边缘颜色和填充颜色以及大小和透明度到函数中。

chart = figure(title="Perceived Corruption and Child Labor in Africa",
               tools=TOOLS)  # 传递TOOLS变量到图片初始化函数中。

output_file("scatter_int_plot.html")

for row in africa_cpi_cl.rows:
    column_source = ColumnDataSource(
        data={'country': [row['Country / Territory']]})  # 变量 column_source 现在保存着一个数据源字典，其中是国家名称。这一行代码将国家名称作为列表传递，因为字典的值必须是一个可迭代对象。
    scatter_point(chart, float(row['CPI 2013 Score']),
                  float(row['Total (%)']), column_source, 'circle')  # 对于每一行数据，使用CPI得分作为x 轴，童工雇用率作为 y 轴，添加一个数据点。

hover = chart.select(dict(type=HoverTool))  # 从图表中选择 HoverTool 对象
hover.tooltips = [
    ("Country", "@country"),  # 使用悬停对象的 tooltips 方法，展示不同的数据属性。@country 选择了通过列数据源传入的数据，而$x 和$y 选择图表中x 和y数据点。
    ("CPI Score", "$x"),
    ("Child Labor (%)", "$y"),
]

show(chart)
