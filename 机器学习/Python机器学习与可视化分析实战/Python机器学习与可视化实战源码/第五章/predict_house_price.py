import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

train = pd.read_csv("./train.csv")

# sns.set_style("white")
# sns.set_color_codes(palette='deep')
# f, ax = plt.subplots(figsize=(8, 7))
# #Check the new distribution
# sns.distplot(train['SalePrice'], color="b");
# ax.xaxis.grid(False)
# ax.set(ylabel="Frequency")
# ax.set(xlabel="SalePrice")
# ax.set(title="SalePrice distribution")
# sns.despine(trim=True, left=True)
# plt.show()

# corr = train.corr()
# plt.subplots(figsize=(15,12))
# sns.heatmap(corr, vmax=0.9, cmap="Blues", square=True)
# plt.show()


# data = pd.concat([train['SalePrice'], train['OverallQual']], axis=1)
# f, ax = plt.subplots(figsize=(8, 6))
# fig = sns.boxplot(x=train['OverallQual'], y="SalePrice", data=data)
# fig.axis(ymin=0, ymax=800000);
#
# data = pd.concat([train['SalePrice'], train['YearBuilt']], axis=1)
# f, ax = plt.subplots(figsize=(16, 8))
# fig = sns.boxplot(x=train['YearBuilt'], y="SalePrice", data=data)
# fig.axis(ymin=0, ymax=800000);
# plt.xticks(rotation=45);
#
# data = pd.concat([train['SalePrice'], train['TotalBsmtSF']], axis=1)
# data.plot.scatter(x='TotalBsmtSF', y='SalePrice', alpha=0.3, ylim=(0,800000));
#
#
# data = pd.concat([train['SalePrice'], train['LotArea']], axis=1)
# data.plot.scatter(x='LotArea', y='SalePrice', alpha=0.3, ylim=(0,800000));
#
# data = pd.concat([train['SalePrice'], train['GrLivArea']], axis=1)
# data.plot.scatter(x='GrLivArea', y='SalePrice', alpha=0.3, ylim=(0,800000));
#
# plt.show()

train["SalePrice"] = np.log1p(train["SalePrice"])
# sns.set_style("white")
# sns.set_color_codes(palette='deep')
# f, ax = plt.subplots(figsize=(8, 7))
# #Check the new distribution
# sns.distplot(train['SalePrice'] , color="b");
#
# ax.xaxis.grid(False)
# ax.set(ylabel="Frequency")
# ax.set(xlabel="SalePrice")
# ax.set(title="SalePrice distribution")
# sns.despine(trim=True, left=True)
#
# plt.show()

# determine the threshold for missing values

# Split features and labels
train_labels = train['SalePrice'].reset_index(drop=True)
train_features = train.drop(['SalePrice'], axis=1)


def percent_missing(df):
    data = pd.DataFrame(df)
    df_cols = list(pd.DataFrame(data))
    dict_x = {}
    for i in range(0, len(df_cols)):
        dict_x.update({df_cols[i]: round(data[df_cols[i]].isnull().mean() * 100, 2)})

    return dict_x

missing = percent_missing(train_features)
df_miss = sorted(missing.items(), key=lambda x: x[1], reverse=True)

train_features['BsmtFinType1_Unf'] = 1*(train_features['BsmtFinType1'] == 'Unf')
train_features['HasWoodDeck'] = (train_features['WoodDeckSF'] == 0) * 1
train_features['HasOpenPorch'] = (train_features['OpenPorchSF'] == 0) * 1
train_features['HasEnclosedPorch'] = (train_features['EnclosedPorch'] == 0) * 1
train_features['Has3SsnPorch'] = (train_features['3SsnPorch'] == 0) * 1
train_features['HasScreenPorch'] = (train_features['ScreenPorch'] == 0) * 1
train_features['YearsSinceRemodel'] = train_features['YrSold'].astype(int) - train_features['YearRemodAdd'].astype(int)
train_features['Total_Home_Quality'] = train_features['OverallQual'] + train_features['OverallCond']
train_features = train_features.drop(['Utilities', 'Street', 'PoolQC',], axis=1)
train_features['TotalSF'] = train_features['TotalBsmtSF'] + train_features['1stFlrSF'] + train_features['2ndFlrSF']
train_features['YrBltAndRemod'] = train_features['YearBuilt'] + train_features['YearRemodAdd']

