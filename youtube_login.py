from  selenium.webdriver import Chrome
import time
#install package "secret"
#import secret

driver = Chrome("./chromedriver")
driver.get("https://www.youtube.com/view_all_playlists")
#帳號
(driver.find_element_by_id("identifierId").send_keys("account_number"))
driver.find_element_by_id("identifierNext").click()
#密碼
time.sleep(3) #等待google驗證帳號存在時間
(driver.find_element_by_class_name("whsOnd").send_keys("password")) #點選輸入密碼框找到class="whsOnd zHQkBf"以空白為分隔，擇一即可
driver.find_element_by_id("passwordNext").click()

#取得播放清單
time.sleep(5)
playlists = driver.find_element_by_class_name("vm-video-title-text")
#(bs4)["href"] => get_attribute("href")
for p in playlists:
    print(p.text)
    print(p.get_attribute("href"))