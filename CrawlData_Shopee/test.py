# list = [""]

# if not list:
#     list.append("")
# else:
#     print("t")
    
# if not list:
#     list.append("")
# else:
#     print("t")

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

options = uc.ChromeOptions() 
# options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
options.headless = False
driver = uc.Chrome(options)
driver.get(SHOPEE_LOGIN_URL)
wait = WebDriverWait(driver, TIMEOUT)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("HAHA")
# element_1 = driver.find_elements(By.XPATH,NUM_AVAILABLE_XPATH)
# print(element_1[0].text)
sleep(10)
Username = wait.until(EC.visibility_of_element_located((By.NAME, "loginKey")))
Username.send_keys("name")

print("Oke")
driver.maximize_window()
sleep(random.uniform(7,10))
# elements = driver.find_elements(By.CSS_SELECTOR,'.flex')
# # element = driver.find_element(By.CSS_SELECTOR,'div.flex.items-center > div:nth-child(2)')

# # element_2 = driver.find_element(By.CSS_SELECTOR, NUM_LIKE_CLASS_NAME)


# # elements = driver.find_elements(By.CSS_SELECTOR, PRODUCT_DETAIL_HEADER_CLASS_NAME)

# # for element in elements:

# # print(element_2.text)
# # # print(elements.text)
# # for element in elements: 
# #     print(element.text)
# try:
#     div_elements = driver.find_elements(By.CSS_SELECTOR, ".dR8kXc")
# except:
#     pass

# product_detail = {}
# list_header = []
# list_content = []
# for element in div_elements:
#     header = element.find_element(By.CSS_SELECTOR,".zquA4o")
#     list_header.append(header.text)
#     contents = element.find_elements(By.CSS_SELECTOR, ":not(.zquA4o)")
#     list_content.append(contents[0].text)

# i = 0
# for header in list_header:
#     product_detail[header] = list_content[i]
#     i = i + 1
