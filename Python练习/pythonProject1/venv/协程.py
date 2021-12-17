import asyncio
import aiohttp
import requests
import time

urls = [
      'http://kr.shanghai-jiuxin.com/file/2021/0602/c4ab41ce2c692d8f7a92feb54384fb6c.jpg',
      'http://kr.shanghai-jiuxin.com/file/2021/0601/fba0a3a2fbf7368e2134fa8cd6dc0dd9.jpg',
      'http://kr.shanghai-jiuxin.com/file/2021/0602/2e96200707ae7d2391f01c00959cc493.jpg'
      ]

async def download(url):
    #  s = aiohttp.ClientSession()   ====等价于===requests,后边可直接用s.get()，s.post()之类的
    name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #resp.content.read()等价于requests获得的resp.content
            #resp.text()等价于requests获得的resp.concenttext
            with open (name,mode='wb') as f:
                f.write(await resp.content.read())      #读取内容是异步的，需要await挂起
            print(f'完成{name}')

async def main():
   tasks = []
   for url in urls:
      tasks.append(asyncio.create_task(download(url)))
   await asyncio.wait(tasks)
def download1(url):#对比速度用
    name = url.split('/')[-1]
    resp = requests.get(url)
    with open (name,mode='wb') as f:
        f.write(resp.content)
    print(f'完成{i}个')

if __name__ == '__main__':
   time_start = time.time()
   asyncio.run(main())
   # for url in urls:#同步执行download1函数，对比速度
   #     download1(url)
   #     i+=1
   print(time.time()-time_start)

