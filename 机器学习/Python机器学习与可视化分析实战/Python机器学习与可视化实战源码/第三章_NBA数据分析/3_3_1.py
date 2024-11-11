import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

#常规赛数据
team_season = pd.read_csv('./NBA data/team_season.csv')
#季后赛数据
team_playoff = pd.read_csv('./NBA data/team_playoff.csv')

def handle_score(score:str):
    score_list = score.split("-")
    score = int(score_list[0][3:]) - int(score_list[1][:(len(score_list[1]) - 3)])
    return score
team_season["分差"] = team_season["比分"].map(handle_score)

def handle_season(season:str):
    season_list = season.split("/")

    return int(season_list[0])

team_season["赛季"] = team_season["时间"].map(handle_season)
team_season = team_season.loc[team_season["球队"] == "BOS"]
#print(team_season.head())

# 常规赛分析
temp = team_season[['得分','赛季','分差','篮板','犯规','罚球','罚球命中','罚球出手','失误','助攻','投篮']].groupby('赛季')
plt.figure(figsize=(14,4))
plt.subplot(121)
plt.title('各个赛季得分: 极值与均值')
plt.plot(temp['得分'].min(),'g.',alpha=0.7)
plt.plot(temp['得分'].max(),'g.',alpha=0.7)
plt.plot(temp['得分'].mean(),'bo',temp.mean()['得分'],'k',alpha=0.8)
plt.subplot(122)
plt.title('各个赛季得分标准差与场均分差')
plt.plot(temp['得分'].std(),'go',temp['得分'].std(),'k',alpha=0.8)
plt.plot(temp['分差'].mean(),'ro',temp['分差'].mean(),'k',alpha=0.8)
plt.legend()

plt.figure(figsize=(14,4))
plt.subplot(131)
plt.plot(temp.min()['篮板'],'g.',alpha=0.7)
plt.plot(temp.max()['篮板'],'g.',alpha=0.7)
plt.plot(temp.mean()['篮板'],'o',temp.mean()['篮板'],'k',alpha=0.8)

plt.subplot(231)
plt.plot(temp['失误'].mean(),'ko',temp['失误'].mean(),'grey',alpha=0.8, label=u'失误');plt.legend()
plt.subplot(234)
plt.plot(temp['助攻'].mean(),'yo',temp['助攻'].mean(),'c',alpha=0.8, label=u'助攻');plt.legend()
plt.subplot(232)
plt.plot(temp['犯规'].mean(),'co',temp['犯规'].mean(),'k',alpha=0.8, label=u'犯规');plt.legend()
plt.subplot(235)
plt.plot(temp['罚球'].mean(), 'o',temp['罚球'].mean(),'grey',alpha=0.8, label=u'罚球');plt.legend()
plt.subplot(233)
plt.plot(temp['投篮'].mean(),'ro',temp['投篮'].mean(),'k',alpha=0.8, label=u'投篮');plt.legend()
plt.subplot(236)
plt.plot(temp['篮板'].mean(),'ko',temp['篮板'].mean(),'orange',alpha=0.8, label=u'篮板');plt.legend()
plt.show()


