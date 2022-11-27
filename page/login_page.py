from  common.base import Base
from selenium.webdriver.common.by import By
import page

class Login(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def swich_btn(self):
        self.click_element(page.swich_click)


    def login_name(self,userName):
        self.send_keys(page.login_name,userName)

    def login_pwd(self,pwd):
        self.send_keys(page.login_pwd,pwd)

    def login_piccode(self,piccode):
        self.send_keys(page.login_piccode,piccode)

    def login_btn(self):
        self.click_element(page.login_btn)



