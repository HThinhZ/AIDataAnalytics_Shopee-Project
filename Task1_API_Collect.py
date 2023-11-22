from Collect_Settings import *
from Task2_Store import *
import requests
from tqdm import tqdm
import pandas as pd
import json
from time import sleep
import random
from datetime import datetime 

class Task1_API_Collect:
    def __init__(self):
        self.headers = headers
        
    def crawl(self,url):
        request = requests.get(url,headers=self.headers)
        raw_data = json.loads(request.content)
        data = raw_data['data']['sections'][0]['data']['item']
        df = pd.DataFrame(data)
        
        return df
    
    def crawl_shop_infor(self,shop_ids):
        all_shops = []
        for i in tqdm(range(0,len(shop_ids))):
            url = SHOPS_URL + str(shop_ids[i])
            request = requests.get(url,headers=headers)
            raw_data = json.loads(request.content)
            data = raw_data['data']
            all_shops.append(data)
            sleep(random.uniform(5,7))
        
        df = pd.DataFrame(all_shops)
        return df
            
    def store(self,df):
        try: 
            print("<===== Local database =====>\n")
            local_store_data = Task2_Local_Store()
            local_store_data.insert_data(df)

        except:
            print("\nError. Retry")
    
    def store_id(self,df):
        try: 
            print("<===== Local database Id=====>\n")
            local_store_data_id = Task2_Local_Store_Id()
            local_store_data_id.insert_data(df)

        except:
            print("\nError. Retry")
    
    def collect(self,shop_ids):
        local_store_data_id = Task2_Local_Store_Id()
        num_documents = local_store_data_id.num_documents
        print("Number of documents in the collection:", num_documents)
        for i in tqdm(range(0,len(shop_ids))):
            url = ITEMS_URL + str(shop_ids[i])
            df = self.crawl(url)
            Crawl_Time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_column_name = 'crawl_time'
            df[new_column_name] = Crawl_Time
            self.store(df)
            df['Crawl_id'] = df.index
            df['Crawl_id'] = df['Crawl_id'] + num_documents
            df.rename(columns={'Crawl_id': 'crawl_id'}, inplace=True)
            self.store_id(df)
            num_documents = num_documents + len(df)
            sleep(random.uniform(5,8))
    

shopee_full_data = Task1_API_Collect()
shopee_full_data.collect(top_shopee_mall_id)
shopee_full_data.collect(normal_shop_id)
# df = shopee_full_data.crawl_shop_infor(normal_shop_id)
# df.to_csv('Normal_Shops_Information.csv',index=False,header=True,encoding="utf-8-sig")