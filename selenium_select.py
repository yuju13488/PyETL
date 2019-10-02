from  selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select #selenium的下拉式選單功能
import time

driver = Chrome("./chromedriver")
driver.get("https://www.marathonsworld.com/artapp/racelist.php?p=1") #開啟網址
time.sleep(10) #因網頁開啟緩慢需等待10秒以上
year = Select(driver.find_element_by_xpath("//select[@id='year']")) #
year.select_by_value("2019") #從value尋找
run = Select(driver.find_element_by_xpath("//select[@id='type']")) #
run.select_by_index("1")
time.sleep(10)
driver.close()