# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 08:26:19 2021

@author: kingb
"""
import next_asyncio
import asyncio
import time
# await: 当该任务被挂起后,CPU会⾃动切换到其他任务中
async def func1():
   print("func1, start")
   await asyncio.sleep(3)
   print("func1, end")
async def func2():
   print("func2, start")
   await asyncio.sleep(4)
   print("func2, end")
async def func3():
   print("func3, start")
   await asyncio.sleep(2)
   print("func3, end")
if __name__ == '__main__':
   start = time.time()
   tasks = [ # 协程任务列表
            func1(), # 创建协程任务
            func2(),
            func3()
            ]
   lop = asyncio.get_event_loop()
   #我要执⾏这个协程任务列表中的所有任务
   lop.run_until_complete(asyncio.wait(tasks))
   # asyncio.run(asyncio.wait(tasks))
   # a = func1()
   # await a
   # 我要执⾏这个协程任务列表中的所有任务
   print(time.time() - start)