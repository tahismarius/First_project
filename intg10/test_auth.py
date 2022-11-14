import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Authentication(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)

    def tearDown(self):
        self.chrome.quit()

    # @unittest.skip
    def test_auth(self):
        self.chrome.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
        sleep(3)

        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element
                                                     ((By.XPATH, '//*[@id="content"]/div/p'),
                                                      "Congratulations! You must have the proper credentials."))

        assert actual is True
        print('Mesajul este corect')

# https://admin:admin@the-internet.herokuapp.com/basic_auth -> Pagina formatata fara variabile

# https://the-internet.herokuapp.com/basic_auth