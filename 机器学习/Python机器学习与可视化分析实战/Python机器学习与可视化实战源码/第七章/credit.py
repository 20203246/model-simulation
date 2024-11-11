import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PowerTransformer
from sklearn.linear_model import LinearRegression,LassoCV,LogisticRegression
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.model_selection import KFold,train_test_split,StratifiedKFold,GridSearchCV,cross_val_score

import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

df0 = pd.read_csv('./信用卡违约/cs-training.csv')
df0 = df0.drop('Unnamed: 0',axis=1)
# 为方便查看调整列名为中文
df0.rename(columns = {'SeriousDlqin2yrs':'未来两年可能违约', 'RevolvingUtilizationOfUnsecuredLines':'可用信贷额度比例', 'age':'年龄',
       'NumberOfTime30-59DaysPastDueNotWorse':'逾期30-59天的笔数', 'DebtRatio':'负债率', 'MonthlyIncome':'月收入',
       'NumberOfOpenCreditLinesAndLoans':'信贷数量', 'NumberOfTimes90DaysLate':'逾期90天+的笔数',
       'NumberRealEstateLoansOrLines':'固定资产贷款数', 'NumberOfTime60-89DaysPastDueNotWorse':'逾期60-89天的笔数',
       'NumberOfDependents':'家属数量'},inplace=True)

# print(df0.head().T)
# print(df0.describe().T)
#
# print(df0.info())
# print(df0.isnull().sum())

# plt.figure(figsize=(20,20),dpi=300)
# plt.subplots_adjust(wspace =0.3, hspace =0.3)
# for n,i in enumerate(df0.columns):
#     plt.subplot(4,3,n+1)
#     plt.title(i,fontsize=15)
#     plt.grid(linestyle='--')
#     df0[i].hist(color='grey',alpha=0.5)
#
# plt.show()

# 通过箱型图观察各字段异常情况
# 负债率异常值（错误）较多；可用信贷额度比例 异常值（错误）较多，理论应小于或等于1
#  '逾期30-59天的笔数', '负债率', '月收入','逾期90天+的笔数', '固定资产贷款数', '逾期60-89天的笔数'异常值非常多，难以观察数据分布。
# 年龄方面异常值有待观察
# plt.figure(figsize=(20,20),dpi=300)
# plt.subplots_adjust(wspace =0.3, hspace =0.3)
# for n,i in enumerate(df0.columns):
#     plt.subplot(4,3,n+1)
#     plt.title(i,fontsize=15)
#     plt.grid(linestyle='--')
#     df0[[i]].boxplot(sym='.')
# plt.show()

# 由图可知，逾期笔数这三个字段，共线性极高，可考虑去除共线性
# plt.figure(figsize=(10,5),dpi=300)
# sns.heatmap(df0.corr(),cmap='Reds',annot=True)
# plt.show()

from 第七章 import credit_untils
# 从数据初探可以发现，'未来两年可能违约'标签类别分布不均，需对样本进行重取样
df1 = df0.copy()
print(df0.shape)
df1 = credit_untils.error_processing(df1)
df1 = credit_untils.collineation_processing(df1,'逾期90天+的笔数', '逾期60-89天的笔数', '逾期30-59天的笔数','逾期60-89天/30-59天')
df1 = credit_untils.missing_values_processing(df1,func1=1,func2=1)
df1 = credit_untils.resample(df1)

# 最后将数据集划分成训练集和验证集，两者划分比例都为8：2
# 可考虑删去的列：'逾期30-59天的笔数','逾期60-89天的笔数','逾期90天+的笔数','逾期60-89天/30-59天','未来两年可能违约'
X = df1.drop(['未来两年可能违约','逾期60-89天/30-59天'],axis=1)
y = df1['未来两年可能违约']
xtrain,xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state = 17)

# 分层k折交叉拆分器 - 用于网格搜索
cv = StratifiedKFold(n_splits=3,shuffle=True)

# 随机森林分类模型
rf_clf = RandomForestClassifier(criterion='gini',
                               n_jobs=-1,
                               n_estimators=1000)    # random_state
# 参数设定
rf_grid_params = {'max_features':['auto'],    # ['auto',0.5,0.6,0.9] 未知最优参数时可以自己设定组合
                    'max_depth':[6,9]}    # [3,6,9]
# 参数搜索
rf_gridsearch = GridSearchCV(rf_clf,rf_grid_params,cv=cv,
                               n_jobs=-1,scoring='roc_auc',verbose=10,refit=True)
# 工作流管道
pipe_rf = Pipeline([
        ('sc',StandardScaler()),
        ('pow_trans',PowerTransformer()),
        ('rf_grid',rf_gridsearch)
        ])
# 搜索参数并训练模型
pipe_rf.fit(xtrain,ytrain)
# 最佳参数组合
print(pipe_rf.named_steps['rf_grid'].best_params_)
# 训练集性能指标
credit_untils.perfomance_clf(pipe_rf,xtrain,ytrain,name='train')
# 测试集性能指标
credit_untils.perfomance_clf(pipe_rf,xtest,ytest,name='test')