train_features['Total_sqr_footage'] = (train_features['BsmtFinSF1'] + train_features['BsmtFinSF2'] +
                                 train_features['1stFlrSF'] + train_features['2ndFlrSF'])
train_features['Total_Bathrooms'] = (train_features['FullBath'] + (0.5 * train_features['HalfBath']) +
                               train_features['BsmtFullBath'] + (0.5 * train_features['BsmtHalfBath']))
train_features['Total_porch_sf'] = (train_features['OpenPorchSF'] + train_features['3SsnPorch'] +
                              train_features['EnclosedPorch'] + train_features['ScreenPorch'] +
                              train_features['WoodDeckSF'])
train_features['TotalBsmtSF'] = train_features['TotalBsmtSF'].apply(lambda x: np.exp(6) if x <= 0.0 else x)
train_features['2ndFlrSF'] = train_features['2ndFlrSF'].apply(lambda x: np.exp(6.5) if x <= 0.0 else x)
train_features['GarageArea'] = train_features['GarageArea'].apply(lambda x: np.exp(6) if x <= 0.0 else x)
train_features['GarageCars'] = train_features['GarageCars'].apply(lambda x: 0 if x <= 0.0 else x)
train_features['LotFrontage'] = train_features['LotFrontage'].apply(lambda x: np.exp(4.2) if x <= 0.0 else x)
train_features['MasVnrArea'] = train_features['MasVnrArea'].apply(lambda x: np.exp(4) if x <= 0.0 else x)
train_features['BsmtFinSF1'] = train_features['BsmtFinSF1'].apply(lambda x: np.exp(6.5) if x <= 0.0 else x)

train_features['haspool'] = train_features['PoolArea'].apply(lambda x: 1 if x > 0 else 0)
train_features['has2ndfloor'] = train_features['2ndFlrSF'].apply(lambda x: 1 if x > 0 else 0)
train_features['hasgarage'] = train_features['GarageArea'].apply(lambda x: 1 if x > 0 else 0)
train_features['hasbsmt'] = train_features['TotalBsmtSF'].apply(lambda x: 1 if x > 0 else 0)
train_features['hasfireplace'] = train_features['Fireplaces'].apply(lambda x: 1 if x > 0 else 0)

def logs(res, ls):
    m = res.shape[1]
    for l in ls:
        res = res.assign(newcol=pd.Series(np.log(1.01+res[l])).values)
        res.columns.values[m] = l + '_log'
        m += 1
    return res

log_features = ['LotFrontage','LotArea','MasVnrArea','BsmtFinSF1','BsmtFinSF2','BsmtUnfSF',
                 'TotalBsmtSF','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea',
                 'BsmtFullBath','BsmtHalfBath','FullBath','HalfBath','BedroomAbvGr','KitchenAbvGr',
                 'TotRmsAbvGrd','Fireplaces','GarageCars','GarageArea','WoodDeckSF','OpenPorchSF',
                 'EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal','YearRemodAdd','TotalSF']

all_features = logs(train_features, log_features)



def squares(res, ls):
    m = res.shape[1]
    for l in ls:
        res = res.assign(newcol=pd.Series(res[l]*res[l]).values)
        res.columns.values[m] = l + '_sq'
        m += 1
    return res

squared_features = ['YearRemodAdd', 'LotFrontage_log',
              'TotalBsmtSF_log', '1stFlrSF_log', '2ndFlrSF_log', 'GrLivArea_log',
              'GarageCars_log', 'GarageArea_log']
all_features = squares(all_features, squared_features)

all_features = pd.get_dummies(all_features).reset_index(drop=True)
all_features = all_features.dropna()


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


train_labels = all_features.iloc[:,-1].reset_index(drop=True)
X = all_features.iloc[:len(train_labels), :]
x = X.values
y = train_labels.values

lr = LinearRegression()
# 拟合训练数据
lr.fit(x,y)