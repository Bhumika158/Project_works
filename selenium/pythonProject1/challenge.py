
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fName= driver.find_element(By.NAME,value="fName")
fName.send_keys("Bhumika")
lName= driver.find_element(By.NAME,value="lName")
lName.send_keys("Peshwani")
email= driver.find_element(By.NAME,value="email")
email.send_keys("test@gmail.com")

Button= driver.find_element(By.TAG_NAME,value='button')
Button.click()



