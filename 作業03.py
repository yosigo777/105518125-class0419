# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:32:56 2022

@author: 劉育秀
"""

n = int(input("要印幾行？"))
pascalList=[]

#計算Pascal三角形的值
for i in range(n):
    pascalList.append([])
    pascalList[i].append(1)
    for j in range(1,i):
        pascalList[i].append(pascalList[i-1][j-1]+pascalList[i-1][j])
    if(n!=0):
        pascalList[i].append(1)

#輸出Pascal三角形
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(pascalList[i][j]),end=" ",sep=" ")
    print()