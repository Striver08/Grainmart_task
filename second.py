import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

url = "https://www.dramexchange.com/"
browser = webdriver.Chrome()
browser.get("https://www.dramexchange.com/")
# In this, getting the required element by using its xpath.
element = browser.find_element_by_xpath('//*[@id="tb_NationalDramSpotPrice"]/tr[3]/td[5]')
print(element.text)

time.sleep(5)
browser.close()