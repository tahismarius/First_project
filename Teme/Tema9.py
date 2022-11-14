import unittest
from time import sleep
from unittest import TestCase

import selenium.webdriver.support.color
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(TestCase):
    LOGIN_BTN = (By.LINK_TEXT, 'Form Authentication')
    PAGE_TITLE = (By.LINK_TEXT, 'The Internet')
    MESSAGE_ERROR_LOGIN = (By.XPATH, '//div//div//div[@class="flash error"]')
    MESSAGE_SUCCES_LOGIN = (By.XPATH, '//div//div//div[@class="flash success"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.implicitly_wait(1)
        self.chrome.find_element(*self.LOGIN_BTN).click()

    def tearDown(self) -> None:
        self.chrome.quit()

    def test1(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'The Page is not open correct')

    def test2(self):
        actual = self.chrome.title
        expected = "The Internet"
        self.assertEqual(actual, expected)

    def test3(self):
        actual = self.chrome.find_element(By.XPATH, '//h2').text
        expected = "Login Page"
        self.assertEqual(actual, expected)

    def test4(self):
        self.chrome.find_element(By.XPATH, '//form/button').is_displayed()

    def test5(self):
        self.chrome.find_element(By.XPATH, '//a[text()="Elemental Selenium"]').is_enabled()

    def test6(self):
        self.chrome.find_element(By.XPATH, '//form/button').click()
        message = self.chrome.find_element(*self.MESSAGE_ERROR_LOGIN)
        self.assertTrue(message.is_displayed(), 'The message is correct.')

    def test7(self):
        self.chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('invalid')
        self.chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('invalid')
        self.chrome.find_element(By.XPATH, '//form/button').click()
        actual = self.chrome.find_element(By.XPATH, '//div//div//div[@class="flash error"]').text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect.')

    def test8(self):
        self.chrome.find_element(By.XPATH, '//form/button').click()
        self.chrome.find_element(By.XPATH, '//a[@class="close"]').click()
        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element
                                                     ((By.XPATH, '//div//div//div[@id="flash"]'),
                                                      "Your username is invalid!"))
        if actual:
            print('Message is not displayed!')
        else:
            print(f'Message is displayed!')

    def test9(self):
        actual = [self.chrome.find_element(By.XPATH, '//label[@for="username"]').text,
                  self.chrome.find_element(By.XPATH, '//label[@for="password"]').text]
        expected = ["Username", "Password"]
        self.assertEqual(actual[0], expected[0]) and self.assertEqual(actual[1], expected[1])

    def test10(self):
        self.chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//form/button').click()
        WebDriverWait(self.chrome, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div//div//div[@class="flash success"]')))
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(actual, expected, 'The Page is not open correct.')
        message2 = self.chrome.find_element(*self.MESSAGE_SUCCES_LOGIN)
        self.assertTrue(message2.is_displayed(), 'The message is correct.')
        actual = self.chrome.find_element(By.XPATH, '//div//div//div[@class="flash success"]').text
        expected = 'secure area!'
        self.assertTrue(expected in actual, 'Success message text is correct.')

    def test11(self):
        self.chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//form/button').click()
        self.chrome.find_element(By.XPATH, '//div//a[@class="button secondary radius"]').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'The Page is not open correct.')

    def test12(self):
        text_of_website = self.chrome.find_element(By.XPATH, '//div//h4').text
        x = text_of_website.split()
        for split in x:
            self.chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
            self.chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys(split)
            self.chrome.find_element(By.XPATH, '//form/button').click()
            if self.chrome.current_url == 'https://the-internet.herokuapp.com/secure':
                print(f'The secret password is : {split}')
                break
        else:
            print('I couldn t find the password')