from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
s = Service(GeckoDriverManager().install())
firefox = webdriver.Firefox(service=s)

firefox.maximize_window()

firefox.get('https://formy-project.herokuapp.com/form')

first_name = firefox.find_element(By.ID, 'first-name')
first_name.send_keys('Matei')

sleep(3)
firefox.quit()

'''
pt alte browsere
https://pypi.org/project/webdriver-manager/#use-with-firefox
'''