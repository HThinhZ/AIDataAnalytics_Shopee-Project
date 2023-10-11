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

# src code: 
class Task1_Collect:
    
    def setup(self): 
        proxydf = pd.read_csv('./proxylist.csv',header=None)
        proxies = proxydf.values.tolist()
        proxylist = [proxy for sublist in proxies for proxy in sublist]
        options = webdriver.EdgeOptions()
        proxy = random.choice(proxylist)
        options.add_argument(f'--proxy-server={proxy}')
        return options

    def __init__(self,username,password):
        # Declare browser:
        self.driver = webdriver.Edge()
        self.username = username
        self.password = password
        
    def click_button(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
        sleep(random.uniform(1, 2))
    
    def login(self,url):
        self.driver.get(url)
        sleep(random.uniform(3, 5))
        self.driver.find_element(By.NAME, "loginKey").send_keys(self.username)
        sleep(random.uniform(1, 2))
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        sleep(random.uniform(1, 2))
        self.click_button(LOGIN_BUTTON)
        
    def get_attribute_text(self,class_name):
        text = []
        elements = self.driver.find_elements(By.CSS_SELECTOR,class_name)
        for element in elements:
            text.append(element.get_attribute("textContent"))
        return text
    
    def get_attribute_link(self, class_name):
        link = []
        elements = self.driver.find_elements(By.CSS_SELECTOR,class_name)
        for element in elements:
            link.append(element.get_attribute('href'))
        return link
    
    def get_detail_item(self,link):
        self.driver.get(link)
        sleep(random.uniform(3, 5))
        
        default_price = self.get_attribute_text(DEFAULT_PRICE_CLASS_NAME)
        discount_price = self.get_attribute_text(DISCOUNT_PRICE_CLASS_NAME)
        
        return (default_price,discount_price)
    
    def crawl(self,page_url):
        self.driver.get(page_url)
        sleep(random.uniform(3, 5))
        
        titles = self.get_attribute_text(TITLE_CLASS_NAME)
        links = self.get_attribute_link(TITLE_LINK_CLASS_NAME)
        
        detailed_items = []
        for i in range(0,4): 
            detailed_items.append(self.get_detail_item(links[i]))
        
        default_price = [item[0][0] for item in detailed_items]
        discount_price = [item[1][0] for item in detailed_items]
            
        # df = pd.DataFrame(list(zip(titles,links,default_price,discount_price)),\
        #                   columns=['title','link','default_price','discount_price'])
        # return df
        return [default_price,discount_price]
    
    def crawl_multiple_pages(self,num_pages,pare_url):
        list_data = []
        
        for page in range(0,num_pages):
            url = page_url + "?page=" + str(page) + "&sortBy=ctime"
            list_data.append(self.crawl(url))
            sleep(random.uniform(3, 5))
        
        return list_data
        
# def main():
shopee_data = Task1_Collect(USERNAME, PASSWORD)
shopee_data.login(SHOPEE_LOGIN_URL)
page_url = "https://shopee.vn/sp.btw2"
df = shopee_data.crawl_multiple_pages(1,page_url)
print(df)


# if __name__ == "__main__":
#     main()