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


async def main():
    print("start")
    # # 添加协程任务
    # t1 = asyncio.create_task(func1())
    # t2 = asyncio.create_task(func2())
    # t3 = asyncio.create_task(func3())
    # ret1 = await t1
    # ret2 = await t2
    # ret3 = await t3
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    # ⼀次性把所有任务都执⾏

    done, pedding = await asyncio.wait(tasks)

    print("end")


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)