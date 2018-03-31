# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 14:27:58 2017

@author: fan
"""

import numpy as np
import matplotlib.pyplot as plt

#随机生成100个正态分布的数据，并计算平均值与标准差
data=np.random.randn(10000)
print(data)
print('avg=',np.average(data))
print('std',np.std(data))

plt.hist(data,100)
plt.show()