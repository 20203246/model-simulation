import numpy as np
import matplotlib.pyplot as plt

class SingleLinearRegression:
    def __init__(self):   #初始化a,b
        self.a_=None;
        self.b_=None;

    def fit(self,x_train,y_train):  #训练函数，训练出a,b
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)  # 求x和y的平均值

        fenzi = 0.0;
        fenmu = 0.0;  # 对分子分母初始化
        for x_i, y_i in zip(x_train, y_train):  # 将x,y打包成元组的形式
            fenzi += (x_i - x_mean) * (y_i - y_mean)  # 根据最小二乘法求出参数
            fenmu += (x_i - x_mean) ** 2

        self.a_ = fenzi / fenmu
        self.b_ = y_mean - self.a_ * x_mean  #得到a,b

        return self

    def predict(self,x_test_group):  #预测函数，用户输入一组x（为一维向量）,可以进行y的预测
        result=[]  #初始化一个列表，用来储存预测的y值
        for x_test in x_test_group:  #对于每个输入的x都计算它对应的预测y值并加入列表中
            result.append(self.a_*x_test+self.b_)
        y_predict=np.array(result)  #将列表转换为矩阵向量形式方便运算

        return y_predict

    def r_square(self,y_true,y_predict):  #打分函数，评估该模型的准确率
        mse=np.sum((y_true-y_predict)**2)/len(y_true)  #计算均方误差mse
        var=np.var(y_true)  #计算方差
        r=1-mse/var #计算拟合优度r的平方
        return r

    def get_variable(self):
        return self.a_,self.b_

if __name__=='__main__':
    x = np.array([8, 12, 13, 15, 17])
    y = np.array([19, 26, 30, 35, 39])
    l=SingleLinearRegression()  #创建一个对象，接下来调用对象的方法
    l.fit(x,y)

    #画出散点图和预测图
    plt.scatter(x, y, color='b')  # 画出原来值得散点图
    plt.plot(x,l.predict(x), color='r')  # 画出预测后的线

    plt.xlabel('x')  # 写上标签
    plt.ylabel('y')

    plt.show()  # 作图函数


    a,b = l.get_variable()
    print(a,b)