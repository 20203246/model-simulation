# 导入所需要的包
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go
from sklearn.decomposition import PCA
from sklearn import datasets
import pandas as np

from sklearn import datasets
import pandas as np

iris_datas = datasets.load_iris()

data = pd.DataFrame(iris_datas.data, columns=['SpealLength', 'Spealwidth', 'PetalLength', 'Petalwidth'])
data["Species"] = iris_datas.target

# pos = pd.DataFrame(data)
# #获取花瓣的长和宽，转换Series为ndarray
# x = pos['PetalLength'].values
# y = pos['Petalwidth'].values
# x = x.reshape(len(x),1)
# y = y.reshape(len(y),1)
#
# from sklearn.linear_model import LinearRegression
# clf = LinearRegression()
# clf.fit(x,y)
# pre = clf.predict(x)
#
# plt.scatter(x,y,s=100)
# plt.plot(x,pre,'r-',linewidth=4)
# for idx, m in enumerate(x):
#     plt.plot([m,m],[y[idx],pre[idx]], 'g-')
# plt.show()
#
# print("系数：", clf.coef_)
# print("截距：", clf.intercept_)


from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
iris = load_iris()
clf = KMeans()
clf.fit(iris.data,iris.target)
predicted = clf.predict(iris.data)

pos = pd.DataFrame(data)
L1 = pos['SpealLength'].values
L2 = pos['Spealwidth'].values

plt.scatter(L1, L2, c=predicted, marker='s',s=100,cmap=plt.cm.Paired)
plt.title("KMeans")
plt.show()




