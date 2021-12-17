################################################################################
# 导入给定期权和期货的每日行情，并生成隐含波动率数据
# 使用美式二叉树定价模型以及相应的隐波计算方法
# 
# 注意：
# 本代码是周宏成为了给东北财经大学的研究生上课时准备的案例，
# 请不要用作它途
###############################################################################

#%%
import math
import pandas as pd
import numpy  as np

import BinomialOptionModel as op
import DateUtil as du



# 1. 从文件中读取数据
tradeDate = '20200316'

ROOT_PATH = "E:\\PythonShares\\Y2021\\Examples\\the_18th_lesson[期权波动率曲面构建和不活跃期权合约的价格预测]\\"
futPath = ROOT_PATH + "DATA\\m_fut.csv"
optPath = ROOT_PATH + "DATA\\m_opt.csv"


# 成交量大于0,价格大于0.5的才保留
dfFutAll = pd.read_csv(futPath,header=0,parse_dates=["交易日"])
futCriteria = (dfFutAll["交易日"] == tradeDate) & (dfFutAll["成交量"] > 0 )
dfFut = dfFutAll.loc[futCriteria,["交易日","交割月","收盘价","成交量"]]

dfOptAll = pd.read_csv(optPath,header=0,parse_dates=["交易日"])
optCriteria = (dfOptAll["交易日"]== tradeDate) & (dfOptAll["成交量"] > 0 ) & (dfOptAll["收盘价"] > 0.5 )
dfOpt = dfOptAll.loc[optCriteria,["交易日","交割月","收盘价","成交量"]]


# 2. 准备构建隐含波动率曲面的各种数据
# 创建空的dataFrame
dfIV = pd.DataFrame(columns=["OPT_CONTRACT_ID","OPTION_TYPE","STRIKE_PRICE","OPTION_PRICE","FUTURE_PRICE","LG_MM","T","IV","TOT_QTY"])

# 循环处理每条期权数据，并填充上表
for row_index,row in dfOpt.iterrows():
    tradeDate = row["交易日"]
    contractId = row["交割月"]
    closePrice = row["收盘价"]
    tot_qty = row["成交量"]

    # 分解合约号为期货交割月、期权类型和执行价格
    deliveryMonth = contractId[1:5]  # 字符串类型
    optionType = contractId[6:7]
    strikePrice = np.int64(contractId[8:])

    # 根据deliveryMonth获得对应的期货合约
    dfUnderlying = dfFut.loc[dfFut["交割月"] == np.int64(deliveryMonth)]
    underlyingPrice = dfUnderlying.iloc[0,2]  #标的期货合约的价格


    # 计算当前交易日距离到期的日期差
    optLastTradeDate = du.getOptLastTradeDate( deliveryMonth )
    diffDays = (optLastTradeDate - tradeDate).days + 1

    # 计算期权的隐含波动率
    S0 = underlyingPrice
    K = strikePrice
    T = diffDays/365  # 年化的到期时间
    r = 0.03
    optionPrice = closePrice
    if ( optionType == 'C'):
        otype = 'call'
    else :
        otype = 'put'
    iv = op.getImpliedVolatility(S0, K, T, r,optionPrice,otype)
    #print(tradeDate,contractId,closePrice,iv )

    # 将生成的隐含波动率数据写入到dfIV中
    row = { }
    row["OPT_CONTRACT_ID"] = contractId
    row["OPTION_TYPE"] = optionType
    row["STRIKE_PRICE"] = strikePrice
    row["OPTION_PRICE"] = optionPrice
    row["FUTURE_PRICE"] = underlyingPrice
    row["T"] = T
    row["LG_MM"] = math.log(strikePrice/underlyingPrice)
    row["IV"] = iv
    row["TOT_QTY"] = tot_qty
    row["DELIVERY_MONTH"] = deliveryMonth
    
    dfIV = dfIV.append(row, ignore_index=True)

outPath= ROOT_PATH + "data\\soybean_opt_iv1.csv"
dfIV.to_csv( outPath )
print( " OVER !")

#%%
