import requests
import json
from bs4 import BeautifulSoup

start = 0 #檔案主名稱使用
page = 0 #頁數使用
while True:

    #找出開發人員工具 -> Network -> search?ei=...... -> Headers中不同之處
    #將ijn=、start=改為=0
    url = ("https://www.google.com/search?ei=jTFnXcSJEK3YhwOPq5_ADg&rlz=1C1SQJL_zh-TWTW836TW836&yv=3&q=%E6%96%B0%E5%9E%A3%E7%B5%90%E8%A1%A3&tbm=isch&vet=10ahUKEwiEhOfe_abkAhUt7GEKHY_VB-gQuT0IOCgB.jTFnXcSJEK3YhwOPq5_ADg.i&ved=0ahUKEwiEhOfe_abkAhUt7GEKHY_VB-gQuT0IOCgB&ijn="
            + str(page) + "&start="
            + str(page * 100) + "&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc")
    page +=1 #加入動態頁數後立即+1

    #找到accept-language項目
    headers = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6"
    }
    response = requests.get(url,headers=headers)
    html = BeautifulSoup(response.text)

    #找到網頁原始碼中有關鍵字圖片副檔名（.jpg）處的div，"pt"標題、"ou"位置、"ity"格式、"ru"圖片出處網址......
    pictures = html.find_all("div",class_="rg_meta")
    if len(pictures) ==0: #提取圖片結束
        print('finished')
        break
    for p in pictures:
        data = json.loads(p.text) #loads
        print("類型",data['ity'])
        print("標題",data['pt'])
        print('連結',data['ou'])
        try: #處理網址無法連結
            response = requests.get(data['ou'],stream=True) #下載
            if data['ity'] == "":
                fn = "yui/" + str(start) + ".jpg" #檔名
            else:
                fn = "yui/" + str(start) + "." + data['ity'] # 檔名
            f = open(fn,"wb") #開啟網路檔案（先手動創資料夾）
            f.write(response.raw.read()) #寫入
            f.close()
            start += 1
        except:
            print('pass')