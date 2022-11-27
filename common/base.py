from selenium import webdriver

class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc):
        return self.driver.find_element(loc[0],loc[1])

    def click_element(self,loc):
        self.find_element(loc).click()

    def send_keys(self,loc,content):
        input_element = self.find_element(loc)
        input_element.clear()
        input_element.send_keys(content)




