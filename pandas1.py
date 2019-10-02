from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
#install package "pandas"
import pandas as pd
#準備空表格(columns固定欄位順序)
df = pd.DataFrame(columns=["評價","日文","英文","詳細"])

page=59
while True:
    print('頁數：',page)
    url = "https://tabelog.com/tw/tokyo/rstLst/"+str(page)+"/?SrtT=rt"
    page += 1
    try:
        response = urlopen(url)
    except:
        print('Last Page!')
        #save,index=False不存index
        df.to_csv('tabelog.csv',encoding="utf-8",index=False)
        break
    html = BeautifulSoup(response)
    rs = html.find_all('li',class_='list-rst')
    for r in rs:
        ja = r.find('small',class_='list-rst__name-ja')
        en = r.find('a',class_='list-rst__name-main')
        score = r.find('b', class_='c-rating__val')
        prices = r.find_all('span', class_="c-rating__val")
        print(en.text,ja.text,score.text)
        print('晚間',prices[0].text)
        print('午間',prices[1].text)
        print(en["href"])
        #準備資料
        data = {"評價":score.text,
                "日文":ja.text,
                "英文":en.text,
                "詳細":en["href"]}
        #寫入資料
        #data frame專屬，屬於append。改變舊df，新df=None。
        df = df.append(data,ignore_index=True) #append改變原本df，但df.append為動作無值為None