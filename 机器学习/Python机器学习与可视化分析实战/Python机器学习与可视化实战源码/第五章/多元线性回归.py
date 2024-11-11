import numpy as np

class LinearRegression:
    def __init__(self):
        '''初始化模型'''
        self.coef_ = None
        self.interception_ = None
        self._theta = None

    def fit_normal(self, X_train, y_train):
        '''根据训练数据集X_train,y_train训练模型'''
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]
        return self

    def predict(self, X_predict):
        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return X_b.dot(self._theta)


if __name__ == '__main__':
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    iris = load_iris()
    #获取花瓣长度作为x，花瓣宽度作为y。
    x, y = iris.data[:,2].reshape(-1,1), iris.data[:,3]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

    lr = LinearRegression()
    #使用训练集数据，训练模型。
    lr.fit_normal(x_train, y_train)

    y_hat = lr.predict(x_test)
    print('实际值：', y_test[:5])
    print('预测值：', y_hat[:5])

    import matplotlib.pyplot as plt

    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 15

    plt.figure(figsize=(10, 6))
    plt.scatter(x_train, y_train, c='orange', label='训练集')
    plt.scatter(x_test, y_test, c='g', marker='D', label='测试集')
    plt.plot(x, lr.predict(x), 'r-')
    plt.legend()
    plt.xlabel('花瓣长度')
    plt.ylabel('花瓣宽度')

    plt.show()

    plt.figure(figsize=(15, 6))
    plt.plot(y_test, label='真实值', color='r', marker='o')
    plt.plot(y_hat, c='g', marker='o', ls='--', label='预测值')
    plt.legend()
    plt.show()
