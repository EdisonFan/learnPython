# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:12:19 2017

@author: fan
"""


import numpy as np
import pandas as pd

df=pd.read_csv('macrodata.csv')
print(macrodata['realgdp'])

#绘制直方图
df['realgdp'].plot.hist(bins=100,title='Histograms')


#绘制散点图
df.plot.scatter(x='realgdp',y='realcons',color='red',title='scatter');
