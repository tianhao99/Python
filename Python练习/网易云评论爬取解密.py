# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:10:15 2021

@author: kingb
"""
#爬取网易云音乐评论
#pip install pycrypto
import requests
from Crypto.Cipher import AES
from base64 import b64encode   #字符
import json #将字典转化成字符串

#对加密代码进行解密
data = {
        'cursor': '-1',
        'offset': '0',
        'orderType': '1',
        'pageNo': '1',
        'pageSize': '20',
        'rid': "R_SO_4_1804320463",
        'threadId': "R_SO_4_1804320463"
       }

'''
    #通过设置断点找到加密函数，对加密函数进行分析，能跳过则跳过，如i为随机变量，但是c()函数中仅使用
    #i值，再无其他变量，所以取一个i值，通过浏览器获得当前i值对应的c()函数值，并设置为定值使用，
    #省去了破解c()函数加密过程。
    
    function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c                  
    }
    #生成字符串中随机16位字符    在浏览器中设置断点，获取一个i的值，将他固定。
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {   #c()中不产生随机数，可采用特殊值
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);   #a生成的随机16位字符
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),                     !!!!!
        h.encSecKey = c(i, e, f),                        !!!!!
        h
    }

    }
    window.asrsea = d,
window.asrsea(JSON.stringify(i7b), bwa1x(["流泪", "强"]), bwa1x(RQ4U.md), bwa1x(["爱心", "女孩", "惊恐", "大笑"])

JSON.stringify(i7b)==========d========data{}字符串形式
bwa1x(["流泪", "强"])========e========'010001'
bwa1x(RQ4U.md)===========f============"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
bwa1x(["爱心", "女孩", "惊恐", "大笑"]===g==="0CoJUm6Qyw8W8jud"
i ======在浏览器中设置断点，取一个值=========='VAvoY7258G0ubQhG'

'''

i = 'VAvoY7258G0ubQhG'#通过浏览器设置断点取得的一次随机数，本程序中固定使用，避免破解C()函数的加密过程
e = '010001'
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
d = json.dumps(data)
def enc_text(a,b):#解密b函数，其使用的为AES加密算法
    iv = '0102030405060708'
    aes = AES.new(key=b.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)   #创建加密器
    ba = aes.encrypt(data)     #加密,加密的内容必须是16的倍数
    strba = str(b64encode(ba),'utf-8')#转化成字符串，直接ba.encode('utf-8')不可以，因为加密后的字符串是乱的，不能被'utf-8'识别
    return strba

def get_encSecKey ():
    #这个值是在浏览器中通过固定i='VAvoY7258G0ubQhG'，时获得的encSecKey值
    #这样就避免破解c()函数的加密过程
    encSecKey = 'zw3HRMOdoMtnjknRyg+jGs8URI7gr8iYC3G3dcYr+59R9Zp/5D…vvW7Yhll7M+7KCpJXqV8Z3cmMb4iBVTk7klI/v869bMxybnGD'
    return encSecKey

def get_encText(a):
    da = to_16(a)
    encText1 = enc_text(da,g)
    encText = enc_text(encText1,i)
    return encText
def to_16(a):
    pad = 16-len(a)%16
    a += chr(pad)*pad
    return a
   
    
params = get_encText(d)
encSecKey = get_encSecKey()

#爬取代码
c
# =============================================================================
# 字典形式输出热门评论
# dic = respcom.json()
# for i in range(15):
#     print(i)
#     print(dic['data']['hotComments'][i]['content'])
# =============================================================================
