import numpy as np
import pandas as pd
import random
import sys
import time
import numpy as np

class KMeansClusterer:
    def __init__(self, ndarray, cluster_num):
        self.ndarray = ndarray
        self.cluster_num = cluster_num
        self.points = self.__pick_start_point(ndarray, cluster_num)

    def cluster(self):
        result = []
        for i in range(self.cluster_num):
            result.append([])
        for item in self.ndarray:
            distance_min = sys.maxsize
            index = -1
            for i in range(len(self.points)):
                distance = self.__distance(item, self.points[i])
                if distance < distance_min:
                    distance_min = distance
                    index = i
            result[index] = result[index] + [item.tolist()]
        new_center = []
        for item in result:
            new_center.append(self.__center(item).tolist())
        # 中心点未改变，说明达到稳态，结束递归
        if (self.points == new_center).all():
            return result

        self.points = np.array(new_center)

        return np.array(self.cluster())

    def __center(self, list):
        '''计算一组坐标的中心点
        '''
        # 计算每一列的平均值
        return np.array(list).mean(axis=0)

    def __distance(self, p1, p2):
        '''计算两点间距
        '''
        tmp = 0
        for i in range(len(p1)):
            tmp += pow(p1[i] - p2[i], 2)
        return pow(tmp, 0.5)

    def __pick_start_point(self, ndarray, cluster_num):

        if cluster_num < 0 or cluster_num > ndarray.shape[0]:
            raise Exception("簇数设置有误")

        # 随机点的下标
        indexes = random.sample(np.arange(0, ndarray.shape[0], step=1).tolist(), cluster_num)
        points = []
        for index in indexes:
            points.append(ndarray[index].tolist())
        return np.array(points)


if __name__ == '__main__':
    array = np.random.random(size=(1024,2))
    k_means = KMeansClusterer(array,cluster_num=3)
    cluster = (k_means.cluster())

    x_0 = [];y_0 = []
    for pari in (cluster[0]):
        x_0.append(pari[0])
        y_0.append(pari[1])

    x_1 = [];y_1 = []
    for pari in (cluster[1]):
        x_1.append(pari[0])
        y_1.append(pari[1])


    x_2 = [];y_2 = []
    for pari in (cluster[2]):
        x_2.append(pari[0])
        y_2.append(pari[1])

    import matplotlib.pyplot as plt

    plt.scatter(x_0, y_0, marker='o')
    plt.scatter(x_1, y_1, marker='^')
    plt.scatter(x_2, y_2, marker='*')


    plt.colorbar()
    plt.show()