from sklearn.datasets import load_iris           #导入数据集
from sklearn.decomposition import PCA            #导入函数库
from 第四章 import k_means
import matplotlib.pyplot as plt
import numpy as np
iris=load_iris()
pca=PCA(n_components=2,random_state=17)                           #设置保留的主成分个数为2
trans_data=pca.fit_transform(iris.data)           #调用fit_transform方法，返回新的数据集

k_means = k_means.KMeansClusterer(trans_data,cluster_num=3)
cluster = (k_means.cluster())

x_0 = [];
y_0 = []
for pari in (cluster[0]):
    x_0.append(pari[0])
    y_0.append(pari[1])

x_1 = [];
y_1 = []
for pari in (cluster[1]):
    x_1.append(pari[0])
    y_1.append(pari[1])

x_2 = [];
y_2 = []
for pari in (cluster[2]):
    x_2.append(pari[0])
    y_2.append(pari[1])

import matplotlib.pyplot as plt

plt.scatter(x_0, y_0, marker='o',)
plt.scatter(x_1, y_1, marker='^')
plt.scatter(x_2, y_2, marker='*')
plt.colorbar()
plt.show()


index1=np.where(iris.target==0)
index2=np.where(iris.target==1)
index3=np.where(iris.target==2)
labels=['setosa', 'versicolor', 'virginica']
plt.plot(trans_data[index1][:,0],trans_data[index1][:,1],'r*', marker='o')
plt.plot(trans_data[index2][:,0],trans_data[index2][:,1],'g*', marker='^')
plt.plot(trans_data[index3][:,0],trans_data[index3][:,1],'b*', marker='*')
plt.legend(labels)
plt.show()
