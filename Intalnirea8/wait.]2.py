from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s= Service(ChromeDriverManager().install())
chrome=webdriver.Chrome(service=s)
chrome.maximize_window()


actual=chrome.current_url
exceted= 'https://formy-project.herokuapp.com/'
chrome.find_element(By.LINK_TEXT, 'autocomplete').click()
sleep(2)
chrome.get("https://formy-project.herokuapp.com/autocomplete")
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Marius')
sleep(2)

assert actual == exceted, f'Url invalid: excepted {exceted}, found {actual}'


