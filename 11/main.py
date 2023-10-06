from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
 
class TestCase(object):

  def __init__(self):
    self.driver = webdriver.Chrome()
    self.driver.get('http://sahitest.com/demo/linkTest.htm')

  def test_webelement_prop(self):
    e = self.driver.find_element(By.ID, 't1')
    print(e.id)
    print(e.tag_name)

  def test_webelement_method(self):
    e = self.driver.find_element(By.ID, 't1')
    e.send_keys("hello world")
    sleep(5)
    e.clear()
    print(e.get_attribute('type'))

if __name__ == '__main__':
  case = TestCase()
  # case.test_webelement_prop()
  case.test_webelement_method()