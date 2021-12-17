# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:26:04 2021

@author: kingb
"""


from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

class CtripCommentsCrawler:
    def __init__(self, url):
        self.url = url
    
    def getdata(self, pagenum, filepath):
        try:
            option = Options()
            option.add_experimental_option('excludeSwitches', ['enable-automation']) #启用开发者模式
            driver = webdriver.Chrome(options=option)
            driver.get(url)
            with open(filepath, 'w', encoding='utf-8') as f:
                for pageno in range(1,pagenum+1):
                    trynum = 0
                    while True:
                        try:
                            comments = driver.find_elements_by_css_selector('#divCtripComment > div.comment_detail_list > div')
                            break
                        except:
                            trynum += 1
                            if trynum > 6:
                                break
                            time.sleep(5)
                            continue
                    for comment in comments:
                        comment_main = comment.find_element_by_class_name('comment_main')
                        comment_title = comment_main.find_element_by_class_name('comment_title')
                        score = comment_title.find_element_by_class_name('score')
                        n = score.find_element_by_class_name('n').text
                        comment_txt = comment_main.find_element_by_class_name('comment_txt')
                        J_commentDetail = comment_txt.find_element_by_class_name('J_commentDetail').text
                        f.write('{0},{1}\n'.format(n, J_commentDetail))
                    print('page. {0}'.format(pageno))
                    try:
                        nextpage = driver.find_element_by_css_selector('#divCtripComment > div.c_page_box > div > a.c_down')
                        driver.execute_script("arguments[0].click();", nextpage)
                        #nextpage.click()
                        time.sleep(5)
                    except:
                        break
        finally:
            driver.quit()
        
if __name__=='__main__':
    url = 'https://hotels.ctrip.com/hotel/1073814.html?isFull=F&masterhotelid=1073814&hcityid=2#ctm_ref=hod_sr_lst_dl_n_1_2'
    crawler = CtripCommentsCrawler(url)
    crawler.getdata(5, './ctripcomments.csv')