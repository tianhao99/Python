def wrapper(fn):
    """
    装饰器
    :param fn: 被装饰的函数
    :return: inner
    """
    def inner(*args,**kwargs):
        i =5
        while i>0:

            """执行目标函数之前需要的操作"""
            ret = fn(*args,**kwargs)
            i-=1
            """执行目标函数之后需要的操作"""

        return ret
    return inner

@wrapper
def temp():
    print('小李飞刀李寻欢')


if __name__ == '__main__':
    temp()