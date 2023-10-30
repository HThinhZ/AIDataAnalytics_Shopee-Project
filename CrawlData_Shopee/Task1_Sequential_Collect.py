# import libraries
from Settings import *
from Task2_Store import *
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
from tqdm import tqdm
from datetime import datetime
import os
import subprocess


list_df = []
# src code: 
class Task1_Sequential_Collect:
    # Init global variables:
       
    def __init__(self,Mall_id,Mall_name):
        # Declare browser:
        # options = uc.ChromeOptions() 
        # # options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
        # options.headless = False
        # self.driver = uc.Chrome(options)
        # self.driver.maximize_window()
        self.username = USERNAME
        self.password = PASSWORD
        # Declare varibles:
        self.Mall_id = Mall_id
        self.Mall_name = Mall_name
        self.n_pages = 0
        global mall_id, mall_name, titles, links, default_price, promotional_price, \
            num_reviews, rating, num_sold, num_available, num_like, detailed_product, crawl_time
        self.mall_id, self.mall_name, self.crawl_time,\
        self.titles, self.links, self.default_price, \
        self.promotional_price, self.num_reviews, \
        self.rating, self.num_sold, self.num_available,\
        self.num_like, self.detailed_product = [], [], [], [], [], [], [], [], [], [], [], [], []   
        self.retry = 0
    
    def reset_varibles(self):
        self.mall_id, self.mall_name, self.crawl_time,\
        self.titles, self.links, self.default_price, \
        self.promotional_price, self.num_reviews, \
        self.rating, self.num_sold, self.num_available,\
        self.num_like, self.detailed_product = [], [], [], [], [], [], [], [], [], [], [], [], []  
        
    def wait_time(self,driver):
        wait = WebDriverWait(driver, TIMEOUT)
        return wait
    
    def init_driver(self):
        # Declare browser:
         options = uc.ChromeOptions() 
         # options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
         options.headless = False
         driver = uc.Chrome(options)
         driver.maximize_window()
         
         return driver
     
    def login(self, driver, url):
        driver.get(url)
        while self.retry <= 2:
            try: 
                self.wait_time(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, WAIT_LOGIN_CLASS_NAME)))
                self.retry = 10
            except:
                print("=> Retry")
                driver.refresh()
                self.retry = self.retry + 1
        
        self.retry = 0
        sleep(random.uniform(3, 5))
        # self.driver.find_element(By.NAME, "loginKey").send_keys(self.username)
        Username = self.wait_time(driver).until(EC.visibility_of_element_located((By.NAME, "loginKey")))
        Username.send_keys(self.username)
        sleep(random.uniform(2, 3))
        Password = self.wait_time(driver).until(EC.visibility_of_element_located((By.NAME, "password")))
        Password.send_keys(self.password)
        sleep(random.uniform(2, 3))
        self.click_button(driver,LOGIN_BUTTON)
        print("Login successfully")
        
    def init_and_login(self):
        driver = self.init_driver()
        sleep(random.uniform(2, 3))
        self.login(driver, SHOPEE_LOGIN_URL)
        sleep(random.uniform(5, 7))
        
        return driver
    
    def click_button(self, driver,xpath):
        # self.driver.find_element(By.XPATH,xpath).click()
        Button = self.wait_time(driver).until(EC.element_to_be_clickable((By.XPATH,xpath)))
        Button.click()
        
    def get_attribute_text(self,driver,class_name):
        text = []
        # while self.retry <= 2:
        #     try:
        #         self.wait_time(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, class_name)))
        #         self.retry = 10
        #         # elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name)))
        #     except:
        #         print("Retry crawl text")
        #         driver.refresh()
        #         self.retry = self.retry + 1
            
        elements = driver.find_elements(By.CSS_SELECTOR,class_name)    
        self.retry = 0
        for element in elements:
            text.append(element.get_attribute("textContent"))
            print(element.text)

        return text
    
    def get_attribute_link(self,driver, class_name):
        link = []
        # while self.retry <= 2:
        #     try:
        #         self.wait_time(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, class_name)))
        #         # elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name)))
        #         self.retry = 10
        #     except:
        #         print("Retry crawl link")
        #         driver.refresh()
        #         self.retry = self.retry + 1
        
        elements = driver.find_elements(By.CSS_SELECTOR,class_name)
        self.retry = 0
        for element in elements:
            link.append(element.get_attribute('href'))
        return link
    
    def get_attribute_xpath(self,driver,xpath):
        text = []
        # while self.retry <= 2: 
        #     try:
        #         self.wait_time(driver).until(EC.presence_of_element_located((By.XPATH,xpath)))
        #         self.retry = 10
        #         # elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name)))
        #     except:
        #         print("Retry crawl xpath")
        #         driver.refresh()
        #         self.retry = self.retry + 1
        
        elements = driver.find_elements(By.XPATH,xpath) 
        self.retry = 0
        for element in elements:
            text.append(element.get_attribute("textContent"))
            print(element.text)
        return text
    
    def get_detail_item(self, driver, link):
        driver.get(link)
        while self.retry <= 2:
            try:
                self.wait_time(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, WAIT_CLASS_NAME)))
                self.retry = 10
            except:
                print("=> Retry")
                driver.refresh()
                self.retry = self.retry + 1
                
        self.retry = 0
        sleep(random.uniform(2,3))
        
        Title_Name = self.get_attribute_xpath(driver,TITLE_XPATH)
        Default_Price = self.get_attribute_text(driver,DEFAULT_PRICE_CLASS_NAME)       
        Promotional_Price = self.get_attribute_text(driver,PROMOTIONAL_PRICE_CLASS_NAME)
        Ratings_And_Num_Reviews = self.get_attribute_text(driver,NUM_REVIEWS_CLASS_NAME)
        Num_Sold = self.get_attribute_text(driver,NUM_SOLD_CLASS_NAME)
        Num_Available = self.get_attribute_text(driver,NUM_AVAILABLE_CLASS_NAME)
        Num_Like = self.get_attribute_text(driver,NUM_LIKE_CLASS_NAME)
        Current_Time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while self.retry <= 2:
            try:
                driver.execute_script("window.scrollBy(0,1200)","")
                self.wait_time(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, DETAILED_PRODUCT_CLASS_NAME)))
                self.retry = 10
                Detailed_Product_Div = driver.find_elements(By.CSS_SELECTOR, DETAILED_PRODUCT_CLASS_NAME)
            except:
                print("=> Retry")
                driver.refresh()
                self.retry = self.retry + 1
        
        self.retry = 0
        if not Default_Price:
            Default_Price.append("")
        if not Promotional_Price:
            Promotional_Price.append("")
        if not Ratings_And_Num_Reviews:
            Ratings_And_Num_Reviews.append("")
            Ratings_And_Num_Reviews.append("")
        if not Num_Sold:
            Num_Sold.append("")
        if not Num_Available:
            Num_Available.append("")
        if not Num_Like: 
            Num_Like.append("")
        try:
            self.titles.append(Title_Name[0])
            self.default_price.append(Default_Price[0]) 
            self.promotional_price.append(Promotional_Price[0])
            self.rating.append(Ratings_And_Num_Reviews[0])
            self.num_reviews.append(Ratings_And_Num_Reviews[1])
            self.num_sold.append(Num_Sold[0])
            self.num_available.append(Num_Available[0])
            self.num_like.append(Num_Like[0])
            self.crawl_time.append(Current_Time)
            Detailed_Product = {}
            list_header = []
            list_content = []
            for Div in  Detailed_Product_Div:
                header = Div.find_element(By.CSS_SELECTOR,HEADER_CLASS_NAME)
                list_header.append(header.text)
                contents = Div.find_elements(By.CSS_SELECTOR, CONTENTS_CLASS_NAME)
                list_content.append(contents[0].text)
            i = 0
            for header in list_header:
                Detailed_Product[header] = list_content[i]
                i = i + 1
            print(Detailed_Product)
            self.detailed_product.append(Detailed_Product)
        except:
            print("Empty,retry")
            Detailed_Product = {}
            self.detailed_product.append(Detailed_Product)
        # self.num_available.append(Num_Available_Inner.text)
        sleep(random.uniform(1, 2))
        
    def crawl(self, driver, url):
        driver.get(url)
        while self.retry <= 2:
            try:
                self.wait_time(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, TITLE_LINK_CLASS_NAME)))
                self.retry = 10
            except:
                print("=> Retry")
                driver.refresh()
                self.retry = self.retry + 1
                
        self.retry = 0
        links_page = self.get_attribute_link(driver, TITLE_LINK_CLASS_NAME)
        print("<==== Crawl detailed item ====>")
        for link in tqdm(links_page):
            self.mall_id.append(self.Mall_id)
            self.mall_name.append(self.Mall_name)
            self.links.append(link)
            self.get_detail_item(driver,link)
        
        
    def update(self,link):
        pass
    
    def crawl_multiple_pages(self):
        mall_pages = MALL_URL + str(self.Mall_id)
        print(mall_pages)
        driver = self.init_and_login()
        driver.get(mall_pages)
        while self.retry <= 2:
            try:
                self.wait_time(driver).until(EC.presence_of_element_located((By.CSS_SELECTOR, TOTAL_PAGE_CLASS_NAME)))
                self.retry = 10
            except:
                print("=> Retry")
                driver.refresh()
                self.retry = self.retry + 1
                
        self.retry = 0
        sleep(random.uniform(3, 5))        
        n_pages = driver.find_element(By.CSS_SELECTOR, TOTAL_PAGE_CLASS_NAME).text
        print("Num pages: {}".format(n_pages))
        
        driver.quit()
        # Completely terminate processing in memory
        if os.name == 'nt':  
            # subprocess.run('taskkill /F /IM chromedriver.exe /T', check=True, shell=True)
            try:
                subprocess.run('taskkill /F /IM chrome.exe /T', check=True, shell=True)
            except:
                print("Shuted down")
        
        for page in range(7,int(n_pages)):
            print("====== Page {} ======".format(page + 1))
            driver = self.init_and_login()
            page_url = mall_pages + "?page=" + str(page) + "&sortBy=ctime"
            self.crawl(driver, page_url)
            driver.quit()
            df = pd.DataFrame({'crawl_time': self.crawl_time, 'mall_id': self.mall_id, 'mall_name': self.mall_name,'titles': self.titles,\
                            'links': self.links,'default price': self.default_price, 'promotional_price': self.promotional_price,\
                            'rating': self.rating,'num_reviews': self.num_reviews,'num_sold':self.num_sold ,\
                            'num_available': self.num_available, 'num_like': self.num_like, 'detrailed_product': self.detailed_product})
            list_df.append(df)
            
            # try:
            #     print("<===== Local database =====>\n")
            #     local_store_data = Task2_Local_Store()
            #     local_store_data.insert_data(df)
            # except:
            #     print("\nError. Retry")
            try: 
                print("<===== Remote database =====>\n")
                remote_store_data = Task2_Remote_Store()
                remote_store_data.insert_data(df)
            except:
                print("\nError. Retry")
            sleep(random.uniform(3,5))
            self.reset_varibles()
            # Completely terminate processing in memory
            if os.name == 'nt':  
                # subprocess.run('taskkill /F /IM chromedriver.exe /T', check=True, shell=True)
                try:
                    subprocess.run('taskkill /F /IM chrome.exe /T', check=True, shell=True)
                except:
                    print("Shuted down")

            sleep(random.uniform(7,10))
        
            
    # def crawl_multiple_pages(self,num_pages,pare_url):
    #     for page in range(0,num_pages):
    #         url = page_url + "?page=" + str(page) + "&sortBy=ctime"
   

