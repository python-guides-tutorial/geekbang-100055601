from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
 
class TestCase(object):

  def __init__(self):
    self.driver = webdriver.Chrome()

  def test(self):
    self.driver.get('https://www.baidu.com')
    sleep(2)
    self.driver.find_element(By.ID,'kw').send_keys('selenium')
    sleep(1)
    self.driver.find_element(By.ID,'su').click()

    sleep(20)
    self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test()