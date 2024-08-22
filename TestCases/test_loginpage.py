from PageObject.LoginPage import LoginPage


class Test_001_login:

    baseurl = 'https://www.saucedemo.com/'
    username = 'standard_user'
    password = 'secret_sauce'

    def test_login_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.driver.close()
        else:
            assert False

    def test_homePage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Swag Labs':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\title.png")
            self.driver.close()
            assert False
