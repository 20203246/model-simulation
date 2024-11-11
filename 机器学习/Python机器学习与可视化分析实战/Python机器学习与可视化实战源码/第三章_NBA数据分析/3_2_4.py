import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

data = pd.read_csv("./NBA data/球员薪资.csv")


### 分组操作 按球队
dat_grp=data.groupby(by=['TEAM'],as_index=False).agg({'SALARY_MILLIONS':np.mean,'RPM':np.mean,'PLAYER':np.size})
dat_grp=dat_grp.loc[dat_grp.PLAYER>5]  #不考虑在赛季中转会的球员
#print(dat_grp.sort_values(by='SALARY_MILLIONS', ascending=False).head(10))

#根据已有变量生成新的变量
data['avg_point']=data['POINTS']/data['MP'] #每分钟得分
def age_cut(df):
    if df.AGE<=24:
        return 'young'
    elif df.AGE>=30:
        return 'old'
    else:
        return 'best'
data['age_cut']=data.apply(lambda x: age_cut(x),axis=1) #球员是否处于黄金年龄
data['cnt']=1 #计数用

### 分组操作 按场上位置
dat_grp2=data.groupby(by=['TEAM','age_cut'],as_index=False).agg({'SALARY_MILLIONS':np.mean,'RPM':np.mean,'PLAYER':np.size})
dat_grp2=dat_grp2.loc[dat_grp2.PLAYER>3]     ##剔除掉少量的position摇摆人
#print(dat_grp2.sort_values(by=['PLAYER', 'RPM'], ascending=False).head(15))




sns.set_style('whitegrid')#设置seaborn的面板风格
plt.figure(figsize=(12,8))
dat_grp4=data[data['TEAM'].isin(['GS','CLE','SA','LAC','OKC','UTAH','CHA','TOR','NO','BOS'])]
plt.subplot(3,1,1)
sns.boxplot(x='TEAM',y='AGE',data=dat_grp4)
plt.subplot(3,1,2)
sns.boxplot(x='TEAM',y='SALARY_MILLIONS',data=dat_grp4)
plt.subplot(3,1,3)
sns.boxplot(x='TEAM',y='MPG',data=dat_grp4)

plt.show()