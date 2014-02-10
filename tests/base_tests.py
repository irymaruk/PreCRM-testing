# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

###############################################################
######################### Pge Objects #########################
###############################################################

class CustomerPage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_user_info(self, user_name):
        return self.driver.find_element_by_xpath("//*[@id='userInfo']/a[1]").text

    def set_user_name(self, user_name):
        self.driver.find_element_by_xpath("//label[text()='Логін:']").send_keys(user_name)

    def bt_exit_click(self):
        self.driver.find_element_by_xpath("//a[text()='Вийти']").click()
        return LoginPage(self.driver)


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def set_user_name(self, user_name):
        self.driver.find_element_by_xpath("//label[text()='Логін:']").send_keys(user_name)

    def set_user_password(self, user_password):
        self.driver.find_element_by_xpath("//label[text()='Пароль:']").send_keys(user_password)

    def bt_enter_click(self):
        locator = "//span[text()='Зайти']"
        elem = self.driver.find_element_by_xpath(locator)
        self.driver.click(elem)
        return CustomerPage(self.driver)




###############################################################
############################ TESTS ############################
###############################################################

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://172.16.1.13")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.close()

class TestLogin(BaseTestCase):

    #def test_login_success(self):
    def do_login(self, user_name, user_password):
        # Заходимо на домашню сторінку і успішно проходимо авторизацію
        login_page = LoginPage(self.driver)
        login_page.set_user_name(user_name)
        login_page.set_user_password(user_password)
        customer_page = login_page.bt_enter_click()
        title = self.wait.until(EC.title_is(u'PreCRM. Клієнти'))
        # Перевіряємо, що ми дійсно на сторінці Клієнти і виходимо на сторінку логіну
        assert u'PreCRM. Клієнти' in customer_page.get_title()
        assert user_name in customer_page.get_user_info()
        login_page = customer_page.bt_exit_click()
        # Перевіряємо, що ми дійсно на сторінці Авторизації і успішно проходимо авторизацію
        assert u'PreCRM. Логін' in login_page.get_title()

    def test_login_success_lowercase(self):
        self.do_login('test1234', 'qwer4321')

    def test_login_success_uppercase(self):
        self.do_login('TEST1234', 'qwer4321')


if __name__ == "__main__":
    unittest.main()