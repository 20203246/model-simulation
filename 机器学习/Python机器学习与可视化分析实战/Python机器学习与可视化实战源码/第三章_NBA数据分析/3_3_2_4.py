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

season_kd_score = super_star_data[super_star_data.球员 == 'Kevin Durant'].groupby('赛季').mean()['得分']
plt.figure(figsize=(16, 9))
plt.subplots_adjust(hspace=0.8)
#plt.subplot(321)
plt.subplot(611)
plt.title(u'杜兰特赛季平均得分', color='red')
# plt.xlabel(u'赛季')
plt.ylabel(u'得分')
plt.plot(season_kd_score, 'k', season_kd_score, 'bo')
for x, y in enumerate(season_kd_score):
    plt.text(x, y + 0.2, '%s' % round(y, 2), ha='center')

season_lj_score = super_star_data[super_star_data.球员 == 'LeBron James'].groupby('赛季').mean()['得分']
#plt.subplot(322)
plt.subplot(612)
plt.title(u'詹姆斯赛季平均得分', color='red')
# plt.xlabel(u'赛季')
plt.ylabel(u'得分')
plt.plot(season_lj_score, 'k', season_lj_score, 'bo')
for x, y in enumerate(season_lj_score):
    plt.text(x, y + 0.2, '%s' % round(y, 2), ha='center')

season_kb_score = super_star_data[super_star_data.球员 == 'Kobe Bryant'].groupby('赛季').mean()['得分']
a = season_kb_score[0:-4]
b = season_kb_score[-4:]
season_kb_score = pd.concat([b, a])
#plt.subplot(323)
plt.subplot(613)

plt.title(u'科比赛季平均得分', color='red')
# plt.xlabel(u'赛季')
plt.ylabel(u'得分')
plt.xticks(range(len(season_kb_score)), season_kb_score.index)
plt.plot(list(season_kb_score), 'k', list(season_kb_score), 'bo')
for x, y in enumerate(season_kb_score):
    plt.text(x, y + 0.2, '%s' % round(y, 2), ha='center')

season_rw_score = super_star_data[super_star_data.球员 == 'Russell Westbrook'].groupby('赛季').mean()[
    '得分']
#plt.subplot(324)
plt.subplot(614)
plt.title(u'威少赛季平均得分', color='red')
# plt.xlabel(u'赛季')
plt.ylabel(u'得分')
plt.plot(season_rw_score, 'k', season_rw_score, 'bo')
for x, y in enumerate(season_rw_score):
    plt.text(x, y + 0.2, '%s' % round(y, 2), ha='center')

season_sc_score = super_star_data[super_star_data.球员 == 'Stephen Curry'].groupby('赛季').mean()['得分']
#plt.subplot(325)
plt.subplot(615)
plt.title(u'库里赛季平均得分', color='red')
# plt.xlabel(u'赛季')
plt.ylabel(u'得分')
plt.plot(season_sc_score, 'k', season_sc_score, 'bo')
for x, y in enumerate(season_sc_score):
    plt.text(x, y + 0.2, '%s' % round(y, 2), ha='center')

season_ca_score = super_star_data[super_star_data.球员 == 'Carmelo Anthony'].groupby('赛季').mean()['得分']
#plt.subplot(326)
plt.subplot(616)
plt.title(u'安东尼赛季平均得分', color='red')
# plt.xlabel(u'赛季')
plt.ylabel(u'得分')
plt.plot(season_ca_score, 'k', season_ca_score, 'bo')
for x, y in enumerate(season_ca_score):
    plt.text(x, y + 0.2, '%s' % round(y, 2), ha='center')

plt.show()
