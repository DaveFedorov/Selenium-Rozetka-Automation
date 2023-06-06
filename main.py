import time
import sys
import random
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
sys.path.insert(0, 'W:\\my_project\\categories\\PC_and_Laptops')
import PC_and_LaptopsCAT

sys.path.insert(0, 'W:\\my_project\\categories\PC_and_Laptops\\subcategories\\PC_components')
import CPUs

sys.path.insert(0, 'W:\\my_project\\categories\PC_and_Laptops\\subcategories\\PC_components')
import GPU

sys.path.insert(0, 'W:\\my_project\\categories\PC_and_Laptops\\subcategories\\PC_components')
import Motherboards

sys.path.insert(0, 'W:\\my_project\\categories\PC_and_Laptops\\subcategories\\PC_components')
import RAM

sys.path.insert(0, 'W:\\my_project\\categories\PC_and_Laptops\\subcategories\\PC_components')
import pc_components_CAT
browser = webdriver.Chrome() 
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

if __name__ == '__main__':
    browser = webdriver.Chrome() 
    run_pc_and_laptopsCAT(browser) #starts category
    time.sleep(1)
    run_pc_componentsCAT(browser) #starts sub category
    time.sleep(1)
    run_CPUs(browser)
    