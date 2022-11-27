from page.login_page import Login
from  common.base import Base
class LoginAction():

    def __init__(self,driver):
        self.driver = driver
        self.loginPage = Login(self.driver)


    def login(self, userName, pwd, piccode):
        self.loginPage.swich_btn()
        self.loginPage.login_name(userName)
        self.loginPage.login_pwd(pwd)
        self.loginPage.login_piccode(piccode)
        self.loginPage.login_btn()
