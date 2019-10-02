#以python指令控制Chrome
#install package "selenium"

from  selenium.webdriver import Chrome
import time

driver = Chrome("./chromedriver")
driver.get("https://www.facebook.com") #開啟網址
#find=>find_element；find_all=>find_elements
driver.find_element_by_id("email").send_keys("account_number") #send_keys輸入
driver.find_element_by_id("pass").send_keys("password") #輸入密碼
driver.find_element_by_id("loginbutton").click() #按下登入按鈕
c = input("請輸入驗證碼：")
driver.find_element_by_id("approvals_code").send_keys(c) #輸入驗證碼
driver.find_element_by_id("checkpointSubmitButton").click() #按下繼續

time.sleep(1) #等待1秒跑網頁再按下繼續
driver.find_element_by_id("checkpointSubmitButton").click()

time.sleep(3) #等待3秒跑網頁再抓取貼文
content = driver.find_element_by_class_name("userContent") #class定位（根據class屬性找到輸入框），class_name必須唯一（空白格中擇一）
print(content.text)

#等待3秒後關閉
time.sleep(3)
driver.close()