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

def process_product_type(product_type):
    sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
    import CPUs

    sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
    import GPU

    sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
    import Motherboards

    sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
    import RAM
    
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
        wait = WebDriverWait(browser, 10)  # Wait for up to 10 seconds
        product_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'buy-button')))  # Wait for the elements to be present
        product_elements = browser.find_elements(By.CLASS_NAME, 'buy-button')  #list of products
        retry_attempts = 3
        repeat_times = random.randint(1, 5)
        for _ in range(repeat_times):
            for _ in range(retry_attempts):
                try:
                    random_index = random.randint(0, len(product_elements) - 1)  # pick random product from the list
                    random_product = product_elements[random_index]            
                    browser.execute_script("arguments[0].click();", random_product)  # click using JavaScript
                    break  # If the click is successful, exit the loop
                
                except StaleElementReferenceException:  # error that sometimes appears
                    
                    # retry the loop
                    
                    continue
            continue
        time.sleep(5)
        buy_button = browser.find_element(By.XPATH,'/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[7]/rz-cart/button')
        browser.execute_script("arguments[0].click();", buy_button) # click using JavaScript
        time.sleep(2) # wait until the element appears
        confirm_buy_button = browser.execute_script("return document.querySelector('a[href=\"https://rozetka.com.ua/ua/checkout/\"]')")
        browser.execute_script("arguments[0].click();", confirm_buy_button) # click using JavaScript
    
    browser = webdriver.Chrome()
    sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops')
    import PC_and_LaptopsCAT
    
    sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops\\subcategories\\PC_components')
    import pc_components_CAT

    run_pc_and_laptopsCAT(browser)  # starts category
    wait = WebDriverWait(browser,5)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/rz-super-portal/div/main/section/div[2]/rz-dynamic-widgets/rz-widget-list[2]/section/ul/li[1]/rz-list-tile/div/a[2]')))
    run_pc_componentsCAT(browser)  # starts subcategory
    time.sleep(5)
    if product_type == 'Cases':
        run_Cases(browser)
    elif product_type == 'SSDs':
        run_SSDs(browser)
    elif product_type == 'PSUs':
        run_PSUs(browser)
    elif product_type == 'Coollers':
        run_Coollers(browser)
    elif product_type == 'RAM':
        run_RAM(browser)
    elif product_type == 'CPUs':
        run_CPUs(browser)
    elif product_type == 'GPU':
        run_GPU(browser)
    elif product_type == 'Motherboards':
        run_Motherboards(browser)
    time.sleep(5)
    run_script(browser)
    time.sleep(3)
    browser.quit()

if __name__ == '__main__':
    logging.basicConfig(filename='script.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    pool = multiprocessing.Pool()
    product_types = ['Cases', 'SSDs', 'PSUs', 'Coollers', 'RAM', 'CPUs', 'GPU', 'Motherboards']
    browser = webdriver.Chrome()
    pool.map(process_product_type, product_types)
    pool.close()
    pool.join()
    result_values = multiprocessing.Array('i', len(product_types))
    for i, product_type in enumerate(product_types):
        result_values[i] = i
        logging.info(f"Executing {product_type} script")

    logging.info("All scripts executed")



















