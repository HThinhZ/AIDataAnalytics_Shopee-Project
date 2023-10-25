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
from tqdm import tqdm

# src code: 
class Task1_Sequential_Collect:
    # Init global variables:
       
    def __init__(self,username,password):
        # Declare browser:
        options = uc.ChromeOptions() 
        # options.add_argument(r"--user-data-dir=C:\Users\ADMIN\AppData\Local\Google\Chrome\User Data")
        options.headless = False
        self.driver = uc.Chrome(options)
        self.driver.maximize_window()
        self.username = username
        self.password = password
        # Wait until TIMEOUT
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        # Declare varibles:
        global mall_id, mall_name, titles, links, default_price, promotional_price, \
            num_reviews, rating, num_sold, num_available, num_like, detailed_product
        self.mall_id, self.mall_name,\
        self.titles, self.links, self.default_price, \
        self.promotional_price, self.num_reviews, \
        self.rating, self.num_sold, self.num_available,\
        self.num_like, self.detailed_product = [], [], [], [], [], [], [], [], [], [], [], []
    
    def login(self,url):
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        sleep(random.uniform(1, 2))
        # self.driver.find_element(By.NAME, "loginKey").send_keys(self.username)
        Username = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginKey")))
        Username.send_keys(self.username)
        sleep(random.uniform(2, 3))
        Password = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        Password.send_keys(self.password)
        sleep(random.uniform(2, 3))
        self.click_button(LOGIN_BUTTON)
        print("Login successfully")
    
    def click_button(self,xpath):
        # self.driver.find_element(By.XPATH,xpath).click()
        Button = self.wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        Button.click()
        
    def get_attribute_text(self,class_name):
        text = []
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR,class_name)
            # elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name)))
        except:
            print("Retry")
        for element in elements:
            text.append(element.get_attribute("textContent"))

        return text
    
    def get_attribute_link(self, class_name):
        link = []
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR,class_name)
            # elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name)))
        except: 
            print("Retry")
        for element in elements:
            link.append(element.get_attribute('href'))
        return link
    
    def get_attribute_xpath(self,xpath):
        text = []
        try:
            elements = self.driver.find_elements(By.XPATH,xpath) 
            # elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, class_name)))
        except:
            print("Retry")
        for element in elements:
            text.append(element.get_attribute("textContent"))
        return text
    
    def get_detail_item(self,link):
        self.driver.get(link)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, WAIT_CLASS_NAME)))
        sleep(random.uniform(2,3))
        
        Default_Price = self.get_attribute_text(DEFAULT_PRICE_CLASS_NAME)       
        Promotional_Price = self.get_attribute_text(PROMOTIONAL_PRICE_CLASS_NAME)
        Ratings_And_Num_Reviews = self.get_attribute_text(NUM_REVIEWS_CLASS_NAME)
        Num_Sold = self.get_attribute_text(NUM_SOLD_CLASS_NAME)
        Num_Available = self.get_attribute_xpath(NUM_AVAILABLE_XPATH)
        Num_Like = self.get_attribute_text(NUM_LIKE_CLASS_NAME)
        try:
            self.driver.execute_script("window.scrollBy(0,1200)","")
            sleep(random.uniform(1,3))
            Detailed_Product_Div = self.driver.find_elements(By.CSS_SELECTOR, DETAILED_PRODUCT_CLASS_NAME)
        except:
            print("Error, retry")
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
            self.default_price.append(Default_Price[0]) 
            self.promotional_price.append(Promotional_Price[0])
            self.rating.append(Ratings_And_Num_Reviews[0])
            self.num_reviews.append(Ratings_And_Num_Reviews[1])
            self.num_sold.append(Num_Sold[0])
            self.num_available.append(Num_Available[0])
            self.num_like.append(Num_Like[0])
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
            self.detailed_product.append(Detailed_Product)
        except:
            print("Empty,retry")
        # self.num_available.append(Num_Available_Inner.text)
        sleep(random.uniform(1, 2))
        
    def crawl(self,url):
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, TITLE_CLASS_NAME)))
        
        sleep(random.uniform(3, 5))
        titles_page = self.get_attribute_text(TITLE_CLASS_NAME)
        for title in titles_page:
            self.mall_id.append("sp.btw2")
            self.mall_name.append("Aviano Menswear")
            self.titles.append(title)
            
        links_page = self.get_attribute_link(TITLE_LINK_CLASS_NAME)
        for link in tqdm(links_page):
            self.links.append(link)
            self.get_detail_item(link)
    
    # def crawl_multiple_pages(self,num_pages,pare_url):
    #     for page in range(0,num_pages):
    #         url = page_url + "?page=" + str(page) + "&sortBy=ctime"
   

def crawl_multiple_pages(mall,n_pages):
    pass
    
# def main():

shopee = Task1_Sequential_Collect(USERNAME, PASSWORD)
shopee.login(SHOPEE_LOGIN_URL)
sleep(random.uniform(3, 5))
shopee.crawl("https://shopee.vn/sp.btw2?page=6&sortBy=ctime")


mall_id = shopee.mall_id
mall_name = shopee.mall_name
titles = shopee.titles
links = shopee.links
default_price = shopee.default_price
promotional_price = shopee.promotional_price
rating = shopee.rating
num_reviews = shopee.num_reviews
num_sold = shopee.num_sold
num_available = shopee.num_available
num_like = shopee.num_like
detailed_product = shopee.detailed_product

# <codecell>
initial_df = pd.read_csv('sample_6.csv')
additional_df = pd.DataFrame({'mall_id': mall_id, 'mall_name': mall_name,'titles': titles,\
                'links': links,'default price': default_price, 'promotional_price': promotional_price,\
                'rating': rating,'num_reviews': num_reviews,'num_sold':num_sold ,\
                'num_available':num_available, 'num_like': num_like, 'detrailed_product': detailed_product})
df = pd.concat([initial_df,additional_df], ignore_index=True)
df.to_csv('sample_7.csv',index=False,header=True,encoding="utf-8-sig")




