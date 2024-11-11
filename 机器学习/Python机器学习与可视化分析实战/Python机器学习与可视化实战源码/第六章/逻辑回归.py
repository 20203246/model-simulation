import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# sigmoid函数和初始化数据
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def init_data():
    X1, Y1 = make_classification(n_samples=200, n_features=2, n_redundant=0, n_clusters_per_class=1, n_classes=2)

    dataMatIn = X1
    classLabels = Y1
    dataMatIn = np.insert(dataMatIn, 0, 1, axis=1)  #特征数据集，添加1是构造常数项x0
    plt.scatter(X1[:, 0], X1[:, 1], c=Y1*10, s=3, marker='*')
    plt.show()
    return dataMatIn, classLabels

# 梯度上升
def grad_descent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)  #(m,n)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMatrix)
    weights = np.ones((n, 1))  #初始化回归系数（n, 1)
    alpha = 0.001 #步长
    maxCycle = 500  #最大循环次数

    for i in range(maxCycle):
        h = sigmoid(dataMatrix * weights)  #sigmoid 函数
        weights = weights + alpha * dataMatrix.transpose() * (labelMat - h)  #梯度
    return weights

# 计算结果
if __name__ == '__main__':
    dataMatIn, classLabels = init_data()
    r = grad_descent(dataMatIn, classLabels)
    print(r)