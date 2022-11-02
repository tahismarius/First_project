from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())


# selector by link text
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Checkboxes').click()
# sleep(2)
# chrome.quit()
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Hovers').click()
# sleep(2)
# chrome.quit()
# # 3
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Key Presses').click()
# sleep(2)
# chrome.quit()
#

# # selector by partial link text
# # 1
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Download').click()
# sleep(2)
# chrome.quit()
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Typos').click()
# sleep(2)
# chrome.quit()
# # 3
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Dropdown').click()
# sleep(2)
# chrome.quit()


# selector by id
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.ID, 'search_query_top').send_keys('toops')
# sleep(2)
# chrome.quit()
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.ID, 'contact-link').click()
# sleep(2)
# chrome.quit()
# # 3
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php?controller=contact')
# chrome.find_element(By.ID, 'id_order').send_keys('Cash')
# sleep(2)
# chrome.quit()

# Name selector
# 1/2
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php/')
# chrome.find_element(By.NAME, 'search_query').send_keys('Heloo , i found you')
# chrome.find_element(By.NAME, 'submit_search').click()
# sleep(2)
# chrome.quit()
# 3
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php/')
# chrome.find_element(By.NAME, 'email').send_keys('elonmusk30@gmail.com')
# sleep(2)
# chrome.quit()

# selector by Tag

# 1
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_elements(By.TAG_NAME, 'input')
# 2
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_elements(By.TAG_NAME, 'input')[5].send_keys('425300')
# # 3
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_elements(By.TAG_NAME, 'input')[1].send_keys('First strret')
# input_list = chrome.find_elements(By.TAG_NAME, 'input')[2]
# input_list.send_keys('Second Street')
# sleep(2)
# chrome.quit()

# selector by class name
# 1
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php')
#
# list1 = chrome.find_elements(By.CLASS_NAME, 'login')
# list1[0].click()
# sleep(2)
# # 2
# chrome = webdriver.Chrome(service=s)
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_elements(By.CLASS_NAME, 'product_img_link')[3].click()
# sleep(2)
# # 3
# chrome.find_element(By.CLASS_NAME, 'sf-with-ul').click()
# sleep(2)
# chrome.quit()

# selector by CSS
# 1 attribute value
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter address"').send_keys('Ilva')
# sleep(2)
# 2 id
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input#street_number').send_keys('102C')
# sleep(2)
# 3 class
# chrome = webdriver.Chrome(service=s)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('27')
# sleep(2)
# chrome.quit()