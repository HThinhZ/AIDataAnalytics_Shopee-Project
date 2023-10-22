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
        titles, links = [], []
    
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
    
    def loadMultiPages(self,driver, n):
        # for driver in self.drivers:
        driver.maximize_window()
        self.login(driver,SHOPEE_LOGIN_URL)
        sleep(random.uniform(3, 5))
        driver.get("https://shopee.vn/sp.btw2?page={}&sortBy=ctime".format(n))
        sleep(random.uniform(5, 6))
            
    def loadMultiBrowsers(self, n):
        i = 0
        for driver in self.drivers:
            if i < n:
                t = threading.Thread(target=self.loadMultiPages, args = (driver,i,))
                t.start()
            i = i + 1
        
    def runInParallel(self, func):
        for driver in self.drivers:  
            queue = Queue()
            print("-------Running parallel---------")
            t1 = threading.Thread(target=lambda q, arg1: q.put(func(arg1)), args=(queue, driver))
            t1.start()
        try:    
            output = queue.get()
        except:
            output = [] 
    
        return output
    
    def setup(self): 
        proxydf = pd.read_csv('./proxylist.csv',header=None)
        proxies = proxydf.values.tolist()
        proxylist = [proxy for sublist in proxies for proxy in sublist]
        options = webdriver.EdgeOptions()
        proxy = random.choice(proxylist)
        options.add_argument(f'--proxy-server={proxy}')
        return options
        
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
        # self.driver.get(page_url)
        sleep(random.uniform(3, 5))
        
        titles = self.get_attribute_text(driver,TITLE_CLASS_NAME)
        links = self.get_attribute_link(driver,TITLE_LINK_CLASS_NAME)
        
        # detailed_items = []
        # for link in links: 
        #     detailed_items.append(self.get_detail_item(link))
        #     try:
        #         default_price = [item[0][0] for item in detailed_items]
        #         discount_price = [item[1][0] for item in detailed_items]
        #     except Exception as e:
        #         print("An error occurred:", str(e))
        
        # df = pd.DataFrame({'title': titles,'link': links})
        # df = pd.DataFrame(list(zip(titles,links,default_price,discount_price)),\
        #                   columns=['title','link','default_price','discount_price'])
        # return df
        # return [default_price,discount_price]
        return titles,links
    
    def crawl_multiple_pages(self,num_pages,pare_url):
        df = pd.DataFrame()
        
        for page in range(0,num_pages):
            url = page_url + "?page=" + str(page) + "&sortBy=ctime"
            df = pd.concat([df, self.crawl(url)], ignore_index=True)
            sleep(random.uniform(4, 5))
        
        return df
        
# def main():
n = 2
shopee = Task1_Collect(USERNAME, PASSWORD)
shopee.openMultiBrowsers(n)
shopee.loadMultiBrowsers(n)
sleep(20)

title_link = shopee.runInParallel(shopee.crawl)
print(title_link)

# shopee_data.login(SHOPEE_LOGIN_URL)
# page_url = "https://shopee.vn/sp.btw2"
# df = shopee_data.crawl_multiple_pages(2,page_url)
# df.to_csv('page.csv',index=False,header=True,encoding="utf-8-sig")

# driver = webdriver.Edge()

# # Open URL: 
# driver.get("https://shopee.vn/buyer/login")
# sleep(random.randint(3, 5))

# driver.find_element(By.NAME, "loginKey").send_keys("hoangthinh130322@gmail.com")
# sleep(1)
# driver.find_element(By.NAME, "password").send_keys("Thinhpro123456#")
# sleep(1)

# button_1= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button")
# button_1.click()
# sleep(8)


# titles = []
# for page in range(0,2):
#     page_url = "https://shopee.vn/sp.btw2?page=" + str(page) + "&sortBy=pop"
#     driver.get(page_url)
#     sleep(random.randint(3, 5))
    
#     button_2= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/a[2]/span")
#     button_2.click()
#     sleep(1)

#     # Find and extract the titles
#     title_elements = driver.find_elements(By.CSS_SELECTOR, ".NxFDlV")
    
#     for title in title_elements:
#         titles.append(title.get_attribute("textContent"))

