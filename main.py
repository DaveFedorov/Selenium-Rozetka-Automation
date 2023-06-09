import time
import logging
import sys
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename='script.log',filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops')
import PC_and_LaptopsCAT

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import CPUs

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import GPU

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import Motherboards

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import RAM

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import pc_components_CAT

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import Coollers

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import PSUs

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import SSDs

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import Cases

def run_Cases(browser):
    Cases.run(browser)

def run_SSDs(browser):
    SSDs.run(browser)

def run_PSUs(browser):
    PSUs.run(browser)

def run_Coollers(browser):
    Coollers.run(browser)

def run_RAM(browser):
    RAM.run(browser)

def run_CPUs(browser):
    CPUs.run(browser)

def run_GPU(browser):
    GPU.run(browser)

def run_Motherboards(browser):
    Motherboards.run(browser)

def run_pc_and_laptopsCAT(browser):
    PC_and_LaptopsCAT.run(browser)

def run_pc_componentsCAT(browser):
    pc_components_CAT.run(browser)


def run_script(browser):
    product_elements = browser.find_elements(By.CLASS_NAME, 'goods-tile__title')
    retry_attempts = 3
    for _ in range(retry_attempts):
        try:
            random_index = random.randint(0, len(product_elements) - 1)  # pick random product from the list
            random_product = product_elements[random_index]            
            browser.execute_script("arguments[0].click();", random_product)  # click using JavaScript
            break  # If the click is successful, exit the loop
        except StaleElementReferenceException:  # error that sometimes appears
        # retry the loop
            continue
    time.sleep(5)
    buy_button = browser.find_element(By.XPATH,'/html/body/app-root/div/div/rz-product/div/rz-product-tab-main/div[1]/div[1]/div[2]/rz-product-main-info/div[1]/div[1]/rz-product-buy-btn/app-buy-button/button')
    #buy_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div/rz-product/aside/rz-product-carriage/div/div[2]/div/rz-product-buy-btn/app-buy-button/button')))
    browser.execute_script("arguments[0].click();", buy_button) # click using JavaScript
    time.sleep(1) # wait until the element appears
    confirm_buy_button = browser.execute_script("return document.querySelector('a[href=\"https://rozetka.com.ua/ua/checkout/\"]')")
    browser.execute_script("arguments[0].click();", confirm_buy_button) # click using JavaScript

if __name__ == '__main__':
    productType =[
        ('Cases', run_Cases),
        ('SSDs', run_SSDs),
        ('PSUs', run_PSUs),
        ('Coollers', run_Coollers),
        ('RAM', run_RAM),
        ('CPUs', run_CPUs),
        ('GPU', run_GPU),
        ('Motherboards', run_Motherboards)
    ]
    for productTypes_name, productType_script, in productType:
        logging.info(f"Executing {productTypes_name} script")
        browser = webdriver.Chrome()
        run_pc_and_laptopsCAT(browser) # starts category
        time.sleep(1)
        run_pc_componentsCAT(browser) # starts subcategory
        time.sleep(1)
        productType_script(browser)
        time.sleep(1)# delay
        run_script(browser)
        time.sleep(3)
        browser.quit()
        logging.info("All scripts executed")