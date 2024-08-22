from selenium.webdriver.common.by import By


class LoginPage:
    user_name_id = "user-name"
    password_id = "password"
    login_btn_id = "login-button"
    menu_btn_id = "react-burger-menu-btn"
    logout_btn_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.user_name_id).clear()
        self.driver.find_element(By.ID, self.user_name_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.login_btn_id).click()

    def clickLogout(self):
        self.driver.find_element(By.ID, self.menu_btn_id).click()
        self.driver.find_element(By.ID, self.logout_btn_id).click()