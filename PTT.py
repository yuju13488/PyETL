#install package "requests"
import requests
from bs4 import BeautifulSoup
import os
import json

#找出五頁文章連結
start = 25701
howmany = 5
total = []
for i in range(howmany):
    url = 'https://www.ptt.cc/bbs/Beauty/index'+str(start-i)+'.html'
    response = requests.get(url,cookies={"over18":"1"})
    html = BeautifulSoup(response.text)
    for t in html.find_all("div",class_="title"):
        #沒有a代表被刪除
        if not t.find("a") == None:
            turl = "https://www.ptt.cc" + t.find("a")["href"]
            total.append(turl)

#針對每一篇文章下載
for u in total:
    url = u
    #當同一網址有不同顯示->cookie（網址列最前面鎖頭圖案）
    #cookie自動附加的附加資訊：網址->+附加資訊(over18)->Server
    response = requests.get(url,cookies={"over18":"1"})
    #requests，須將text欄位取出查看
    #print(response.text)
    html = BeautifulSoup(response.text)

    #作者、標題、發文時間
    metas = html.find_all('span',class_="article-meta-value")
    print("ID:",metas[0].text)
    print("看板:",metas[1].text)
    print("標題:",metas[2].text)
    print("時間:",metas[3].text)
    score = 0
    pushes = html.find_all("span",class_="push-tag")
    for p in pushes:
        if "推" in p.text: #不用"=="防p.text內清洗出來的資料有空白
            score += 1
        elif "噓" in p.text:
            score -= 1
    print('score:',score)
    saved = {"id":metas[0].text,
             "board":metas[1].text,
             "title":metas[2].text,
             "date":metas[3].text}


    #用title為名儲存資料夾，先篩選資料夾路徑不可有字元
    notallowed = [' ','？','！','/', '|', '\\', '?', '\"', ':', '<', '>', '.', '*']
    title_revised = ""
    for c in metas[2].text:
        if c not in notallowed:
            title_revised = title_revised+ c

    #圖片
    #enumerate將位置全部抓取
    for i,a in enumerate(html.find_all("a")): #i為index，a為值
        allow = ['gif','jpg','jpeg','png']
        if a["href"].split(".")[-1].lower() in allow: #篩選網址最後小寫化為allow中副檔名的
            print(a["href"])
            #.raw(圖片):stream=True方可閱讀
            img_response = requests.get(a["href"],stream = True)
            img = img_response.raw.read()

            dn = "ptt/" + title_revised #存檔資料夾路徑
            fn = dn+ "/" + str(i) + "." +a["href"].split(".")[-1]
            if not os.path.exists(dn):
                os.makedirs(dn)
            f = open(fn,"wb")
            f.write(img)
            f.close()

    #內文（刪除不必要）
    content = html.find("div",id="main-content")
    #去除不需要的部分
    ds = content.find_all("div", class_="article-metaline")
    for d in ds:
        d.extract() #清除
    ds = content.find_all("div",class_ = "article-metaline-right")
    for d in ds:
        d.extract()
        print(d)
    ds = html.find_all("div",class_ = "push")
    for d in ds:
        d.extract()
    print("內文:",content.text)
    saved["content"] = content.text

    #儲存內文（JSON）
    f = open(dn + '/meta.json','w',encoding="utf-8")
    json.dump(saved,f)
    f.close()