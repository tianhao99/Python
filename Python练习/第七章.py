# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:01:39 2021

@author: kingb
"""

class UserError(BaseException):
    def __init__(self,msg): #定义构造方法
        self.msg=msg
    def __str__(self): #将UserError类对象转换为字符串时自动调用该方法
        return self.msg
if __name__=='__main__':
    try:
        raise UserError('user defined error')
    except UserError as e:
        print(e)
#%%
import os
path=input()
if os.path.isabs(path):
    print('yes')
else:
    print('no')
#%%

import os
path=input()
ls = []
ls = os.path.splitext(path)
print(ls[1])  

#%%
str=input()
try:
    s = eval(str)
    if str.isdigit():
        print('yes')
    else:
        print('no')
except:
    print('invalid')
    
ZeroDivisionError()
#%%
n=int(input())
try:
    assert n%2!=0      #assert函数，后面条件成立继续执行，不成立报AssertionError错误
    print('yes')
except AssertionError:
    print('no')
#%%


def findsubstr(str,sub):
    beg=0
    rlt=[]
    while True:
        try:
            pos=str.index(sub,beg)
            rlt.append(pos)
            beg=pos+1
        except ValueError:
            break
    return rlt
    
s1=input()
s2=input()
rlt=findsubstr(s1,s2)
if len(rlt) == 0:
    print('notfound')
else:
    print(rlt)










