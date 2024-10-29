import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
iris_data = datasets.load_iris()
data = pd.DataFrame(iris_data.data,columns=['SpealLength', 'Spealwidth', 'PetalLength', 'Petalwidth'])
data['Species'] = iris_data['target']

from sklearn.model_selection import train_test_split
X = data.iloc[:,:2].values
Y = data['Species']
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=0)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(penalty='l2',solver='newton-cg',multi_class='multinomial')
lr.fit(x_train,y_train)
print(f'LR模型训练集准确率:{lr.score(x_train,y_train)}')
print(f'LR模型测试集准确率:{lr.score(x_test,y_test)}')

x1_min, x1_max = X[:,0].min() - .5, X[:,0].max() + .5
x2_min, x2_max = X[:,1].min() - .5, X[:,1].max() + .5
h = .02
x1, x2 = np.meshgrid(np.arange(x1_min,x1_max,h),np.arange(x2_min,x2_max,h))
grid_test = np.stack((x1.flat,x2.flat),axis=1)
grid_hat = lr.predict(grid_test)
grid_hat = grid_hat.reshape(x1.shape)

plt.figure(1,figsize=(6,5))
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pcolormesh(x1,x2,grid_hat,cmap=plt.cm.Paired)
plt.scatter(X[:50,0],X[:50,1],marker='*',edgecolors='red',label='setosa')
plt.scatter(X[50:100,0],X[50:100,1],marker='+',edgecolors='k',label='versicolor')
plt.scatter(X[100:150,0],X[100:150,1],marker='o',edgecolors='k',label='virginica')
plt.xlabel('花萼长度-Sepal length')
plt.ylabel('花萼宽度-Sepal width')
plt.legend(loc=2)
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
plt.title('Logistic Regression 鸢尾花分类结果', fontsize=15)
plt.xticks(())
plt.yticks(())
plt.grid()
plt.show()