from selenium.webdriver.common.by import By



# login_page
swich_click = (By.LINK_TEXT, '账号登录')
login_name = (By.ID, 'username')
login_pwd = (By.ID, 'password')
login_piccode = (By.ID, 'validcode')
login_btn = (By.CSS_SELECTOR,'.account-form .form-sub')