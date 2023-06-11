import random
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

def run(browser):
    browser.get('https://rozetka.com.ua/ua/')
    category1 = browser.find_element(By.XPATH, '/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[1]/rz-sidebar-fat-menu/div/ul/li[1]/a') #this is laptops and PC category
    browser.execute_script("arguments[0].click();", category1) #click using javascript
if __name__ == '__main__':
    browser = webdriver.Chrome()
    run(browser)
