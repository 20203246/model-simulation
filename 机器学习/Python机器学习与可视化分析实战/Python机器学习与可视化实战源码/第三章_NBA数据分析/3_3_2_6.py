import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# 各个比赛数据
all_members = pd.read_csv('./NBA data/各个比赛数据.csv')
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
super_name_E = [u'Carmelo Anthony', u'Chris Paul', u'James Harden', u'Kawhi Leonard', u'Kevin Durant', u'Kobe Bryant',
                u'LeBron James', u'Paul George', u'Russell Westbrook', u'Stephen Curry']
bar_width = 0.25
import numpy as np
shoot = super_star_data.groupby('球员') .mean()['投篮']
three_pts = super_star_data.groupby('球员') .mean()['三分']
free_throw = super_star_data.groupby('球员') .mean()['罚球']
plt.bar(np.arange(10),shoot,align = 'center',label = u'投篮命中率',color = 'red',width = bar_width )
plt.bar(np.arange(10)+ bar_width, three_pts ,align = 'center',color = 'blue',label = u'三分命中率',width = bar_width )
plt.bar(np.arange(10)+ 2*bar_width, free_throw  ,align = 'center',color = 'green',label = u'罚球命中率',width = bar_width )
for x,y in enumerate (shoot):
    plt.text(x, y+0.01, '%s' % round(y,2), ha = 'center')
for x,y in enumerate (three_pts ):
    plt.text(x+bar_width , y+0.01, '%s' % round(y,2), ha = 'center')
for x,y in enumerate (free_throw):
    plt.text(x+2*bar_width , y+0.01, '%s' % round(y,2), ha = 'center')
plt.legend ()
plt.ylim(0.3,1.0)
plt.title(u'球员的命中率的对比')
plt.xlabel(u'球员')
plt.xticks(np.arange(10)+bar_width  ,super_name)
plt.ylabel(u'命中率')
plt.show()
