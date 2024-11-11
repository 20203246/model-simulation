# 导入所需要的包
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn import datasets
import pandas as np

from sklearn import datasets
import pandas as np

iris_datas = datasets.load_iris()

data = pd.DataFrame(iris_datas.data, columns=['SpealLength', 'Spealwidth', 'PetalLength', 'PetalLength'])
data["Species"] = iris_datas.target
print(data.head())

#print(data['Species'].value_counts())

#data.plot.scatter(x='Spealwidth' , y='SpealLength' , c='green')
#plt.show()

#data.plot.scatter(x='Spealwidth' , y='SpealLength' , c='Species' , colormap='viridis')
#plt.show()

# import seaborn as sns
# sns.relplot(x='Spealwidth' , y='SpealLength' , hue='Species' , data=data)
# plt.show()

# data.hist()
# plt.show()

# data.plot(kind = "kde")
# plt.show()


# data.plot(kind='box', subplots=True, layout=(2,3), sharex=False, sharey=False)
# plt.show()

# from pandas.plotting import radviz
# radviz(data,'Species')
# plt.show()

# from pandas.plotting import andrews_curves
# andrews_curves(data,'Species')
# plt.show()

# from pandas.plotting import parallel_coordinates
# parallel_coordinates(data,'Species')
# plt.show()

# from pandas.plotting import scatter_matrix
# scatter_matrix(data, alpha=0.2, figsize=(7, 7), diagonal='kde')
# plt.show()

# from sklearn import decomposition
# pca = decomposition.PCA(n_components=2)
# X = pca.fit_transform(data.iloc[:,:-1].values)
# pos = pd.DataFrame()
# pos['X'] = X[:,0]
# pos['Y'] = X[:,1]
# pos['Species'] = data['Species']
#
# ax = pos[pos['Species']==0].plot(kind='scatter', x='X', y='Y', marker = '*',color='blue', label='Iris-virginica')
# ax = pos[pos['Species']==1].plot(kind='scatter', x='X', y='Y', marker = 's', color='green', label='Iris-setosa', ax=ax)
# ax = pos[pos['Species']==2].plot(kind='scatter', x='X', y='Y', color='red', label='Iris-versicolor', ax=ax)
# plt.show()
#

# from sklearn import decomposition
# pca = decomposition.FactorAnalysis(n_components=2)
# X = pca.fit_transform(data.iloc[:,:-1].values)
# pos = pd.DataFrame()
# pos['X'] = X[:,0]
# pos['Y'] = X[:,1]
# pos['Species'] = data['Species']
# ax = pos[pos['Species']==0].plot(kind='scatter', x='X', y='Y', marker = '*', color='blue', label='Iris-virginica')
# ax = pos[pos['Species']==1].plot(kind='scatter', x='X', y='Y', marker = 's', color='green', label='Iris-setosa', ax=ax)
# ax = pos[pos['Species']==2].plot(kind='scatter', x='X', y='Y', color='red', label='Iris-versicolor', ax=ax)
# plt.show()



# from sklearn import decomposition
# pca = decomposition.FastICA(n_components=2)
# X = pca.fit_transform(data.iloc[:,:-1].values)
# pos = pd.DataFrame()
# pos['X'] = X[:,0]
# pos['Y'] = X[:,1]
# pos['Species'] = data['Species']
# ax = pos[pos['Species']==0].plot(kind='scatter', x='X', y='Y', marker = '*', color='blue', label='Iris-virginica')
# ax = pos[pos['Species']==1].plot(kind='scatter', x='X', y='Y', marker = 's', color='green', label='Iris-setosa', ax=ax)
# ax = pos[pos['Species']==2].plot(kind='scatter', x='X', y='Y', color='red', label='Iris-versicolor', ax=ax)
# plt.show()

from sklearn import manifold
from sklearn.metrics import euclidean_distances
similarities = euclidean_distances(data.iloc[:,:-1].values)
mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, dissimilarity='precomputed', n_jobs=1)
X = mds.fit(similarities).embedding_
pos = pd.DataFrame(X, columns=['X','Y'])
pos['Species'] = data['Species']
ax = pos[pos['Species']==0].plot(kind='scatter', x='X', y='Y', marker = '*', color='blue', label='Iris-virginica')
ax = pos[pos['Species']==1].plot(kind='scatter', x='X', y='Y', marker = 's', color='green', label='Iris-setosa', ax=ax)
ax = pos[pos['Species']==2].plot(kind='scatter', x='X', y='Y', color='red', label='Iris-versicolor', ax=ax)
plt.show()




