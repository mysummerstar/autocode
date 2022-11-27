from selenium import webdriver
class GetDriver():
    def getDriver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2000)
        return self.driver



