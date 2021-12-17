

from selenium.webdriver import Chrome
import time
import csv

def subject_save(url,count):
    web.get(url)
    time.sleep(10)
    # 获取专业报录信息
    name = web.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/h3').text.split('报考')[-2].split(' ')[-1]
    hang_subject = web.find_elements_by_xpath('//*[@id="table"]/tbody/tr')
    for ii in hang_subject:
        name_subject = ii.find_element_by_xpath('./td[2]').text
        plan_pope_subject = ii.find_element_by_xpath('./td[4]').text
        low_subject = ii.find_element_by_xpath('./td[5]').text
        finish_pope_subject = ii.find_element_by_xpath('./td[6]').text
        years = ii.find_element_by_xpath('./td[7]').text
        cost = ii.find_element_by_xpath('./td[8]').text
        remarks = ii.find_element_by_xpath('./td[11]').text
        f1 = open(f'第{count}次网报统计/{name}网报统计.csv', mode='a', encoding='utf-8')
        wri1 = csv.writer(f1)
        wri1.writerow([name_subject, plan_pope_subject, low_subject, finish_pope_subject, years, cost, remarks])
    # web.close()
    print('完成专业获取！')

def data_save(url,count):
    web.get(url)
    time.sleep(5)
    hang_school = web.find_elements_by_xpath('//*[@id="table"]/tbody/tr')
    j = 1
    lis_code = []
    # 获取学校报录信息
    for i in hang_school:
        pici = i.find_element_by_xpath('./td[1]').text
        num = i.find_element_by_xpath('./td[2]').text
        lis_code.append(num)
        name = i.find_element_by_xpath('./td[3]/a/i')       #这里不加.text，录入时加入，因为后边点击操作还要用
        plan_pope = i.find_element_by_xpath('./td[4]').text
        low = i.find_element_by_xpath('./td[5]').text
        should_pope = i.find_element_by_xpath('./td[8]').text
        finish_pope = i.find_element_by_xpath('./td[9]/a/i').text
        f = open(f'第{count}次网报统计.csv',mode='a',encoding='utf-8')
        wri = csv.writer(f)
        wri.writerow([pici,num,name.text,plan_pope,low,should_pope,finish_pope])
        print(f'完成{j}个')
        j +=1

    print('全部完成！')
    return lis_code


if __name__ == '__main__':
    web = Chrome()

    url1 = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_35_41_20/tj/tjyx.html?path=B'
    # url2 = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_36_42_17/tj/tjyx.html?path=B'
    # url3 = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_43_16/tj/tjyx.html?path=B'
    # url4 = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_44_11/tj/tjyx.html?path=B'
    # url5 = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_E1_45_12/tj/tjyx.html?path=B'


    lis_code = data_save(url1,'一')
    # data_save(url2,'二')
    # data_save(url3,'三')
    # data_save(url4,'四')
    # data_save(url5,'五')
    cont = 1
    for ij in lis_code:
        if cont < 3:    #因为第一次网报，前两个数据为本科一批，网址为3B+....，本科二批为4B+.....
            url1_subj = f'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_35_41_20/tj/tjzy.html?path=3B{ij}'
            subject_save(url1_subj,'一')
            cont +=1
        else:
            url1_subj = f'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_35_41_20/tj/tjzy.html?path=4B{ij}'
            subject_save(url1_subj, '一')