import random

for i in range(0,5):
    print(random.uniform(1,2))
    
import numpy as np 
import pandas as pd
from selenium import webdriver
from time import sleep
import random 
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options



driver = webdriver.Edge()
link = "https://www.bing.com/"
driver.get(link)
driver.maximize_window()
search_word = ["điểm thi thpt 2023"]
list_title = []
list_link =  []
for word in search_word:
    search = driver.find_element(By.CSS_SELECTOR, ".sb_form_q")
    search.send_keys(word)
    sleep(random.uniform(1, 2))
    search.send_keys(Keys.ENTER)
    sleep(random.uniform(2, 4))
    

    # while i < 200: 
    #     i = i + 1
    #     driver.execute_script("window.scrollBy(0,1000)","")
    #     driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    #     try: 
    #         driver.find_element(By.XPATH,"/html/body/div[5]/div/div[10]/div/div[4]/div/div[3]/div[4]/a[1]/h3/div").click()
    #     except:
    #         pass
    # element_title = driver.find_elements(By.CSS_SELECTOR, ".b_topTitle")
    
    
    # parent_title = driver.find_elements(By.CSS_SELECTOR,".b_algo")
    # h2_elements = []
    # for parent in parent_title:
    #     h2_tag = parent.find_element(By.CSS_SELECTOR,"h2 [href]")
    #     h2_elements.append(h2_tag)
    # for element in h2_elements: 
    #     # element_title = driver.find_elements(By.XPATH, "/html/body/div[4]/main/ol/li[2]/div/h2/a")
    #     list_title.append(element.get_attribute("textContent"))
    #     list_link.append(element.get_attribute("href")) 
        
    i = 0
    while i < 100:
        i = i + 1
        parent_title = driver.find_elements(By.CSS_SELECTOR,".b_algo")
        h2_elements = []
        for parent in parent_title:
            h2_tag = parent.find_element(By.CSS_SELECTOR,"h2 [href]")
            h2_elements.append(h2_tag)
        for element in h2_elements: 
            # element_title = driver.find_elements(By.XPATH, "/html/body/div[4]/main/ol/li[2]/div/h2/a")
            list_title.append(element.get_attribute("textContent"))
            list_link.append(element.get_attribute("href")) 
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
        driver.find_element(By.CSS_SELECTOR, "li [title='Next page']").click()
        sleep(random.uniform(2, 3))
    #     i = i + 1
    #     element_title = driver.find_elements(By.CSS_SELECTOR, ".tpcn")
    #     element_link = driver.find_elements(By.CSS_SELECTOR, ".tilk [href]")
    #     for element in element_title: 
    #         list_title.append(element.text)
    #     for element in element_link:    
    #         list_link.append(element.get_attribute("href"))
        
    #     driver.find_element(By.CSS_SELECTOR,"[title='Next page']").click()
    #     sleep(random.uniform(3, 5))
    # <codecell>
    df = pd.DataFrame(list(zip(list_title,list_link)),\
                          columns=['title','link'])
    df = df.astype(str).apply(lambda x: x.str.encode('utf-8').str.decode('utf-8'))
    df.to_csv('test.csv',index=False,header=True,encoding='utf-8-sig')
    # sleep(random.uniform(1, 2))
    # try: 
    #     driver.find_element(By.CLASS_NAME,".GNJvt")
        
    # except: 
    #     print("")
    #
