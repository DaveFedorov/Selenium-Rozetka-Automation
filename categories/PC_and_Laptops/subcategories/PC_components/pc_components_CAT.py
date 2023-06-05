import random
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

def run(browser):
    category1 = browser.find_element(By.XPATH, '/html/body/app-root/div/div/rz-super-portal/div/main/section/div[2]/rz-dynamic-widgets/rz-widget-list[2]/section/ul/li[1]/rz-list-tile/div/a[2]') #this is laptops and PC category
    browser.execute_script("arguments[0].click();", category1) #click using javascript
if __name__ == '__main__':
    browser = webdriver.Chrome()
    run(browser)