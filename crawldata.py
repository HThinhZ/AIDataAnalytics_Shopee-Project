import requests
import hashlib

def encrypt_SHA256(password):
   sha_signature = \
      hashlib.sha256((hashlib.md5(password.encode()).hexdigest()).encode()).hexdigest()
   return sha_signature

class login():
 
   
   def __init__(self) -> None:
      self.s = requests.session()
      payload = {
         'email' : "hoangthinh130322@gmail.com",
         'password': encrypt_SHA256("Thinhpro123456#"),
         'support_ivs': 'true'
      }
      headers = {
         'Accept': 'application/json',
         'Accept-Language': 'en-US,en;q=0.9',
         'Content-Type': 'application/json',
         'Sec-Ch-Ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
         'Sec-Ch-Ua-Mobile': '?0',
         'Sec-Ch-Ua-Platform': "Windows",
         'Sec-Fetch-Dest': 'empty',
         'Sec-Fetch-Mode': 'cors',
         'Sec-Fetch-Site': 'same-origin',
         'X-Api-Source': 'pc',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
              Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
      }
      self.s.headers.update(headers)
      login_in = self.s.post('https://shopee.vn/api/v4/account/login_by_password',data=payload,timeout=10)
      
      # url = "https://shopee.vn/api/v4/shop/get_shop_base?entry_point=&need_cancel_rate=true&request_source=shop_home_page&username=sp.btw2&version=1"
      # re_1 = self.s.get(url,headers=headers)
      # print(re_1.content)


ttc = login()