# <codecell>
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
        titles, links = [], []
    
    def openMultiBrowsers(self,n):
        for i in range(n):
            driver = webdriver.Edge()
            self.drivers.append(driver)
        return self.drivers
    
    def loadMultiPages(self, driver, n):
        driver.maximize_window()
        driver.get("https://shopee.vn/sp.btw2?page={}&sortBy=ctime".format(n))
        sleep(random.uniform(3, 5))
        self.login(SHOPEE_LOGIN_URL)
        sleep(random.uniform(5, 6))
        
    def runInParallel(self, func, drivers_rx):
        for driver in drivers_rx:  
            queue = Queue()
            print("-------Running parallel---------")
            t1 = threading.Thread(target=lambda q, arg1: q.put(func(arg1)), args=(queue, driver))
            t1.start()
        try:    
            output = queue.get()
        except:
            output = [] 
    
        return output
    
    def setup(self): 
        proxydf = pd.read_csv('./proxylist.csv',header=None)
        proxies = proxydf.values.tolist()
        proxylist = [proxy for sublist in proxies for proxy in sublist]
        options = webdriver.EdgeOptions()
        proxy = random.choice(proxylist)
        options.add_argument(f'--proxy-server={proxy}')
        return options


        
        
        
    def click_button(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
        sleep(random.uniform(1, 2))
    
    def login(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(random.uniform(3, 5))
        self.driver.find_element(By.NAME, "loginKey").send_keys(self.username)
        sleep(random.uniform(1, 2))
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        sleep(random.uniform(1, 2))
        self.click_button(LOGIN_BUTTON)
        
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
        # self.driver.get(page_url)
        sleep(random.uniform(3, 5))
        
        titles = self.get_attribute_text(driver,TITLE_CLASS_NAME)
        links = self.get_attribute_link(driver,TITLE_LINK_CLASS_NAME)
        
        # detailed_items = []
        # for link in links: 
        #     detailed_items.append(self.get_detail_item(link))
        #     try:
        #         default_price = [item[0][0] for item in detailed_items]
        #         discount_price = [item[1][0] for item in detailed_items]
        #     except Exception as e:
        #         print("An error occurred:", str(e))
        
        # df = pd.DataFrame({'title': titles,'link': links})
        # df = pd.DataFrame(list(zip(titles,links,default_price,discount_price)),\
        #                   columns=['title','link','default_price','discount_price'])
        # return df
        # return [default_price,discount_price]
        return titles,links
    
    def crawl_multiple_pages(self,num_pages,pare_url):
        df = pd.DataFrame()
        
        for page in range(0,num_pages):
            url = page_url + "?page=" + str(page) + "&sortBy=ctime"
            df = pd.concat([df, self.crawl(url)], ignore_index=True)
            sleep(random.uniform(4, 5))
        
        return df
        
# def main():
n = 2
shopee = Task1_Collect(USERNAME, PASSWORD)
drivers_shopee = shopee.openMultiBrowsers(n)
shopee.loadMultiPages(drivers_shopee, n)

title_link = shopee.runInParallel(shopee.crawl(), drivers_rx)
print(title_link)

# shopee_data.login(SHOPEE_LOGIN_URL)
# page_url = "https://shopee.vn/sp.btw2"
# df = shopee_data.crawl_multiple_pages(2,page_url)
# df.to_csv('page.csv',index=False,header=True,encoding="utf-8-sig")

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
        
        
        def loadMultiPages(self,driver, i):
            # for driver in self.drivers:
            driver.maximize_window()
            self.login(driver,SHOPEE_LOGIN_URL)
            sleep(random.uniform(3, 5))
            driver.get("https://shopee.vn/sp.btw2?page={}&sortBy=ctime".format(i))
            sleep(random.uniform(5, 6))
                
        def loadMultiBrowsers(self, n):
            i = 0
            for driver in self.drivers:
                if i < n:
                    t = threading.Thread(target=self.loadMultiPages, args = (driver,i,))
                    t.start()
                i = i + 1
            
        def runInParallel(self, func):
            for driver in self.drivers:  
                queue = Queue()
                print("-------Running parallel---------")
                t1 = threading.Thread(target=lambda q, arg1: q.put(func(arg1)), args=(queue, driver))
                t1.start()
            try:    
                output = queue.get()
            except:
                output = [] 
        
            return output
            
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
    shopee.loadMultiBrowsers(n)
    sleep(random.uniform(40,50))

    shopee.runInParallel(shopee.crawl)

    titles = shopee.titles
    links = shopee.links

    # shopee_data.login(SHOPEE_LOGIN_URL)
    # page_url = "https://shopee.vn/sp.btw2"
    # df = shopee_data.crawl_multiple_pages(2,page_url)
    # df.to_csv('page.csv',index=False,header=True,encoding="utf-8-sig")

# <codecell>
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


