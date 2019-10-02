from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import re #re.compile()關鍵字篩選

driver = Chrome("./chromedriver")
driver.get("https://www.marathonsworld.com/artapp/racelist.php?p=1") #開啟網址
time.sleep(10) #因網頁開啟緩慢需等待10秒以上
continue_link = driver.find_element_by_partial_link_text('trainingDaily')
print(continue_link)
driver.close()