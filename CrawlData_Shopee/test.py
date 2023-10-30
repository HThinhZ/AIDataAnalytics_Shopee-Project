# import libraries
from Settings import *
import numpy as np 
from selenium import webdriver
from time import sleep
import random 
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class A:
    def __init__(self):
        options = uc.ChromeOptions() 
        # options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
        options.headless = False
        self.driver = uc.Chrome(options)
        self.driver.maximize_window()
        
    def close_driver(self):
        sleep(2)
        self.driver.quit()
    
    def init_new_driver(self):
        options = uc.ChromeOptions() 
        # options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
        options.headless = False
        self.driver = uc.Chrome(options)
        self.driver.maximize_window()
        

# options = uc.ChromeOptions() 
# # options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
# options.headless = False
# driver = uc.Chrome(options)
# driver.maximize_window()
# driver.get(SHOPEE_LOGIN_URL)
# wait = WebDriverWait(driver, TIMEOUT)
# wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# sleep(random.uniform(1, 2))
# # self.driver.find_element(By.NAME, "loginKey").send_keys(self.username)
# Username =wait.until(EC.visibility_of_element_located((By.NAME, "loginKey")))
# Username.send_keys(USERNAME)
# sleep(random.uniform(2, 3))
# Password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
# Password.send_keys(PASSWORD)
# sleep(random.uniform(2, 3))
# Button = wait.until(EC.element_to_be_clickable((By.XPATH,LOGIN_BUTTON)))
# Button.click()
# print("Login successfully")
# sleep(4)
# mall_page = MALL_URL + str("sp.btw2")
# driver.get(mall_page)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, TOTAL_PAGE_CLASS_NAME)))
# element = driver.find_element(By.CSS_SELECTOR, TOTAL_PAGE_CLASS_NAME)
# print(element.text)

options = uc.ChromeOptions() 
# options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
options.headless = False
driver = uc.Chrome(options)
driver.get("https://shopee.vn/%C3%81o-croptop-n%E1%BB%AF-hai-d%C3%A2y-th%E1%BB%9Di-trang-YANDO-AT12-Ch%E1%BA%A5t-li%E1%BB%87u-Thun-thun-borip-co-gi%C3%A3n-%C4%90en-Tr%E1%BA%AFng-2-m%C3%A0u-i.332828338.16808013617?sp_atk=79d925ad-6ad2-4612-864f-a070f63d4b89&xptdk=79d925ad-6ad2-4612-864f-a070f63d4b89")
# wait = WebDriverWait(driver, TIMEOUT)
# wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
driver.maximize_window()
sleep(5)
print("HAHA")
element_1 = driver.find_elements(By.CSS_SELECTOR,NUM_AVAILABLE_CLASS_NAME)
print(element_1[0].text)
driver.quit()
import os
import subprocess
if os.name == 'nt':  
    # subprocess.run('taskkill /F /IM chromedriver.exe /T', check=True, shell=True)
    try:
        subprocess.run('taskkill /F /IM chrome.exe /T', check=True, shell=True)
    except:
        print("Shuted down")
