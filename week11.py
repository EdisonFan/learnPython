# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:27:16 2018

@author: fan
第一题：
data1 是40名癌症病人的一些生存资料，其中，X1表示生活行动能力评分（1~100），X2表示病人的年龄，X3表示由诊断到直入研究时间（月）；X4表示肿瘤类型，X5把ISO两种疗法（“1”是常规，“0”是试验新疗法）；Y表示病人生存时间（“0”表示生存时间小于200天，“1”表示生存时间大于或等于200天）
试建立Y关于X1~X5的logistic回归模型
"""

from numpy import *
import pandas as pd
data=pd.read_table('data1.txt',encoding='gbk')
x=data.iloc[:,1:6].as_matrix()
y=data.iloc[:,6].as_matrix()
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR 

rlr=RLR()
rlr.fit(x, y)
rlr.get_support()
fit_x = data[data.columns[rlr.get_support()]].as_matrix() #筛选好特征
lr=LR()
lr.fit(fit_x,y)
lr.score(fit_x, y)
#正确率水平为 75%

'''
第二题：
data2 是关于重伤病人的一些基本资料。自变量X是病人的住院天数，因变量Y是病人出院后长期恢复
的预后指数，指数数值越大表示预后结局越好。
'''