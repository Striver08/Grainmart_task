import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

url = "https://www.dramexchange.com/"
browser = webdriver.Chrome()
browser.get("https://www.dramexchange.com/")
code = browser.page_source  #Here the code for the webpage is extracted.
#print(code)
soup = BeautifulSoup(code) #The webpage code is beautified so it is easier to read and find the content.
#print(soup)
table = soup.find("tbody", attrs = {"id": "tb_NationalDramSpotPrice"}) #Here, the code for required table is extracted in the "table" variable.

soup1 = table.findAll('td', attrs = {"class": "tab_tr_gray"}) #From the extracted table the content of the table is extracted
arr = []
for i in soup1:       #The for loop is used here so as to store the table elements in an array and print our required element.
    arr.append(i.text)
print(arr[7])

time.sleep(7)        #The "browser.close" is used so as to close the tab after the pause of 7 seconds of work is done.
browser.close()      