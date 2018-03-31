# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:30:56 2018

@author: fan
"""
import datetime
import cx_Oracle
from pandas import Series, DataFrame 
import pandas as pd

db = cx_Oracle.connect('calis', 'calis123', '162.105.139.4:1521/orcl')
dsn_tns = cx_Oracle.makedsn('162.105.139.4', 1521, 'orcl')
print dsn_tns
print db.version

cursor = db.cursor()
starttime = datetime.datetime.now()
x=cursor.execute('select t.* from T_INDICES_HINIT_DATA_2017  t where rownum<=1000000') 

print type(x)
rs= x.fetchall()
print type(rs)
data=DataFrame(rs)
data.to_csv('b.csv')
endtime = datetime.datetime.now()
print (endtime - starttime)
cursor.close()
db.close()