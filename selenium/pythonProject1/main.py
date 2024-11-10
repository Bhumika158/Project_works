from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar= driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents= driver.find_element(By.CLASS_NAME,value="a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")
my_dic={}
event_times=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_name= driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")

for n in range(0,len(event_times)):
    my_dic[n]={
        "time":event_times[n].text,
        "name":event_name[n].text
    }
print(my_dic)
driver.close()