    def crawl_multiple_pages(self,num_pages,pare_url):
        list_data = []
        self.driver.get(page_url)
        sleep(random.uniform(3, 5))
        self.click_button(ALL_PRODUCTS_BUTTON)
        
        for page in range(0,num_pages):
            list_data.append(self.crawl(TITLE_CLASS_NAME))
            self.click_button(NEXT_PAGE_BUTTON)
            sleep(random.uniform(3, 5))
            
        return list_data
    
    def setup(self): 
        proxydf = pd.read_csv('./proxylist.csv',header=None)
        proxies = proxydf.values.tolist()
        proxylist = [proxy for sublist in proxies for proxy in sublist]
        options = webdriver.EdgeOptions()
        proxy = random.choice(proxylist)
        options.add_argument(f'--proxy-server={proxy}')
        return options