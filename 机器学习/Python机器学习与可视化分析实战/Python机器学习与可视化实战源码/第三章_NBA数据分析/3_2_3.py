import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

data = pd.read_csv("./NBA data/球员薪资.csv")

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

# 球员薪水与效率值   按年龄段来看
sns.set_style('darkgrid')  # 设置seaborn的面板风格
plt.figure(figsize=(8, 8), dpi=100)
plt.title('RPM and SALARY', size=15)

X1 = data.loc[data.age_cut == 'old'].SALARY_MILLIONS
Y1 = data.loc[data.age_cut == 'old'].RPM
plt.plot(X1, Y1, '.')

X2 = data.loc[data.age_cut == 'best'].SALARY_MILLIONS
Y2 = data.loc[data.age_cut == 'best'].RPM
plt.plot(X2, Y2, '^')

X3 = data.loc[data.age_cut == 'young'].SALARY_MILLIONS
Y3 = data.loc[data.age_cut == 'young'].RPM
plt.plot(X3, Y3, '.')

plt.xlim(0, 30)
plt.ylim(-8, 8)
plt.xlabel('Salary')
plt.ylabel('RPM')
plt.xticks(np.arange(0, 30, 3))
# 绘制图例
plt.legend(['old', 'best', 'young'])
# 显示图像
plt.show()







