from urllib.request import urlopen, urlretrieve
import json
import os
#install package "beautifulSoup4"
#find取得html，find.all取得List
from bs4 import BeautifulSoup

page=1
while True:
    print('頁數：',page)
    url = "https://tabelog.com/tw/tokyo/rstLst/"+str(page)+"/?SrtT=rt"
    page += 1
    try:
        response = urlopen(url)
    except:
        print('Last Page!')
        break
    html = BeautifulSoup(response) #檔案 -> 最外層html
    #html.find_all('li',{'class':'list-rst'})
    rs = html.find_all('li',class_='list-rst') #用find_all取得所有list-rst列表，class_將python功能換成參數
    #type(rs) -> List
    for r in rs:
        ja = r.find('small',class_='list-rst__name-ja') #從網頁中尋找標籤：尋找class="list-rst__name-ja"的small標籤
        en = r.find('a',class_='list-rst__name-main')
        score = r.find('b', class_='c-rating__val')
        prices = r.find_all('span', class_="c-rating__val") #找出價格盒子晚間、午間兩種
        #萃取紙條：盒子.text
        #萃取特徵：盒子["href"]
        print(en.text,ja.text,score.text)
        print('晚間',prices[0].text)
        print('午間',prices[1].text)
        print(en["href"])