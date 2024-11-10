from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3954674611&f_LF=f_AL&geoId=105556991&keywords=python%20developer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

sign_in= driver.find_element(By.CSS_SELECTOR, value='.sign-in-modal button')
sign_in.click()

session_key= driver.find_element(By.NAME,value='session_key')
session_key.send_keys("bhumikapeshwani158@gmail.com")


session_password= driver.find_element(By.NAME,value='session_password')
session_password.send_keys("MummyBhumikaLinkedIn158.")

button= driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
button.click()