
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')


#selector by ID
try:
   first_name = chrome.find_element(By.ID, 'first-name')
   first_name.send_keys('Marius')
except Exception as e:
    print('ID-ul introdus nu este corect')
print('Am ajuns aici')
chrome.find_element(By.ID, 'first-name').send_keys('TEST AUTOMATION')

sleep(50)
chrome.quit()




