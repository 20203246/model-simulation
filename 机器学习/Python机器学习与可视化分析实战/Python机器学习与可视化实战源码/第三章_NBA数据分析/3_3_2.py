import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

#各个比赛数据
all_members = pd.read_csv('./NBA data/各个比赛数据.csv')
#print(all_members.head())

#print(all_members.info())
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

super_star_data = pd.concat([kd_data ,kb_data,jh_data,lj_data,sc_data,kl_data,cp_data,rw_data,pg_data,ca_data])
#print(super_star_data.info())

#参加的比赛信息
#print(super_star_data.球员.value_counts())
#print(super_star_data.groupby('球员').得分.describe())


super_off_mean_score = super_star_data.groupby('球员').mean()['得分']
labels = [u'场数',u'均分',u'标准差',u'最小值','25%','50%','75%',u'最大值']
super_name = [u'安东尼',u'保罗',u'哈登',u'伦纳德',u'杜兰特',u'科比',u'詹姆斯',u'乔治',u'威少',u'库里']
# 绘图
plt.bar(range(len(super_off_mean_score )),super_off_mean_score ,align = 'center')

plt.ylabel(u'得分')
plt.title(u'得分数据对比')
#plt.xticks(range(len(labels)),labels)
plt.xticks(range(len(super_off_mean_score )),super_name)
plt.ylim(15,35)
for x,y in enumerate (super_off_mean_score ):
    plt.text (x, y+1, '%s' % round(y, 2) , ha = 'center')
plt.show()

