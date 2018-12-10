import matplotlib.pyplot as plt
'''绘制点'''

x_values = [1,2,3,4,5]
y_vlaues = [1,4,9,16,25]
# plt.scatter(2,4,s=2000)
plt.scatter(x_values,y_vlaues,s=200)
#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()