import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

data = pd.read_csv("./NBA data/球员薪资.csv")
# print(data.head())
# print(data.shape)
# print(data.describe())
data_cor = data.loc[:, ['RPM', 'AGE', 'SALARY_MILLIONS', 'ORB',
                        'DRB', 'TRB','AST', 'STL',
                        'BLK', 'TOV', 'PF',
                        'POINTS', 'GP', 'MPG', 'ORPM', 'DRPM']]

#print(data_cor.head())
# 获取两列数据之间的相关性
corr = data_cor.corr()
#print(corr.iloc[:, 0])
# import seaborn as sns
# sns.heatmap(corr,square=True, linewidths=0.2, annot=False)
# plt.show()
# 薪资最高的10名运动员
print(data.loc[:, ['PLAYER', 'SALARY_MILLIONS', 'RPM', 'AGE', 'MPG']
         ].sort_values(by='SALARY_MILLIONS', ascending=False).head(10))

# 效率值最高的10名运动员
print(data.loc[:, ['PLAYER', 'RPM', 'SALARY_MILLIONS', 'AGE', 'MPG']
      ].sort_values(by='RPM', ascending=False).head(10))
# 出场时间最高的10名运动员
print(data.loc[:, ['PLAYER', 'RPM', 'SALARY_MILLIONS', 'AGE', 'MPG']
      ].sort_values(by='MPG', ascending=False).head(10))
