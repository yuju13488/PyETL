#install package "pytube"
from selenium.webdriver import Chrome
import time
import secret
from pytube import Playlist
import os

driver = Chrome("./chromedriver")
driver.get("https://www.youtube.com/view_all_playlists")
# 輸入帳號
(driver.find_element_by_id("identifierId")
       .send_keys("r99921052@g.ntu.edu.tw"))
driver.find_element_by_id("identifierNext").click()
# 輸入密碼
time.sleep(3)
(driver.find_element_by_class_name("whsOnd")
       .send_keys(secret.pwd))
driver.find_element_by_id("passwordNext").click()

# 取得播放清單
time.sleep(5)
playlists = driver.find_elements_by_class_name("vm-video-title-text")
# 紙條: .text
# (bs) ["href'"] -> get_attribute("href")
for p in playlists:
    print(p.text)
    print(p.get_attribute("href"))
    try:
        pl = Playlist(p.get_attribute("href"), suppress_exception=True) #suppress_exception=True略過已移除影片
        dn = "youtube/" + p.text
        if not os.path.exists(dn):
            os.makedirs(dn)
        pl.download_all(dn)
    except:
        print("放棄這播放清單")