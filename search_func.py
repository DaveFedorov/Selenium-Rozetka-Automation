import multiprocessing
import time
import logging
import sys
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import GPU

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops')
import PC_and_LaptopsCAT
    
sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import pc_components_CAT

def run_GPU(browser):
    GPU.run(browser)

def run_pc_and_laptopsCAT(browser):
    PC_and_LaptopsCAT.run(browser)

def run_pc_componentsCAT(browser):
    pc_components_CAT.run(browser)

def run_script(browser):
    wait = WebDriverWait(browser, 5)
    product_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'goods-tile__title')))
    random_index = random.randint(0, len(product_elements) - 1)
    random_product = product_elements[random_index]  
    random_product_title = random_product.text.split("(")[0].strip()
    print(random_product_title)
    main_page_button = browser.find_element(By.CLASS_NAME,"breadcrumbs__link")
    main_page_button.click()
    search_bar = wait.until(EC.presence_of_element_located((By.NAME, 'search')))
    search_bar.clear()
    search_bar.send_keys(random_product_title)
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button')))
    search_button.click()
    time.sleep(3)
    result_products = browser.find_elements(By.CLASS_NAME,'goods-tile__title')
    found = False
    for result_product in result_products:
        if random_product_title in result_product.text:
            found = True
            break
    if found:
        print("Product was found")
    else:
        print("Product was NOT found")
browser = webdriver.Chrome()

PC_and_LaptopsCAT.run(browser)
time.sleep(3)
pc_components_CAT.run(browser)
time.sleep(3)
GPU.run(browser)
time.sleep(3)
run_script(browser)