# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:04:35 2017
@author: 范学海
作业1. 读入  肝气郁结证型系数.xls  数据集，将数据集按照等距、小组等量 两种方式 
    分别分为5组数据，分别计算5组数据的中位数与标准差
"""

from pandas import Series, DataFrame 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange #导入拉格朗日插值函数
import numpy as np

inputfile="E:\pythonWorkSpace\study\data.xls"
df1=pd.read_excel(inputfile,header=None,skiprows=1)  

df1['categroy']= pd.cut(df1[0],5) #将第1列，按等距方式分5组
median         = df1.groupby('categroy').median() 
std            = df1.groupby('categroy').std()
median.columns = ['median']
std.columns    = ['std']

print(median) #打印中位数
print(std) #打印标准差


"""
作业2：读入BHP1.csv，使用适当的方法填补缺失值
"""

inputfile = 'E:\pythonWorkSpace\study\BHP1.csv' 
df2 = pd.read_csv(inputfile) #读入数据 
#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):  
  y = s[range(n-k, n) + range(n+1, n+1+k)] #取数  
  y = y[y.notnull()] #剔除空值  
  return lagrange(y.index, list(y))(n) #插值并返回插值结果 
  
  #将空格转化为nan
for i in df2.columns:  
  for j in range(len(df2)):  
      if str(df2.ix[j,i]).isspace():
         df2.ix[j,i]=np.NAN
print(df2)
#用拉格朗日插值填补nan值
for i in df2.columns:  
  for j in range(len(df2)):  
      if (df2[i].isnull())[j]  :
          df2[i][j] =ployinterp_column(df2[i], j)
print(df2)

"""
作业3. 读入BHP2.xlsx，与BHP1数据集合并为BHP数据集 
"""

inputfile = 'E:\pythonWorkSpace\study\BHP2.xlsx' 
df3 = pd.read_excel(inputfile) # 读入数据 
BHP=pd.concat([df2,df3],ignore_index=True)
