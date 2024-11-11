import numpy as np
import matplotlib.pyplot as plt

r"""
用以实现: $f(x)=ax+b \sigma=\sum(f(x_i)-y_i)^2$ 最小
"""
m = 20 # 数据集个数
x0 = np.ones((m,1))
x1 = np.arange(1,m+1).reshape((m,1))
x = np.hstack((x0,x1)) # (m,2)
y = np.array([
    3,4,5,5,2,4,7,8,11,8,12,
    11,13,13,16,17,18,17,19,21
]).reshape(m,1) # (m,1)

alpha = 1e-2
def error_function(theta,x,y):
    h_pred = np.dot(x,theta)
    ...