# def crawl_multiple_pages(mall,n_pages):
#     pass
    
# def main():
shopee = Task1_Sequential_Collect("levents.vn","Levents .vn")
shopee.crawl_multiple_pages()


# mall_id = shopee.mall_id
# mall_name = shopee.mall_name
# titles = shopee.titles
# links = shopee.links
# default_price = shopee.default_price
# promotional_price = shopee.promotional_price
# rating = shopee.rating
# num_reviews = shopee.num_reviews
# num_sold = shopee.num_sold
# num_available = shopee.num_available
# num_like = shopee.num_like
# detailed_product = shopee.detailed_product

# # <codecell>
# initial_df = pd.read_csv('sample1.csv')
# additional_df = list_test_df[0]
# # additional_df = pd.DataFrame({'mall_id': mall_id, 'mall_name': mall_name,'titles': titles,\
# #                 'links': links,'default price': default_price, 'promotional_price': promotional_price,\
# #                 'rating': rating,'num_reviews': num_reviews,'num_sold':num_sold ,\
# #                 'num_available':num_available, 'num_like': num_like, 'detrailed_product': detailed_product})
# df = pd.concat([initial_df,additional_df], ignore_index=True)
# df.to_csv('sample.csv',index=False,header=True,encoding="utf-8-sig")

# # <codecell>

# local_store_data = Task2_Local_Store()
# for df in list_df:
#     local_store_data.insert_data(df)



