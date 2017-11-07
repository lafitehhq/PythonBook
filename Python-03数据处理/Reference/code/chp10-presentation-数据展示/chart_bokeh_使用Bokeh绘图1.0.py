
"""
Description:
    使用 Bokeh，基于各国家创建一个 CPI 和童工数据的散点图。
拓展：
Bokeh（http://bokeh.pydata.org/）是一个 Python 绘图库，能够用相当简单的命令来绘制更
复杂的图表类型。如果想要创建一个条形图、散点图或时间序列图，尝试Bokeh，看看是
否合适。使用 Bokeh，基于各国家创建一个 CPI 和童工数据的散点图。
"""
from bokeh.plotting import figure, show, output_file

# NOTE: You'll need to have 'africa_cpi_cl' table from Chapter 9 to use this
# code.


def scatter_point(chart, x, y, marker_type):  # 定义一个函数，scatter_point，接受一个图表、x 轴和 y 轴值、标记的类型（圆形、正方形、矩形），并且添加这些点到图表中。
    chart.scatter(x, y, marker=marker_type, line_color="#6666ee",
                  fill_color="#ee6666", fill_alpha=0.7, size=10)  # 图表的 scatter 方法需要两个必需的参数（x 轴和 y 轴）和一些不同的关键参数，为这些点添加样式（包括颜色、透明度、大小）。这行代码传递了边缘颜色和填充颜色以及大小和透明度到函数中。

chart = figure(title="Perceived Corruption and Child Labor in Africa")  # 使用函数 figure创建图表，同时传入一个标题。
output_file("scatter_plot.html")  # 使用函数output_file 定义输出的文件。这会在你运行代码的文件夹下创建文件scatter_plot.html。

for row in africa_cpi_cl.rows:
    scatter_point(chart, float(row['CPI 2013 Score']),
                  float(row['Total (%)']), 'circle')  # 对于每一行数据，使用CPI得分作为x 轴，童工雇用率作为 y 轴，添加一个数据点。

show(chart)  # 在浏览器窗口中展示这张图表。

