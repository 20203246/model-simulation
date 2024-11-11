import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# 各个比赛数据
all_members = pd.read_csv('./NBA data/球员高阶数据.csv')
# print(all_members.head())

# print(all_members.info())
kd_data = all_members[all_members.球员 == 'Kevin Durant']
jh_data = all_members[all_members.球员 == 'James Harden']
kb_data = all_members[all_members.球员 == 'Kobe Bryant']
lj_data = all_members[all_members.球员 == 'LeBron James']
kl_data = all_members[all_members.球员 == 'Kawhi Leonard']
sc_data = all_members[all_members.球员 == 'Stephen Curry']
rw_data = all_members[all_members.球员 == 'Russell Westbrook']
pg_data = all_members[all_members.球员 == 'Paul George']
ca_data = all_members[all_members.球员 == 'Carmelo Anthony']
cp_data = all_members[all_members.球员 == 'Chris Paul']

super_star_data = pd.concat([kd_data, kb_data, jh_data, lj_data, sc_data, kl_data, cp_data, rw_data, pg_data, ca_data])
super_name = [u'安东尼',u'保罗',u'哈登',u'伦纳德',u'杜兰特',u'科比',u'詹姆斯',u'乔治',u'威少',u'库里']

import seaborn as sns


player_labels = [ u'篮板率', u'助攻率', u'抢断率', u'盖帽率',u'失误率', u'使用率', u'胜利贡献值',  u'霍格林效率值']
player_data = super_star_data[['球员','篮板率','助攻率','抢断率','盖帽率','失误率',
                             '使用率','ws','per']] .groupby('球员').mean()
num = [100,100,100,100,100,100,1,1]
np_num = np.array(player_data)*np.array(num)
plt.title(u'球员攻防两端的能力热力图')
sns.heatmap(np_num , annot=True,xticklabels= player_labels ,yticklabels=super_name  ,cmap='YlGnBu')
plt.show()


