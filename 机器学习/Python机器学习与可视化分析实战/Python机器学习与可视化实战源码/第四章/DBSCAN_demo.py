import matplotlib.pyplot as plt
import random
import numpy as np
import math
import DBSCAN
from sklearn import datasets

list_1 = []
list_2 = []

def loadDataSet(fileName, splitChar='\t'):
    dataSet = []
    with open(fileName) as fr:
        for line in fr.readlines():
            curline = line.strip().split(splitChar)
            fltline = list(map(float, curline))
            dataSet.append(fltline)
    return dataSet

dataSet = loadDataSet('dbscan.txt', splitChar=',')
C = DBSCAN.dbscan(dataSet, 2, 7)
x = []
y = []
for data in dataSet:
    x.append(data[0])
    y.append(data[1])
plt.scatter(x, y, c=C, marker='o')
plt.show()

