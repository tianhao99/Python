# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:03:47 2021

@author: kingb
"""

#%%花括号
a = {10,2.5,'test',3+4j,True,5.3,2.5}
print(a)
#%%


#%%数字-----返回星期几
week = '星期'
num1='一二三四五六日'
s=eval(input("请输入数字:"))
print(week + num1[s-1])
#%%

#%%花括号
d={'Python':1,'C++':2,'Java':3}
for k in d:
    print('%s:%d'%(k,d[k]))
#%%


#%%
#n的阶乘
n = eval(input('请输入一个大于0的整数：'))
s = 1
for i in range(1,n+1):
    s = s*i
print(s)
#%%

#%%求100以内能被7整除的最大整数[自己写的]
i = 1
s = 7
while s<=100:
    i+=1
    s = i*7
s = (i-1)*7    
print(s)

#%%

n = 100
while n>=0:
    if n%7 ==0:
        print(n)
        break
    n-=1
#%%

#判断素数
n = eval(input('请输入一个大于0的整数：'))
for i in range(2,n):
    if n%i == 0:
        print('%d不是一个素数'%n)
        break
    
    if i == n-1:
        print('%d是一个素数'%n)
        

#%%输出素数
p=eval(input())
for n in range(2,p+1):
    m = int(n**0.5)
    i = 2
    while i <= m:
        if n%i ==0:
            break
        i+=1
    if i>m:
        print(n,end='\n')
    
#%%水仙花数
p=eval(input())
q=eval(input())
t=0
for n in range(p,q):
    bai=n//100
    shi=n//10%10
    ge=n%10
    if bai**3+shi**3+ge**3==n:
        print(n)
        t=1
if t==0:
    print('not found')
    
#%%九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end=(' '))
    print('\n')  

#%%判奇偶
n = eval(input('请输入一个整数'))
if n%2==0:
    print('even number')
else:
    print('odd number')

#%%1-1/3+1/5-----1/99

n=eval(input())
j,m=1,0
for i in range(1,99999,2):
    if j==n+1:
        break
    elif j%2==0:
        m-=1/i
    else:
        m+=1/i
    j+=1    
print('%.2f'%m)
#%%判断闰年
n = eval(input('请输入年份'))
if n%400==0 and n%4==0:
    print('yes')
elif n%100!=0 and n%4==0: 
    print('yes')
else:
    print('no')
#%%对于数值x，如果x在区间(1,2]上，则输出x+2.5的值；如果x在区间[-1,1]上，则输出4.35x的值；如果x在区间[-2,-1)上，则输出x的值；如果x为其他值，则输出“invalid”
n = eval(input())
if n>1 and n<=2:
    print(n+2.5)
elif n>=-1 and n<=1:
    print(4.35*n)
elif n>=-2 and n<-1:
    print(n)
else:
    print('invalid')
#%%1!+2!+3!++++m!
n = eval(input())
i,s=1,0
while i<=n:
    m=1
    for j in range(1,i+1):
        m=m*j
    s=s+m 
    i+=1
print(s)
#%%10元5元1元人民币组成N元
n = eval(input())
shi=n//10                   #最多有几个10元  如22   shi=2
wu=n%10//5                  #10元之后有几个5元       wu=0
yi=n%10%5                   #5元之后剩余为1元        yi=2
print('%d,%d,%d'%(shi,wu,yi))     #输出第一个序列     2 0 2
k=1                         #统计组合次数
while True:
           wuu=wu           #wuu调用5元个数，并让wu保留数据
           yii=yi           #yii调用1元个数，并让yi保留数据
           while wuu>0:     #10元个数不变，将5元变成1元
                wuu=wuu-1
                yii=yii+5
                print('%d,%d,%d'%(shi,wuu,yii))   #变换一个5元输出一次
                k+=1                 #统计组合次数
           if shi>0 :      #5元分空后，若10元不为0，将10元换成2个5元，回到上一个循环继续分5元
               shi=shi-1
               wu=wu+2
               print('%d,%d,%d'%(shi,wu,yi))
               k+=1
           if yii==n:      #若1元面值等于N时，意味10元、5元全部分空，退出循环
               break
print(k)                   #输出统计的组合次数
#%%10元5元1元人民币组成N元
n = eval(input())
count=0
for ten in range(0,n//10+1):
    for five in range(0,(n-ten*10)//5+1):
        one=n-ten*10-five*5
        print('%d,%d,%d'%(ten,five,one))
        count+=1
print(count)
#%%n能否被m整除
def zchu(m,n):
    if m%n==0:
        return 0
    else:
        return m
sum1,x=0,1
while x !=0:
    x=eval(input())
    sum1 = sum1+zchu(x, 3)
print(sum1)
#%%装饰器
def deco(func):

    def inner(x,y):

        print('deco begin')

        func(x,y)

        print('deco end')

    return inner

@deco

def add(a,b):

    print(a+b)

if __name__=='__main__':

    add(3,5)
#%%判素
def sushu(n):
    if n<2 :
        print('invalid')
    else:
        i=2
        for i in range(2,n):
            if n%i == 0:
                break
        if i >= n-1:
            print('yes')
        else:
            print('no')
x=1      
while x !=0:
    x=eval(input())
    if x!=0:
        sushu(x)
    else:
        break
#%%判断两个字符串是否为对应前缀
def beg1 (a,b):
    i=0
    lena=len(a)                  #取短的字符串长度为leni
    lenb=len(b)
    if lena>lenb:
        leni=lenb
    else:
        leni=lena
    for i in range(leni):        #遍历两个字符串并比较，仅到leni为止
       if a[i]==b[i]:
           i+=1
       else:
           break                 #若字符串不同，直接退出，此时i<leni,输出no
    if i==leni:                  #若遍历至结尾都相同，i=leni，是前缀
        print(a[0:leni])         #因前缀相同，输出a或b都可以
    else:
        print('no')


x=str(input())
y=str(input())
beg1(x, y)        
#%%
def jcheng (n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s     
def Cgailv (x,y):   
    m=0
    if x<y and x>1 and y>1:
      for i in range(1,x+1):
          m+=jcheng(y)/jcheng(i)/jcheng(y-i)
      print('%d'%m) 
    else:
      print('invalid')    

p = int(input()) 
q = int(input())    
Cgailv(p, q) 
#%%判断一个输入数据是否是整数,之后做相应的运算
def zhengxing (x):
    for i in range(len(x)):
        if x[i]<'0'or x[i]>'9':
            return False
            break
    return True
  
x=input()
y=input()
 
if zhengxing(x) and zhengxing(y):
   print(int(x)-int(y))
elif zhengxing(x) and zhengxing(y)==False:
   print(y*int(x))
elif zhengxing(x)==False and zhengxing(y):
   print(x*int(y))
else:
   print(x+y)
#%%汉诺塔
def hanoi (n,A,B,C):
    if n==1:
        print('%d:%s->%s'%(n,A,C))
    else:
        hanoi(n-1, A, C, B)
        print('%d:%s->%s'%(n,A,C))
        hanoi(n-1, B, A, C)
A,B,C='A','B','C' 
n=eval(input())   
hanoi(n, A, B, C)
#%%
class Student:
    def __init__(self,name='unknown'):
        self.name=name
    def PrintInfo(self):
        print(self.name)
if __name__=='__main__':
    stu1=Student()
    stu2=Student('Marry')
    stu1.PrintInfo()
    stu2.PrintInfo()
#%%
class Student:
    def __init__(self,name):
        self.name=name
    def __del__ (self):
        print(self.name)
if __name__=='__main__':
    stu1=Student('Li Xiaoming')
    stu2=Student('Ma Hong')
    stu3=stu2
    del stu2
    del stu1    
#%%
class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def __eq__(self,other) :
        return self.h==other.h and self.m==other.m and self.s==other.s
    def __ne__(self,other) :
        return self.h!=other.h or self.m!=other.m or self.s!=other.s
if __name__=='__main__':
    t1=Time(8,10,15)
    t2=Time(8,10,15)
    t3=Time(9,12,30)
    print(t1==t2)
    print(t1!=t3)   
#%%
class A:
    def fa(self):
        print('A')
class B(A):
    def fb(self):
        print('B')
if __name__=='__main__':
    b=B()
    b.fa()
    b.fb()
#%%
class A:
    def display(self):
        print('A')
class B:
    def display(self):
        print('B')
def func(a):
    a.display()
if __name__=='__main__':
    a=A()
    b=B()
    func(a)
    func(b)   
#%%
class A:
    def display(self):
        print('A',end='')
class B(A):
    def display(self):
        print('B',end='')
        a.display()
class C(B):
    def display(self):
        print('C',end='')
        b.display()
if __name__=='__main__':
    c=C()
    c.display()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

