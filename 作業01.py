# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:27:49 2022

@author: 劉育秀
"""

data = [100,80,90,70,59,30,21,35]

# 對原本的List排序
data.sort()
a="從小到大 =>"
print (a,end='')
print(data)

print("-"*30)

a="從大到小 =>"
print (a,end='')
data.sort(reverse=True)
print(data)

