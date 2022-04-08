# -*- codeing = utf-8 -*-
# @Time :2022/4/7 9:50
# @Author:刘伟怡
# @File :spider.py
# @Software

from bs4 import BeautifulSoup


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls "
    saveData(savepath)


def getData(baseurl):
    datalist = []
    return datalist


def saveData(savepath):
    print("save....")
