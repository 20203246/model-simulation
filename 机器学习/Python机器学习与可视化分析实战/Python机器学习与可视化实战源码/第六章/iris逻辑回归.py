# 导入所需要的包
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris_datas = datasets.load_iris()

data = pd.DataFrame(iris_datas.data, columns=['SpealLength', 'Spealwidth', 'PetalLength', 'Petalwidth'])
data["Species"] = iris_datas.target

# groups = data.groupby(by = "Species")
# means, sds = groups.mean(), groups.std()
# means.plot(yerr = sds, kind = 'bar', figsize = (9, 9), table = True)
# plt.show()

# col_map = {0: 'orange', 1: 'green', 2: 'pink'}
# pd.plotting.scatter_matrix(data.loc[:, 'SpealLength':'Spealwidth']
# , diagonal = 'kde', color = [col_map[lb] for lb in data['Species']], s = 75, figsize = (11, 6))
# plt.show()

from sklearn.model_selection import train_test_split
import chart_studio.plotly as py
import plotly.graph_objs as go
X = data.iloc[:,:2].values            # 取前两列数据
Y = data["Species"]
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.3, random_state = 0)

# plt.scatter(x = X[:,0], y = X[:,1])
# plt.show()

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(penalty='l2',solver='newton-cg',multi_class='multinomial')
lr.fit(x_train,y_train)

print("Logistic Regression模型训练集的准确率：%.3f" %lr.score(x_train, y_train))
print("Logistic Regression模型测试集的准确率：%.3f" %lr.score(x_test, y_test))

x1_min, x1_max = X[:, 0].min() - .5, X[:, 0].max() + .5 # 第0列的范围
x2_min, x2_max = X[:, 1].min() - .5, X[:, 1].max() + .5 # 第1列的范围
h = .02
x1, x2 = np.meshgrid(np.arange(x1_min, x1_max, h), np.arange(x2_min, x2_max, h)) # 生成网格采样点
grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点
grid_hat = lr.predict(grid_test)                  # 预测分类值
# grid_hat = lr.predict(np.c_[x1.ravel(), x2.ravel()])
grid_hat = grid_hat.reshape(x1.shape)             # 使之与输入的形状相同
plt.figure(1, figsize=(6, 5))
# 预测值的显示, 输出为三个颜色区块，分布表示分类的三类区域
plt.pcolormesh(x1, x2, grid_hat,cmap=plt.cm.Paired)

# plt.scatter(X[:, 0], X[:, 1], c=Y,edgecolors='k', cmap=plt.cm.Paired)
plt.scatter(X[:50, 0], X[:50, 1], marker = '*', edgecolors='red', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], marker = '+', edgecolors='k', label='versicolor')
plt.scatter(X[100:150, 0], X[100:150, 1], marker = 'o', edgecolors='k', label='virginica')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend(loc = 2)

plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
plt.title("Logistic Regression", fontsize = 15)
plt.xticks(())
plt.yticks(())
plt.grid()

plt.show()


