from errno import ENOSR
from xml.dom.minidom import Entity

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count=driver.find_element(By.CSS_SELECTOR,value='#articlecount a')
# # article_count.click()
#
# link_text = driver.find_element(By.LINK_TEXT,value='Content portals')
# # link_text.click()
#
# search= driver.find_element(By.NAME,value="search")
# search.send_keys("Python",Keys.ENTER)

