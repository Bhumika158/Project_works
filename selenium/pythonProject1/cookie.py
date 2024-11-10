from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie= driver.find_element(By.ID,value="cookie")
store= driver.find_elements(By.CSS_SELECTOR,value="#store div")
store_ids= [item.get_attribute("id") for item in store]

timeout = time.time() + 5
five_min= time.time() + 60*5
while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text=price.text
            if element_text!="":
                cost= int(price.text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = store_ids[n]

        money_element= driver.find_element(By.ID,value="money").text
        if "," in money_element:
            money_element= money_element.replace(",","")
        current_cookie_count= int(money_element)

        affordable_upgrades= {}
        for cost, idValue in cookie_upgrades.items():
            if current_cookie_count>cost:
                affordable_upgrades[cost]=idValue

        highest_affordable_upgrade= max(affordable_upgrades)
        to_purchase_id= affordable_upgrades[highest_affordable_upgrade]

        driver.find_element(By.ID,value=to_purchase_id).click()
        timeout=time.time() + 5
    if time.time() >five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break




