import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)

data = pd.read_csv("./NBA data/球员薪资.csv")

# 利用seaborn中的displot绘图来分别看一下球员的薪水、效率值、年龄这三个信息的分布情况

# 分布及核密度展示
sns.set_style('darkgrid')  # 设置seaborn的面板风格

# 获取画布
plt.figure(figsize=(10, 10))

# 拆分页面，多图展示
plt.subplot(3, 1, 1)
# 绘制直方图图像
sns.distplot(data['SALARY_MILLIONS'])
# 把0--40之间,分成9个间隔(包含0和40)
plt.xticks(np.linspace(0, 40, 9))
# y轴标签
plt.ylabel('Salary', size=10)  # size：设置字体大小

# 拆分画布
plt.subplot(3, 1, 2)
# 绘制直方图图像
sns.distplot(data['RPM'])
plt.xticks(np.linspace(-10, 10, 9))
# y轴标签
plt.ylabel('RPM', size=10)

# 拆分画布
plt.subplot(3, 1, 3)
# 绘制直方图图像
sns.distplot(data['AGE'])
plt.xticks(np.linspace(20, 40, 11))
# y轴标签
plt.ylabel('AGE', size=10)

plt.show()


