#[MAC]:SSL Certificate Fail
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context()
from urllib.request import urlopen, urlretrieve
import json
import os #與系統新增、修改、刪除相關操作

for y in range(2017,2019):
    for m in range(1,13):
        url = "https://www.google.com/doodles/json/"+str(y)+"/"+str(m)+"?hl=zh_TW"
        respone = urlopen(url) #類似開啟遠端檔案
        #print(respone.read()) 檢視未解碼格式資料，重複使用read會導致使用出錯
        pics = json.load(respone) #load讀取檔案轉List/Dict，loads讀取字串轉List/Dict
        #pics is a List；p is a Dict
        for p in pics:
            print(p['title']) #key=title
            prul = "https:" + p['url']
            print(prul)
            #urlretrieve('下載網址','下載後檔名')
            dn = 'pictures/'+str(y)+'/'+str(m)+'/' #資料夾路徑"/"不可忽略
            fn = dn + prul.split('/')[-1] #當副檔名不同，用原有檔名當檔案名
            #mkdir僅創造路徑最後資料夾；makedirs=>mkdir -p
            if not os.path.exists(dn):
                os.makedirs(dn) #先創造資料夾
            urlretrieve(prul,fn)