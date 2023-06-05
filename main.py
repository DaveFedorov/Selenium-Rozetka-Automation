import time
import sys
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops')
import PC_and_LaptopsCAT

sys.path.insert(0, 'W:\\my_project\\categories\PC_and_Laptops\\subcategories\\PC_components')
import pc_components_CAT
browser = webdriver.Chrome() 
def run_pc_laptops(browser):
    PC_and_LaptopsCAT.run(browser)

def run_pc_components(browser):
    pc_components_CAT.run(browser)

if __name__ == '__main__':
    browser = webdriver.Chrome() 
    run_pc_laptops(browser) #starts category
    time.sleep(3)
    run_pc_components(browser) #starts sub category