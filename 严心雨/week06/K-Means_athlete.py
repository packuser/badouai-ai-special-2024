from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
"""
第一部分：数据集
X表示二维矩阵数据，篮球运动员比赛数据
总共20行，每行两列数据
第一列表示球员每分钟助攻数：assists_per_minute
第二列表示球员每分钟得分数：points_per_minute
"""
X = [[0.0888, 0.5885],
     [0.1399, 0.8291],
     [0.0747, 0.4974],
     [0.0983, 0.5772],
     [0.1276, 0.5703],
     [0.1671, 0.5835],
     [0.1306, 0.5276],
     [0.1061, 0.5523],
     [0.2446, 0.4007],
     [0.1670, 0.4770],
     [0.2485, 0.4313],
     [0.1227, 0.4909],
     [0.1240, 0.5668],
     [0.1461, 0.5113],
     [0.2315, 0.3788],
     [0.0494, 0.5590],
     [0.1107, 0.4799],
     [0.1121, 0.5735],
     [0.1007, 0.6318],
     [0.2567, 0.4326],
     [0.1956, 0.4280]
    ]

"""
第二部分：KMeans聚类
clf = KMeans(n_clusters=3) 表示类簇数为3，聚成3类数据，clf即赋值为KMeans
y_pred = clf.fit_predict(X) 载入数据集X，并且将聚类的结果赋值给y_pred
"""
clf = KMeans(n_clusters=3)
y_pred = clf.fit_predict(X)

# 输出完整Kmeans函数，包括很多省略参数
print(clf)
# 输出聚类预测结果
print("y_pred = ", y_pred)

"""
第三部分：可视化绘图
"""
#获取数据集的第一列和第二列数据 使用for循环获取 n[0]表示X第一列
x=[n[0] for n in X]
y=[n[1] for n in X]

print('第一列\n',x)
print('第二列\n',y)
''' 
绘制散点图 
参数：x横轴; y纵轴; c=y_pred聚类预测结果; marker类型:o表示圆点,*表示星型,x表示点;
'''
plt.scatter(x,y,c=y_pred,marker='o')

"""绘制标题"""
plt.title("Kmeans-Basketball Data")

"""绘制X轴和Y轴"""
plt.xlabel("assists_per_minute")
plt.ylabel("points_per_minute")

"""设置图例"""
plt.legend(['a','b','c'])

plt.show()
