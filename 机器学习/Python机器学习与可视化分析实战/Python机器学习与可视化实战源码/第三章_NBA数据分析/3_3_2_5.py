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

super_name_E = ['Kevin Durant','LeBron James','Kobe Bryant','Russell Westbrook','Stephen Curry','Carmelo Anthony']
super_name_C = [u'杜兰特',u'詹姆斯',u'科比',u'威少',u'库里',u'安东尼']
plt.figure(facecolor= 'bisque')
colors = ['red', 'yellow', 'peru', 'springgreen']
for i in range(len(super_name_E)):
    player_labels = [u'20分以下',u'20~29分',u'30~39分',u'40分以上']
    explode = [0,0.1,0,0] # 突出得分在20~29的比例
    player_score_range = []
    player_off_score_range = super_star_data[super_star_data.球员 == super_name_E [i]]
    player_score_range.append(len(player_off_score_range [player_off_score_range['得分'] < 20])*1.0/len(player_off_score_range ))
    player_score_range.append(len(pd.merge(player_off_score_range[19 < player_off_score_range.得分],
                                           player_off_score_range[player_off_score_range.得分 < 30],
                                       how='inner')) * 1.0 / len(player_off_score_range))
    player_score_range.append(len(pd.merge(player_off_score_range[29 < player_off_score_range.得分],
                                           player_off_score_range[player_off_score_range.得分 < 40],
                                       how='inner')) * 1.0 / len(player_off_score_range))
    player_score_range.append(len(player_off_score_range[39 < player_off_score_range.得分]) * 1.0 / len(player_off_score_range))
    plt.subplot(231 + i)
    plt.title(super_name_C [i] + u'得分分布', color='blue')
    plt.pie(player_score_range, labels=player_labels, colors=colors, labeldistance=1.1,
            autopct='%.01f%%', shadow=False, startangle=90, pctdistance=0.8, explode=explode)
    plt.axis('equal')
plt.show()


std = super_star_data.groupby('球员').std()['得分']
color = ['red','red','red','red','blue','red','red','red','red','red',]

plt.barh(range(10), std, align = 'center',color = color ,alpha = 0.8)
plt.xlabel(u'标准差',color = 'blue')
plt.ylabel(u'球员', color = 'blue')

plt.xlim(6,11)
for x,y in enumerate (std):
    plt.text(y + 0.1, x, '%s' % round(y,2), va = 'center')
plt.show()
