#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:36:07 2021

@author: cuiying
"""

import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import BinomialOptionModel as op
from patsy import dmatrices

from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('seaborn')
mpl.rcParams['font.family']='serif'

##%%
def getMaxIncrementlist(arr):
    
    #求最长单调递增子序列
    #输入参数：列表
    #输出参数：列表
    result=[]
    n=len(arr)
    m=[0]*n
    for x in range(n-2,-1,-1):
        for y in range(n-1,x,-1):
            if arr[x]<arr[y] and m[x]<=m[y]:
                m[x]+=1
        max_value=max(m)
        #result=[]
        for i in range(n):
            if m[i]==max_value:
                result.append(arr[i])
                max_value-=1
    return result

##%%
#从文件中读取数据
ROOT_PATH = "C:\\Users\\kingb\\Desktop\\asdsadsa\\"
iv_file_path=ROOT_PATH+"data//soybean_opt_iv.csv"
IvData=pd.read_csv(iv_file_path,sep=',',header=0)

##%%

deliveryMonths=IvData['DELIVERY_MONTH'].to_numpy()
deliveryMonths=np.unique(deliveryMonths)

##%%

#计算系列的总成交量，并展示出来，从中可以推测出哪些月份的流动性比较低
#流动性比较低的月份波动率的可靠性也相对较低
SeriesTotQty=pd.DataFrame(columns=["DELIVERY_MONTH","SUM_TOT_QTY"])
for seriesID in deliveryMonths.tolist():
    criteria=(IvData['DELIVERY_MONTH']==seriesID)
    series_IvData=IvData.loc[criteria,:]
    series_tot_qty=np.sum(series_IvData['TOT_QTY'])
    print(seriesID,series_tot_qty)
    
##%%

#将无效数据从文件中去掉，将可靠数据保留在IvData_chosed
firstT=True
for iT in deliveryMonths.tolist():
   
    #取虚值
    out_call=(IvData['OPTION_TYPE']=='C')&(IvData['STRIKE_PRICE']>IvData['FUTURE_PRICE'])
    out_call_IvData=IvData[(IvData['DELIVERY_MONTH']==iT)&(out_call)]
   
    #看涨取最长单调递减子序列
    out_call_prices=(out_call_IvData['OPTION_PRICE']*(-1)).tolist()
    max_increment_list=getMaxIncrementlist(out_call_prices)
    max_decrement_list=list(map(lambda x:x*(-1),max_increment_list))
    cond1=out_call_IvData['OPTION_PRICE'].isin(max_decrement_list)
    filtered_out_call_IvData=out_call_IvData.loc[cond1,:]
    
    #取虚值
    out_put=(IvData['OPTION_TYPE']=='p')&(IvData['STRIKE_PRICE']<IvData['FUTURE_PRICE'])
    out_put_IvData=IvData[(IvData['DELIVERY_MONTH']==iT)&(out_put)]
    
    
    #看跌期权取最长单调递增子序列
    out_put_prices=(out_put_IvData['OPTION_PRICE']).tolist()
    max_increment_list=getMaxIncrementlist(out_put_prices)
    cond2=out_put_IvData['OPTION_PRICE'].isin(max_increment_list)
    filtered_out_put_IvData=out_put_IvData.loc[cond2,:]
    
    
    #将过滤完毕的数据合并成样本数据
    filtered_IvData=filtered_out_call_IvData.append(filtered_out_put_IvData)
    if(firstT==True):
        IvData_chosed=filtered_IvData
        firstT=False
    else:
        IvData_chosed=IvData_chosed.append(filtered_IvData)
        
    
    
#%%
#在同一个平面上画图展示各个月份的波动率，从中大致看看分布规律
plt.figure()
style_list=['ro:','gx:','bv:','yD:','mh:','c*:','k.:']
i=0
for iT in deliveryMonths.tolist():
    sample_IvData=IvData_chosed[(IvData_chosed['DELIVERY_MONTH']==iT)]
    sample_IvData=sample_IvData.sort_values(by=['STRIKE_PRICE'])
    sample_strike_price=sample_IvData['STRIKE_PRICE'].to_numpy()
    sample_IV=sample_IvData['IV'].to_numpy()
    style_i=style_list[i]
    plt.plot(sample_strike_price, sample_IV,style_i,label=iT)
    i=i+1

# plt.grid(True)
# plt.xlabel('Strike')
# plt.ylabel('Implied Volatility')
# plt.legend()
# plt.show()

#%%

#
#采用经典的多变量回归模型完成曲面的回归分析工作
#iv=a*m*m+b*t*m+c*m+d*t+e
#这个部分是重点
#
#2.构建三维模型回归函数拟合分析

iv=IvData_chosed['IV']
m=IvData_chosed['LG_MM']
t=IvData_chosed['T']


size=len(iv)
X=np.zeros((size,5))
X[:,4]=m**2
X[:,3]=t*m
X[:,2]=m
X[:,1]=t
X[:,0]=1
model=sm.OLS(iv,X).fit()
params=model.params

#通过分析模型的残差来验证模型的合理性
print(model.params)
print(model.summary())
print(model.rsquared)
w=sm.stats.linear_rainbow(model)

def reg_func(params,m,t):
    f4=params[4]*m**2
    f3=params[3]*t*m
    f2=params[2]*m
    f1=params[1]*t
    f0=params[0]*1
    return(f4+f3+f2+f1+f0)

RIV=reg_func(params, m, t)



##%%

#
#根据生成的数据画出平面图
#
#%%
#在同一个平面上画图展示各个月份的波动率，从中大致看看分布规律
plt.figure()
style_list=['ro:','gx:','bv:','yD：','mh:','c*:','k.:']
i=0
# plt.figure()
# style_list=['ro:','gx:','bv:','yD:','mh:','c*:','k.:']
# i=0
# for iT in deliveryMonths.tolist():
#     sample_IvData=IvData_chosed[(IvData_chosed['DELIVERY_MONTH']==iT)]
#     sample_IvData=sample_IvData.sort_values(by=['STRIKE_PRICE'])
#     sample_strike_price=sample_IvData['STRIKE_PRICE'].to_numpy()
#     sample_IV=sample_IvData['IV'].to_numpy()
#     style_i=style_list[i]
#     plt.plot(sample_strike_price, sample_IV,style_i,label=iT)
#     i=i+1
#
#     criteria = (IvData['DELIVERY_MONTH'] == seriesID)
#     series_IvData = IvData.loc[criteria, :]
#     series_tot_qty = np.sum(series_IvData['TOT_QTY'])
for iT in deliveryMonths.tolist():
    sample_IvData=IvData_chosed[(IvData_chosed['DELIVERY_MONTH']==iT)]
    sample_IvData=sample_IvData.sort_values(by=['STRIKE_PRICE'])
    sample_strike_price=sample_IvData['STRIKE_PRICE'].to_numpy()
    sample_m=sample_IvData['LG_MM'].to_numpy()
    sample_t=sample_IvData['T'].to_numpy()
    sample_IV=reg_func(params,sample_m,sample_t)
    style_i=style_list[i]
    plt.plot(sample_strike_price, sample_IV,style_i,label=iT)
    # print(sample_strike_price, sample_IV, style_i, iT)
    i=i+1
  
plt.grid(True)
plt.xlabel('m')
plt.ylabel('Implied_Volatility')
plt.legend()
plt.show()

#%%
#
#根据生成的数据画出曲面图
#
#准备曲面数据
mseq=np.linspace(np.min(m),np.max(m),1000,endpoint=False)
tseq=np.linspace(np.min(t),np.max(t),1000,endpoint=False)
grid_m,grid_t=np.meshgrid(mseq,tseq)
points=np.asarray(list(zip(m,t)))
grid_iv=griddata(points,RIV,(grid_m,grid_t),method='cubic')


#绘制曲面
fig=plt.figure()
ax=Axes3D(fig)
surf=ax.plot_surface(grid_m,grid_t,grid_iv)
ax.set_xlabel("LG_MM")
ax.set_ylabel("T")
ax.set_zlabel("IV")
fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()

#%%


#
#从原始行情数据中任取某个月份的流动性低的月份的所有数据，生成新的理论价格
#
iT=2011
sample_IvData=IvData_chosed[(IvData_chosed['DELIVERY_MONTH']==iT)]
sample_IvData=sample_IvData.sort_values(by=['STRIKE_PRICE'])
sample_S=sample_IvData['FUTURE_PRICE'].to_numpy()
sample_K=sample_IvData['STRIKE_PRICE'].to_numpy()
sample_T=sample_IvData['T'].to_numpy()
r=0.03
sample_IV=reg_func(params,sample_m,sample_t)
sample_otype=sample_IvData['OPTION_TYPE']

size=len(sample_S)
for i in range(0,size-1):
    S=sample_S[i]
    K=sample_K[i]
    T=sample_T[i]
    sigma=sample_IV[i]
    
    if(sample_otype.iloc[i]=='C'):
        otype='call'
    else:
        otype='put'
    
    theoryPrice=op.getOptionValue(S,K,T,r,sigma,otype)
    print(S,K,T,r,sigma,otype,round(theoryPrice,3))

#%%






