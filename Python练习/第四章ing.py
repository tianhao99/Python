# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:42:15 2021

@author: kingb
"""
#%%父类继承
class A:
    def display(self):
        print('A',end='')
class B(A):
    def display(self):
        print('B',end='')
        A().display()
class C(B):
    def display(self):
        print('C',end='')
        B().display()
if __name__=='__main__':
    c=C()
    c.display()
#%%
#%%类方法和静态方法
class C:
    @classmethod            
    def add(C,x,y):       #类方法（第一个是参数类本身）
        return x+y
    @staticmethod
    def sub(x,y):         #静态方法不需要第一个参数
        return x-y
if __name__=='__main__':
    print(C.add(5,3))
    print(C.sub(5,3))
#%%
#%%动态扩展类，，，将类外部的函数，绑定到类内部，可直接调用
from types import MethodType
class A:
    def __init__(self,val):
        self.val=val
def func(self):
    print(self.val)
if __name__=='__main__':
    a=A(1)
    a.func=MethodType(func, a)
    a.func()
#%%
#%%读写装饰器
class A:
    @property
    def t(self):
        return self._t      #必须在属性名前加下划线，否则会因不断递归调用报错
    @t.setter
    def t(self,t):
        self._t=t           #必须在属性名前加下划线，否则会因不断递归调用报错
if __name__=='__main__':
    a=A()
    a.t=10
    print(a.t)
#%%
#%%
import math
#请在此处补充Circle类定义的代码（提示：计算圆面积时使用math.pi获取圆周率）
class Circle:
    def SetCenter(self,x,y):
        self.x=x
        self.y=y
    def SetRadius(self,r):
        self.r=r
    def GetArea(self):
        return math.pi*self.r**2

if __name__=='__main__':
    x=eval(input()) #输入圆心的x坐标
    y=eval(input()) #输入圆心的y坐标
    r=eval(input()) #输入半径
    c=Circle() #创建Cirle对象
    c.SetCenter(x,y) #设置圆心
    c.SetRadius(r) #设置半径
    print('center:(%.2f,%.2f),radius:%.2f'%(c.x,c.y,c.r)) #输出圆心和半径
    print('area:%.2f'%c.GetArea()) #输出面积
#%%
#请在此处写出Time类定义的代码
class Time:
    def AddOneSec(self):
        self.s+=1
        if self.s==60:
            self.m+=1
            self.s = 00
            if self.m == 60:
                self.h += 1
                self.m = 00
                if self.h == 24:
                    self.h = 0

        '''if self.m<60 and self.s<59:        #自己写的
            self.s+=1
        elif self.m<59 and self.s==59:
            self.m+=1
            self.s=0
        elif self.m==59 and self.s==59 and self.h<23:
            self.h+=1
            self.m=0
            self.s=0
        elif self.m==59 and self.s==59 and self.h==23:
            self.h=0
            self.m=0
            self.s=0'''
    def SetTime(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s

if __name__=='__main__':
    h=int(input()) #输入时
    m=int(input()) #输入分
    s=int(input()) #输入秒
    count=int(input()) #输入要数的秒数
    t=Time()
    t.SetTime(h,m,s)
    for i in range(count):
        print('%02d:%02d:%02d'%(t.h,t.m,t.s)) #输出当前时间
        t.AddOneSec()

#%%
#%%
import math
#请在此处写出Cylinder类定义的代码（提示：计算体积时使用math.pi作为圆周率）
class Cylinder:
    def __init__(self,r,h):
        self.r=r
        self.h=h
    
    def GetVolume(self):
        return math.pi*self.r**2*self.h

if __name__=='__main__':
    r=eval(input()) #输入半径
    h=eval(input()) #输入高
    c=Cylinder(r,h) #创建Cylinder对象
    print('radius:%.2f,height:%.2f'%(c.r,c.h)) #输出半径和高
    print('volume:%.2f'%c.GetVolume()) #输出体积
#%%
xd=eval(input())
num=eval(input())
ls=[]
pls=[]
for i in range(num):
    m = eval(input())
    ls.append(m)
for j in range(num) :   
    if ls[j] == xd:
       pls.append(j)
print(pls[:])

#%%
xd=eval(input())
num=eval(input())
ls=[]
pls=[]
for i in range(num):
    m = eval(input())
    ls.append(m)
for j in range(num) :   
    if ls[j] == xd:
       pls.append(ls.index(xd,j))
print(pls[:])

#%%
import copy
a=[[1.2,True],'Python']

b=copy.deepcopy(a)

a[0][0]=3.5

print(b)
#%%
def primelist(n):
    for i in range(2,n+1):
        m=int(i**0.5)
        for j in range(2,m+1):
            if i%j==0:
                break
        else:
          yield i
if __name__=='__main__':
    n=eval(input())
    for i in primelist(n):
        print(i, end=' ')
#%%
class seq:
    def __init__(self, beg, step):
        self.val=beg
        self.step=step
    def __next__ (self):
        oldval=self.val
        self.val+=self.step
        return oldval
    def __iter__(self):
        return self
if __name__=='__main__':
    s=seq(3,2)
    for i in range(5):
        print(next(s),end=' ')
#%%选择排序
n = eval(input())
ls=[]
i,count = 0,0
while i < n:
    x = eval(input())
    ls.append(x)
    i += 1
while count < n-1:
    m = min(ls[count:])
    idx = ls.index(m)
    if idx != count:
        ls[idx] = ls[count]
        ls[count] = m
    count += 1
    print(ls)
#%%    幻方
#在此处编写is_magicsquare函数的定义代码
def is_magicsquare(ls1):
    n = len(ls1)
    sum1,sum2,sum3 = 0,0,0
    lsm = set()
    for x in range(n):
        for y in range(n):
            lsm.add(ls1[x][y])
    if len(lsm) != n**2:
        return False
   
    
    for i in range(n):
        sum1 = sum1+ls1[i][i]
    for x in range(n):
        for y in range(n):
            sum2 = sum2 + ls1[x][y]
            sum3 = sum3 + ls1[y][x]
        if sum1 == sum2 and sum1 == sum3:
            sum2 = 0
            sum3 = 0
        else:
            return False
            break
    return True


if __name__=='__main__':
    n = eval(input())
    ls = []
    for i in range(n):
        ls.append(list(eval(input())))
    print(ls)
    if is_magicsquare(ls)==True:
        print('Yes')
    else:
        print('No')

#%%
n = eval(input())
ls = {}
for i in range(n):
   ky = input()
   nam = input()
   ls.update({nam:ky})#ls[nam] = ky
n1 = eval(input())
ls1 = []
for i in range(n1):
    ls1.append(input())
for j in range(n1):
    for i in ls.keys():
        if ls1[j] == i:
            print(ls[i]) 
            break
    else :
        print('notfound') 
    














