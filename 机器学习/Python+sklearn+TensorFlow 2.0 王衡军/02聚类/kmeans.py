import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def L2(x:np.array, y:np.array): return np.sqrt(((x-y)**2).sum())
# Jaccard系数（jaccard Coefficient,JC）
def JC(a,b,c): return a / (a + b + c)

# FM指数（Fowlkes and Mallows Index,FMI） sklearn.metrics.adjusted_mutual_info_score(labels_true,labels_pred)
def FMI(a,b,c): return a / ((a+b)*(a+c))**0.5 

'''
官网的
 sklearn.cluster.KMeans(n_clusters=8,
                        init='k-means++',
                        n_init=10,
                        max_iter=300,
                        tol=0.0001,
                        precompute_distances='auto',
                        verbose=0,
                        random_state=None,
                        copy_x=True,
                        n_jobs=None,
                        algorithm='auto')
    def fit(self,X[,y,sample_weightt])...
    def fit_predict(self,X[,y,sample_weight])...
    def fit_transform(self,X[,y,sample_weight])...
    def get_params(self[,deep])...
    def predict(self,X[,sample_weight])...
    def score(self,X[,y,sample_weight])...
    def set_params(self,\*\*params)...
    def transform(self,X)...
'''
def KMeans(X:np.array,k:int,dist=L2):
    '''
    :param X: 样本集
    :param k: 分类的个数
    :dist   : 度量函数
    :return : 标签,k个点中心,误差和
    '''
    n = X.shape[0] # 样本数
    m = X.shape[1] # 特征数
    center = np.zeros((k,m))
    for i in range(m):
        center[:,i] = X[:,i].min() + np.random.randn(k) * (X[:,i].max() - X[:,i].min())
    FlagChanged = True
    tag = np.array([-1]*n)
    while FlagChanged:
        FlagChanged = False
        GlobalCost = 0
        for i in range(n):
            Index = -1
            Cost = np.inf
            for j, cent in enumerate(center):
                CurCost = dist(X[i], cent)
                if CurCost < Cost:
                    Cost = CurCost
                    Index = j
            assert Index != -1, 'data???'
            if tag[i] != Index: FlagChanged = True
            tag[i] = Index
            GlobalCost += dist(center[Index],X[i])
        for i in range(k):
            ans = np.mean(X[tag == i],axis=0)
            if not np.isnan(ans[0]):
                center[i,:] = ans
    return tag, center,GlobalCost
if __name__ == '__main__':
    data, tag = make_blobs(n_samples=200,n_features=2,cluster_std=0.5)
    data = np.array(data)
    tag = np.array(tag)
    for i in range(2):
        data[:,i] = (data[:,i] - data[:,i].min()) / (data[:,i].max() - data[:,i].min())
    predictTag, predictCenter, SSE = KMeans(data,4,L2)
    # plt.scatter(data[:,0],data[:,1],c=tag/10,label='truth')
    plt.scatter(data[:,0],data[:,1],c=predictTag,label='predict')
    # plt.scatter(predictCenter[:,0],predictCenter[:,1],c=np.array(list(range(len(predictCenter)))),marker='*',linewidths=3)
    for i in range(len(predictCenter)):
        plt.text(predictCenter[i,0],predictCenter[i,1],s='i='+str(i))
    plt.title(f"{SSE=}")
    plt.show()
