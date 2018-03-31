# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:36:58 2018

@author: fan
作业1：
先将作业中的数据，写入excel，在把数据从excel中加载进来
"""
import pandas as pd
import seaborn as sns
import matplotlib
import numpy as np

df=pd.read_excel('snow.xlsx')
#画散点图
sns.pairplot(df, x_vars='X', y_vars='Y', size=5, aspect=0.8,kind='reg')
#求相关系数
print(df.corr())
'''
（1）答：由于相关系数为 0.988996 ，所以x与y的关系为 非常强的'正'线性关系
'''

'''
 (2) 利用sk-learn 求出Y关于x的一元线性方程
'''

from sklearn.linear_model import LinearRegression
# 第一步：构建X、Y数据集
x=df[['X']]
y=df[['Y']]
# 第二步：创建线性模型
linreg = LinearRegression()
linreg.fit(x,y)
Intercept =linreg.intercept_
coefficient=linreg.coef_

'''
 (2)答：方程式为：y=140.95363128+364.18196329x
 
 (3)若今年的X=7，估计Y的值
'''
y1=140.95363128+364.18196329*7
outcome = linreg.predict(7)
#两种方式计算结果 都是 2690.22737431



'''
作业2 根据数据求出关于Y的“多”元线性模型
'''
# 第一步导入数据，并绘制散点图，初步判断一下线性关系
ground_df=pd.read_excel('ground.xlsx')
print ground_df
sns.pairplot(ground_df,x_vars=['X1','X2','X3'],y_vars='Y',size=3, aspect=1)
# 结论：x2，x3与y的线性相关性不太大

# 第二步自变量因变量的数据集
x=ground_df[['X1','X2','X3']]
y=ground_df[['Y']]

# 第三步创建线性模型
linreg = LinearRegression()
linreg.fit(x,y)
Intercept =linreg.intercept_
coefficient=linreg.coef_

# 第四部构建测试集和训练集
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=1)
linreg.fit(X_train, y_train) 

y_pred = linreg.predict(X_test)
# 第五部 误差评估
from sklearn import metrics

# calculate MAE using scikit-learn
print "MAE:",metrics.mean_absolute_error(y_test,y_pred)
#18.2946018105

# calculate MSE using scikit-learn
print "MSE:",metrics.mean_squared_error(y_test,y_pred)
#395.862060455

# calculate RMSE using scikit-learn
print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred))
#19.8962825788

##模型比较 按照以上过程再来一次 
feature_cols = ['X1']

x1 = ground_df[feature_cols]
y1 = ground_df.Y

x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, random_state=1)

linreg.fit(x1_train, y1_train)

y1_pred = linreg.predict(x1_test)


# calculate MAE using scikit-learn
print "MAE:",metrics.mean_absolute_error(y1_test,y1_pred)
#8.87716315538

# calculate MSE using scikit-learn
print "MSE:",metrics.mean_squared_error(y1_test,y1_pred)
#122.300302714

# calculate RMSE using scikit-learn
print "RMSE:",np.sqrt(metrics.mean_squared_error(y1_test,y1_pred))
#11.0589467272

'''
  答：删除x2，x3变量后与全变量的线性回归方程比较，删除后的较好
'''
