FORM_LINK="https://docs.google.com/forms/d/e/1FAIpQLScvlKOm-aA7wBrDzh1NTVA6A28e4Kv-L_Q9eB0OU7mLXJCDwg/viewform?usp=sf_link"
ZILLOW_URL= "https://appbrewery.github.io/Zillow-Clone/"
from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

response= requests.get(ZILLOW_URL)
soup=BeautifulSoup(response.text,'html.parser')
li_elements= soup.find_all('li',class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(FORM_LINK)

property_link=[]
prices=[]
addresses=[]
for li in li_elements:
    a_tag= li.find('div',class_="StyledPropertyCardDataWrapper").find("a")
    if a_tag and a_tag.has_attr('href'):
        property_link.append(a_tag['href'])

    price_text= li.find('span',class_="PropertyCardWrapper__StyledPriceLine").text
    price= re.split(r'[+/]',price_text)[0].strip()
    prices.append(price)

    address= a_tag.find("address").text.replace("\n","").replace("|","").strip()
    addresses.append(address)

time.sleep(5)
for i in range(len(property_link)+1):
    time.sleep(5)
    address_in = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_in = driver.find_element(By.XPATH,
                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_in = driver.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_in.send_keys(addresses[i])
    price_in.send_keys(prices[i])
    link_in.send_keys(property_link[i])
    submit.click()
    time.sleep(2)
    another_resp= driver.find_element(By.LINK_TEXT,"Submit another response")
    another_resp.click()
    time.sleep(5)
