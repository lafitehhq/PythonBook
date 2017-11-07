
"""
Description:
    使用matplotlib绘制图表,展示政府腐败感得分和童工雇用率的相关性
拓展：
pylab(http://matplotlib.org/1.4.2/users/pyplot_tutorial.html#pyplottutorial)
有很多种图表可用，包括直方图、散点图、条形图和饼形图。

"""
import matplotlib.pyplot as plt

# NOTE: You'll need to have the 'africa_cpi_cl' table and 'highest_cpi_cl'
# table we worked on in Chapter 9.

plt.plot(africa_cpi_cl.columns['CPI 2013 Score'],
         africa_cpi_cl.columns['Total (%)'])  # 使用 pylab 的 plot 方法，传递 x 和 y 的标签数据。传递的第一个变量是 x 坐标系，第二个变量是y坐标系。这会创建一个 Python 图表，绘制这两个数据集。
plt.xlabel('CPI Score - 2013')  # 调用xlabel 和ylabel 方法标记图表坐标系
plt.ylabel('Child Labor Percentage')
plt.title('CPI & Child Labor Correlation')  # 调用title 方法为图表命名
plt.show() # 调用 show 方法来绘制图表。所有在调用show 之前关于图表的操作，会显示在系统默认的图片程序中（例如 Preview 或 Windows 图片查看器）。标题、坐标标签和任何其他通过 matplotlib 设置的属性都会展示在这个图表中。

plt.plot(highest_cpi_cl.columns['CPI 2013 Score'],
         highest_cpi_cl.columns['Total (%)'])
plt.xlabel('CPI Score - 2013')
plt.ylabel('Child Labor Percentage')
plt.title('CPI & Child Labor Correlation')
plt.show()
