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
import threading
from queue import Queue
import math

# src code: 
class Task1_Parallel_Collect:
    # Init global variables:
       
    def __init__(self,username,password):
        # Declare browser:
        self.drivers = []
        # self.driver = webdriver.Edge()
        self.username = username
        self.password = password
        # 
        self.status = 0
        # Declare varibles:
        global titles, links, default_price, promotional_price, \
            num_reviews, rating, num_sold, num_available
        self.titles, self.links, self.default_price, \
        self.promotional_price, self.num_reviews, \
        self.rating, self.num_sold, self.num_available\
            = [], [], [], [], [], [], [], []
    
    def login(self,driver,url):
        driver.get(url)
        driver.maximize_window()
        sleep(random.uniform(4, 6))
        driver.find_element(By.NAME, "loginKey").send_keys(self.username)
        sleep(random.uniform(2, 3))
        driver.find_element(By.NAME, "password").send_keys(self.password)
        sleep(random.uniform(2, 3))
        self.click_button(driver,LOGIN_BUTTON)
    
    def click_button(self,driver,xpath):
        driver.find_element(By.XPATH,xpath).click()
        sleep(random.uniform(1, 2))
    
    def openMultiBrowsers(self,n):
        for i in range(n):
            # driver = webdriver.Edge()
            options = uc.ChromeOptions()
            # options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
            options.headless = False
            driver = uc.Chrome(options)
            self.drivers.append(driver)
        return self.drivers
    
    def loadLogin(self,driver):
        self.login(driver,SHOPEE_LOGIN_URL)
        sleep(random.uniform(3, 5))
        
    def loadLoginMultiBrowsers(self):
        for driver in self.drivers:
            t = threading.Thread(target=self.loadLogin, args = (driver,))
            t.start()
    
    def loadPage(self,driver, i):
        driver.get("https://shopee.vn/sp.btw2?page={}&sortBy=ctime".format(i))
        print("Finish - oke")
        sleep(random.uniform(5, 7))
        self.status = self.status + 1
    
    def loadMultiBrowsers(self, i):
        for driver in self.drivers:
            t = threading.Thread(target=self.loadPage, args = (driver,i,))
            t.start()
            print("Finish")
            i = i + 1

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
    
    def get_attribute_xpath(self,driver,xpath):
        text = []
        try:
            elements = driver.find_elements(By.XPATH,xpath) 
        except:
            print("Retry")
        for element in elements:
            text.append(element.get_attribute("textContent"))
        return text
    
    def get_detail_item(self,driver,link):
        driver.get(link)
        sleep(random.uniform(3, 5))
        Default_Price = self.get_attribute_text(driver,DEFAULT_PRICE_CLASS_NAME)       
        Promotional_Price = self.get_attribute_text(driver,PROMOTIONAL_PRICE_CLASS_NAME)
        Ratings_And_Num_Reviews = self.get_attribute_text(driver, NUM_REVIEWS_CLASS_NAME)
        Num_Sold = self.get_attribute_text(driver, NUM_SOLD_CLASS_NAME)
        # Num_Available_Div = driver.find_element(By.CLASS_NAME, NUM_AVAILABLE_DIV)
        # Num_Available_Inner = Num_Available_Div.find_element(By.XPATH,".//div[contains(text(), 'sản phẩm có sẵn')]")
        if not Ratings_And_Num_Reviews:
            Ratings_And_Num_Reviews.append("")
            Ratings_And_Num_Reviews.append("")
        if not Num_Sold:
            Num_Sold.append("")
        try:
            self.default_price.append(Default_Price) 
            self.promotional_price.append(Promotional_Price)
            self.rating.append(Ratings_And_Num_Reviews[0])
            self.num_reviews.append(Ratings_And_Num_Reviews[1])
            self.num_sold.append(Num_Sold[0])
        except:
            print("Empty,retry")
        # self.num_available.append(Num_Available_Inner.text)
        sleep(random.uniform(1, 2))
        
    def crawl(self,driver):
        sleep(random.uniform(3, 5))
        
        titles_page = self.get_attribute_text(driver,TITLE_CLASS_NAME)
        for title in titles_page:
            self.titles.append(title)
            
        links_page = self.get_attribute_link(driver,TITLE_LINK_CLASS_NAME)
        for link in links_page:
            self.links.append(link)
            sleep(random.uniform(2,3))
            self.get_detail_item(driver, link)
        
    def crawlParallel(self, func):
        for driver in self.drivers:  
           queue = Queue()
           print("-------Running parallel---------")
           t = threading.Thread(target=lambda q, arg1: q.put(func(arg1)), args=(queue, driver))
           t.start()
        
   
    def crawlParallelMutiplePages(self,func, n_pages):
       n = math.floor(n_pages/2)
       for i in range(0,n+1):
           self.loadMultiBrowsers(2*i)
           sleep(random.uniform(5, 7))
           oke = False
           while oke == False: 
               if (self.status == 2):
                   self.crawlParallel(func)
                   oke = True
                   self.status = 0
               else:
                   sleep(random.uniform(3, 5))
        
   
        
# def main():
n_threads = 2
shopee = Task1_Parallel_Collect(USERNAME, PASSWORD)
shopee.openMultiBrowsers(n_threads)
shopee.loadLoginMultiBrowsers()
sleep(random.uniform(25,30))

shopee.crawlParallelMutiplePages(shopee.crawl, 1)

titles = shopee.titles
links = shopee.links
default_price = shopee.default_price
promotional_price = shopee.promotional_price
rating = shopee.rating
num_reviews = shopee.num_reviews
num_sold = shopee.num_sold
num_available = shopee.num_available


# <codecell>
df = pd.DataFrame({'titles': titles, 'links': links, 'default price': \
                    default_price, 'promotional_price': promotional_price,'rating': rating,\
                    'num_reviews': num_reviews,'num_sold':num_sold })
df.to_csv('sample_1.csv',index=False,header=True,encoding="utf-8-sig")


# shopee_data.login(SHOPEE_LOGIN_URL)
# page_url = "https://shopee.vn/sp.btw2"
# df = shopee_data.crawl_multiple_pages(2,page_url)

