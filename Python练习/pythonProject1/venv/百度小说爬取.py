
import requests
import asyncio
import aiohttp

async def getChapterContent(bo_id,cid,title):
    url_txt = 'http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"'+bo_id+'","cid":"'+bo_id+'|'+cid+'","need_bookinfo":1}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url_txt) as resp:
            dic = await resp.json()
            txt = dic['data']['novel']['content']
            with open (f'novel/{title}.txt', mode='a',encoding='utf-8') as f:
                f.write(txt)
                print(title + '已完成！')
async def getCatalog(url,bo_id):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for items in dic['data']['novel']['items']:
        cid = items['cid']
        title = items['title']
        tasks.append(asyncio.create_task(getChapterContent(bo_id, cid, title)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    bo_id = '4306063500'
    urlone = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+bo_id+'"}'#采用三个字符串拼接，因为有大括号直接f需要用转译符
    asyncio.run(getCatalog(urlone,bo_id))

