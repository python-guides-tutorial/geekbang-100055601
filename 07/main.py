from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
sleep(2)
driver.find_element(By.ID,'kw').send_keys('selenimu')
sleep(1)
driver.find_element(By.ID,'su').click()

sleep(20)
driver.quit()