from action.login_action import LoginAction
from common.driver import GetDriver
import time
class TestLogin:
    def setup(self):
        self.driver = GetDriver().getDriver()
        self.driver.get(r"http://www.mtxshop.com:3000/login")
        self.loginAction = LoginAction(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()


    def testLogin(self):
        print("*************开始了test")
        self.loginAction.login('summerstar','king862166605.','1512')
        print("*****************结束了test")
