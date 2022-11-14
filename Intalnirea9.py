
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.implicitly_wait(5) # se declara o singura data
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Marius')
first_name2 = chrome.find_element(By.ID, 'last-name')
first_name2.send_keys("BYe bye")

