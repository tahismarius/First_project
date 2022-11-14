import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller


class Keyboard(unittest.TestCase):
    USER = (By.ID, 'username')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)

    # @unittest.skip
    def test_select_all(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        user = self.chrome.find_element(*self.USER)
        # user.send_keys('Matei CORVIN')
        # sleep(3)
        # user.clear()  #  metoda clear este folosita pentru a sterge tot continutul unui textbox
        # sleep(3)
        # user.send_keys('MIHAI VITEAZUL')
        # sleep(3)
        user.send_keys('Matei CORVIN')
        user.send_keys(Keys.CONTROL, 'A')
        sleep(3)
        user.send_keys(Keys.BACKSPACE)
        # user.send_keys(Keys.ARROW_LEFT)
        # sleep(2)
        # user.send_keys('test')
        # sleep(2)

    def test_backpsace_for(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")
        user = self.chrome.find_element(*self.USER)
        user.send_keys('QWERTYUIOP')
        for i in range(0, 10):
            user.send_keys(Keys.BACKSPACE)
            sleep(0.5)
            i += 1
        sleep(3)

    def tearDown(self):
        self.chrome.quit()

# https://the-internet.herokuapp.com/key_presses