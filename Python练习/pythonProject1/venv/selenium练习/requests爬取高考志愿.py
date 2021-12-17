
import csv
import requests

url = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_35_41_20/data/tjzy.json'

resp = requests.get(url)
resp.encoding = 'utf-8'
dic = resp.json()
for i in range(8074):
    pici = dic[i]['title'].split(' ')[0]
    sch_number = dic[i]['path'][-3:]
    school = dic[i]['title'].split('报考')[-2].split(' ')[-1]
    sub_number = dic[i]['zydh']
    sub_name = dic[i]['zymc']
    sub_character = dic[i]['jhxzmc']
    plan_num = dic[i]['jhs']
    low = dic[i]['lqzdf']
    apply_num = dic[i]['ybrs']
    years = dic[i]['xznx']
    if 'xf' in dic[i]:
        tuition = dic[i]['xf']
    else:
        tuition = '无'
    if 'bxdd' in dic[i]:
        base = dic[i]['bxdd']
    else:
        base = '无'
    if 'bz' in dic[i]:
        remark = dic[i]['bz']
    else:
        remark = '无'
    f = open('第一次网报统计.csv',mode='a',encoding='utf-8')
    wri = csv.writer(f)
    wri.writerow([pici,sch_number,school,sub_number,sub_name,sub_character,plan_num,low,apply_num,years,tuition,base,remark])
    print(f'完成{i+1}个')
print('全部完成！！！')
f.close()
