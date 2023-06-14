import time
import logging
import sys
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import GPU
sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops')
import PC_and_LaptopsCAT

sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
import pc_components_CAT

browser = webdriver.Chrome()

def run_GPU(browser):
    GPU.run(browser)

def run_pc_and_laptopsCAT(browser):
    PC_and_LaptopsCAT.run(browser)

def run_pc_componentsCAT(browser):
    pc_components_CAT.run(browser)


def run_login(browser):
    your_email = "pepito.mussiloni@gmail.com" #DO NOT FORGET TO PASTE YOUR EMAIL!
    your_password = "wL23VrdTjZ6UQ7" #DO NOT FORGET TO PASTE YOUR PASSWORD!
    sign_in_button = browser.find_element(By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]")
    sign_in_button.click()
    time.sleep(2)
    email_input = browser.find_element(By.XPATH,"/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[1]/input")
    email_input.send_keys(your_email)

    password_input = browser.find_element(By.XPATH,"/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[2]/div/div/input")
    password_input.send_keys(your_password)

    login_button = browser.find_element(By.XPATH,"/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]")
    login_button.click()
def run_favorite_products(browser):
    wait = WebDriverWait(browser, 10)
    product_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wish-wrapper")))  # Wait for the elements to be present
    product_elements = browser.find_elements(By.CLASS_NAME, "wish-wrapper")  #list of products
    retry_attempts = 3
    repeat_times = random.randint(2, 7)
    for _ in range(repeat_times):
        for _ in range(retry_attempts):
            try:
                random_index = random.randint(0, len(product_elements) - 1)  # pick random product from the list
                random_product = product_elements[random_index]            
                random_product.click()  # click using JavaScript
                time.sleep(10)
                break  # If the click is successful, exit the loop
            
            except StaleElementReferenceException:  # error that sometimes appears
                
                # retry the loop
                
                continue
        continue

    

run_pc_and_laptopsCAT(browser)
time.sleep(3)
run_login(browser)
time.sleep(30)
run_pc_componentsCAT(browser)
time.sleep(3)
run_GPU(browser)
time.sleep(3)
run_favorite_products(browser)