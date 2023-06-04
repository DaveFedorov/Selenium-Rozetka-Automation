import random
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() 
browser.get('https://rozetka.com.ua/ua/')
category1 = browser.find_element(By.XPATH, '/html/body/app-root/div/div/rz-main-page/div/main/rz-main-page-content/rz-app-fat-menu-tablet/nav/ul/li[1]/a') #this is laptops and PC category
browser.execute_script("arguments[0].click();", category1) #click using javascript
sub_category1 = browser.find_element(By.XPATH,'/html/body/app-root/rz-single-modal-window/div[3]/div[2]/fat-menu-mobile/ul[1]/li[4]/a/span') #GPU category
browser.execute_script("arguments[0].click();", sub_category1) #click using javascript
product_elements = browser.find_elements(By.CLASS_NAME, 'goods-tile__title') #list all products on the page


retry_attempts = 3  
for _ in range(retry_attempts):
    try:
        random_index = random.randint(0, len(product_elements) - 1) #pick random product form the list 
        random_product = product_elements[random_index]
        browser.execute_script("arguments[0].click();", random_product) #click using javascript
        break  # If the click is successful, exit the loop
    except StaleElementReferenceException: #error that sometimes appears idkw
        # retry the loop
        continue
buy_button = browser.find_element(By.XPATH,'/html/body/app-root/div/div/rz-product/div/rz-product-tab-main/div[1]/div[1]/div[2]/rz-product-main-info/div[1]/div[1]/rz-product-buy-btn/app-buy-button/button')
browser.execute_script("arguments[0].click();", buy_button) #click using javascript
time.sleep(3) #wait untill the element will apear
confirm_buy_button = browser.execute_script("return document.querySelector('a[href=\"https://rozetka.com.ua/ua/checkout/\"]')")
browser.execute_script("arguments[0].click();", confirm_buy_button) #click using javascript