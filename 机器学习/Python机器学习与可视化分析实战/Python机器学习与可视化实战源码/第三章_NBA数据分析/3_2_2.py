import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

data = pd.read_csv("./NBA data/球员薪资.csv")


# 使用jointplot查看年龄和薪水之间的关系
dat1=data.loc[:,['RPM','SALARY_MILLIONS','AGE','POINTS']]
sns.jointplot(dat1.SALARY_MILLIONS,dat1.AGE,kind='kde',size=8)
#plt.show()
#plot_kinds = ["scatter", "hist", "hex", "kde", "reg", "resid"]

multi_data = data.loc[:, ['RPM','SALARY_MILLIONS','AGE','POINTS']]
sns.pairplot(multi_data)
plt.show()

