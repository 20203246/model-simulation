import pandas as pd

def error_processing(df):
    '''
    异常值处理，可根据建模效果，反复调节处理方案，建议谨慎删除数据。
    df：数据源
    '''

    def show_error(df, col, whis=1.5, show=False):
        '''
        显示上下限异常值数量，可选显示示例异常数据
        df：数据源
        col：字段名
        whis：默认1.5，对应1.5倍iqr
        show：是否显示示例异常数据
        '''
        iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
        upper_bound = df[col].quantile(0.75) + whis * iqr  # 上界
        lower_bound = df[col].quantile(0.25) - whis * iqr  # 下界
        # print(iqr,upper_bound,lower_bound)
        print('【', col, '】上界异常值总数：', df[col][df[col] > upper_bound].count())
        if show:
            print('异常值示例：\n', df[df[col] > upper_bound].head(5).T)
        print('【', col, '】下界异常值总数：', df[col][df[col] < lower_bound].count())
        if show:
            print('异常值示例：\n', df[df[col] < lower_bound].head(5).T)
        print('- - - - - - ')

    def drop_error(df, col):
        '''
        删除上下限异常值数量
        df：数据源
        col：字段名
        '''
        iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
        upper_bound = df[col].quantile(0.75) + 1.5 * iqr  # 上界
        lower_bound = df[col].quantile(0.25) - 1.5 * iqr  # 下界
        data_del = df[col][(df[col] > upper_bound) | (df[col] < lower_bound)].count()
        data = df[(df[col] <= upper_bound) & (df[col] >= lower_bound)]
        # print('总剔除数据量：',data_del)
        return data

    # 计数器
    n = len(df)

    # 可用信贷额度
    # 从分布直方图可知，比例大于1的应该为错误值。
    # 错误值共3321，若剔除可能影响建模效果。剔除>=20000的数据
    show_error(df, '可用信贷额度比例')
    df = df[df.可用信贷额度比例 <= 20000]

    # 年龄
    # 异常值数量不多，剔除年龄大于100小于18的异常数据
    show_error(df, '年龄')
    df = df[(df['年龄'] > 18) & (df['年龄'] < 100)]

    # 逾期30-59天的笔数
    # 根据箱型图去除>80的异常数据
    show_error(df, '逾期30-59天的笔数')
    df = df[df['逾期30-59天的笔数'] < 80]

    # 逾期90天+的笔数
    # 根据箱型图去除>80的异常数据
    show_error(df, '逾期90天+的笔数')
    df = df[df['逾期90天+的笔数'] < 80]

    # 逾期60-89天的笔数
    # 根据箱型图去除>80的异常数据
    show_error(df, '逾期60-89天的笔数')
    df = df[df['逾期60-89天的笔数'] < 80]

    # 负债率
    # 根据箱型图去除>100000的异常数据
    show_error(df, '负债率')
    df = df[df['负债率'] < 100000]

    # 月收入
    # 根据箱型图去除>500000的异常数据
    show_error(df, '月收入')
    df = df[(df['月收入'] < 500000) | df.月收入.isna()]

    # 固定资产贷款数
    # 根据箱型图去除>20的异常数据
    show_error(df, '固定资产贷款数')
    df = df[df['固定资产贷款数'] < 20]

    # 家属数量
    # 根据箱型图去除>10的异常数据
    show_error(df, '家属数量')
    df = df[(df['家属数量'] < 12) | df.家属数量.isna()]

    # 信贷数量 - 保留异常值
    return df
    print('共删除数据 ', n - len(df), ' 条。')

def collineation_processing(df,col,col1,col2,name):
    '''
    去除共线性，保留一个字段，其他字段求比值
    df：数据源
    col：保留字段
    col1，col2：求比值字段
    name：新比值字段名称
    '''
    def trans2percent(row):
        if row[col2] == 0:
            return 0
        else:
            return row[col1] / row[col2]
    df[name] = df.apply(trans2percent,axis=1)
    return df

def missing_values_processing(df, func1=1, func2=1):
    '''
    缺失值处理
    df：数据源
    func1：默认为1，众数填充家属；0，去除带空值数据行。
    func2：默认为1，众数填充月收入；0，平均数填充月收入。
    '''
    # 家属数量 - 剔除或众数填充
    if func1 == 1:
        df.loc[df.家属数量.isna(), '家属数量'] = df.家属数量.mode()[0]
    elif func1 == 0:
        df = df.dropna(subset=['家属数量'])
    else:
        print('parameter wrong!')

    # 月收入 - 剔除或均值填充
    if func1 == 1:
        df.loc[df.月收入.isna(), '月收入'] = df.月收入.mode()[0]
    elif func1 == 0:
        df.loc[df.月收入.isna(), '月收入'] = df.月收入.mean()[0]
    else:
        print('parameter wrong!')
    return df


def resample(df):
    '''
    使样本'未来两年可能违约'标签的0，1项可以各占一半，以提高预测效果。sample()可以考虑添加random_state以便生成相同样本集
    df：数据源
    '''
    num = df['未来两年可能违约'].value_counts()[1]
    df_t = df[df.未来两年可能违约==1]
    df_f = df[df.未来两年可能违约==0].sample(frac=1)[0:num]
    df_balanced = pd.concat([df_t,df_f]).sample(frac=1).reset_index(drop=True)
#     print(df_balanced.未来两年可能违约.value_counts())
    return df_balanced



from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score,accuracy_score, \
                            precision_score,recall_score, roc_auc_score
# 分类模型性能查看函数
def perfomance_clf(model,X,y,name=None):
    y_predict = model.predict(X)
    if name:
        print(name,':')
    print(f'accuracy score is: {accuracy_score(y,y_predict)}')
    print(f'precision score is: {precision_score(y,y_predict)}')
    print(f'recall score is: {recall_score(y,y_predict)}')
    print(f'auc: {roc_auc_score(y,y_predict)}')
    print('--------------')