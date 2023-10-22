# import libraries
from Settings import *
import numpy as np 
from selenium import webdriver
from time import sleep
import random 
import undetected_edgedriver as ue
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import pandas as pd
import threading
from queue import Queue
import math

# src code: 
class Task1_Collect:
    # Init global variables:
       
    def __init__(self,username,password):
        # Declare browser:
        self.drivers = []
        # self.driver = webdriver.Edge()
        self.username = username
        self.password = password
        global titles, links
        self.titles, self.links = [], []
    
    def login(self,driver,url):
        driver.get(url)
        driver.maximize_window()
        sleep(random.uniform(3, 5))
        driver.find_element(By.NAME, "loginKey").send_keys(self.username)
        sleep(random.uniform(1, 2))
        driver.find_element(By.NAME, "password").send_keys(self.password)
        sleep(random.uniform(1, 2))
        self.click_button(driver,LOGIN_BUTTON)
    
    def click_button(self,driver,xpath):
        driver.find_element(By.XPATH,xpath).click()
        sleep(random.uniform(1, 2))
    
    def openMultiBrowsers(self,n):
        for i in range(n):
            driver = webdriver.Edge()
            self.drivers.append(driver)
        return self.drivers
    
    def loadLogin(self,driver):
        driver.maximize_window()
        self.login(driver,SHOPEE_LOGIN_URL)
        sleep(random.uniform(3, 5))
        
    def loadLoginMultiBrowsers(self):
        for driver in self.drivers:
            t = threading.Thread(target=self.loadLogin, args = (driver,))
            t.start()
    
    def loadPage(self,driver, i):
        driver.get("https://shopee.vn/sp.btw2?page={}&sortBy=ctime".format(i))
        sleep(random.uniform(5, 6))
            
    def loadMultiBrowsers(self, i):
        for driver in self.drivers:
            t = threading.Thread(target=self.loadPage, args = (driver,i,))
            t.start()
            i = i + 1
        
    def crawlParallel(self, func):
        for driver in self.drivers:  
            queue = Queue()
            print("-------Running parallel---------")
            t = threading.Thread(target=lambda q, arg1: q.put(func(arg1)), args=(queue, driver))
            t.start()
    
    def crawlParallelMutiplePages(self, func, n_pages):
        n = math.floor(n_pages/2)
        for i in range(0,n+1):
            self.loadMultiBrowsers(2*i)
            sleep(random.uniform(5, 7))
            self.crawlParallel(func)
            sleep(random.uniform(5, 7))
        
    def get_attribute_text(self,driver,class_name):
        text = []
        try:
            elements = driver.find_elements(By.CSS_SELECTOR,class_name)
        except:
            print("Retry")
        for element in elements:
            text.append(element.get_attribute("textContent"))
        return text
    
    def get_attribute_link(self,driver, class_name):
        link = []
        try:
            elements = driver.find_elements(By.CSS_SELECTOR,class_name)
        except: 
            print("Retry")
        for element in elements:
            link.append(element.get_attribute('href'))
        return link
    
    def get_detail_item(self,link):
        driver.get(link)
        sleep(random.uniform(3, 5))
        
        default_price = self.get_attribute_text(DEFAULT_PRICE_CLASS_NAME)
        discount_price = self.get_attribute_text(DISCOUNT_PRICE_CLASS_NAME)
        sleep(random.uniform(1, 2))
        
        return (default_price,discount_price)
    
    def crawl(self,driver):
        sleep(random.uniform(3, 5))
        
        titles_page = self.get_attribute_text(driver,TITLE_CLASS_NAME)
        for title in titles_page:
            self.titles.append(title)
            
        links_page = self.get_attribute_link(driver,TITLE_LINK_CLASS_NAME)
        for link in links_page:
            self.links.append(link)
    
        
# def main():
n = 2
shopee = Task1_Collect(USERNAME, PASSWORD)
shopee.openMultiBrowsers(n)
shopee.loadLoginMultiBrowsers()
sleep(random.uniform(20,25))

shopee.crawlParallelMutiplePages(shopee.crawl, 6)

titles = shopee.titles
links = shopee.links

# shopee_data.login(SHOPEE_LOGIN_URL)
# page_url = "https://shopee.vn/sp.btw2"
# df = shopee_data.crawl_multiple_pages(2,page_url)
# df.to_csv('page.csv',index=False,header=True,encoding="utf-8-sig")

