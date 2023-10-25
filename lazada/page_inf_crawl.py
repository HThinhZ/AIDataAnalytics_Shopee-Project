import requests
import pandas as pd
import csv
import json
import re
import time

headers={
    'authority' :'www.lazada.vn',
    'accept' : 'application/json, text/plain, */*',
    'accept-language' : 'en-US,en;q=0.9,vi;q=0.8',
    'cookie' : '__wpkreporterwid_=53e5f64f-2c0c-46ce-b908-d658dd386f00; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; cto_bundle=-X54el9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDdkJ6UTBIJTJGd0gzMUlBTiUyRnJnbHVjYThqeDFkajk1QU1KMGJWeWlwaTVaTmlIdmNEMGJicWhMQlVaT3V6JTJCS1lYMFRpOXVacTBxWVdkTnBTZ0xYcUk2QWRmUUNNcWN0RWZSenNxT0RFd1dwSiUyRm9BZmklMkJDZE5lSkpWTzlzY2tpTzNXdzBJUUhwNEtSdUY0Q3NSVWRKUWl3VHBwcVhaNU1ITmNSOXk5JTJCMTRUJTJGc2FvTEtMVWhna201UmQwZTglMkJ4JTJGYzJBJTNEJTNE; xlly_s=1; _gid=GA1.2.1196349833.1698079719; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19654%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698684519%7C3%7CMCAAMB-1698684519%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698086919s%7CNONE%7CvVersion%7C5.2.0; _uetsid=03ec940071c411eea6d83b40abd648ab; _uetvid=bfc718e0126311eea8b10777b7e2fca8; _ga_3V5EYPLJ14=GS1.2.1698151148.8.1.1698151205.3.0.0; epssw=1*gwf611gAL1jZMAXMCv4ChVz8OJ2YT6vGwOvZI6RiLzE6Cn3Y7Pyg5j4oCj8LuODNtsNuBxRWH_9ASFFSH__5qKkC396VVKj5n7O66mjGj_9H6LsMbp6VDxd5H3DPKKYf-JFI7jA3fFmpEWomuuf3JQJBWyxQBkD-ezIJv4gJyLB4dLnnx8KLzaSEx5_UkELRy99-yaQganC3Pnh_sOeerz2peyx5e-yjxkmnyUQR; t_sid=8QlYibbweMvxgqkQEz8714QUILsZSngx; utm_channel=NA; _m_h5_tk=6aea5167ccc46f8b649715430b52dfc2_1698169428914; _m_h5_tk_enc=1018a575429436f4d490f4769d916888; x5sec=7b22617365727665722d6c617a6164613b33223a22307c434e2b6233366b47454e6951747645454967706a5958427a62476c6b5a5859794d502f4b6c3572342f2f2f2f2f77464141773d3d222c22733b32223a2262306232306162383364383333306461227d; isg=BL6-xFjbV16mo4I3uCkWgTaDD9QA_4J5pfzP8GjHKoH8C17l0I_SieTtg8_HanqR',
    'referer' :'https://www.lazada.vn/',
    'Postman-Token': 'fcbae239-7197-4bde-a38d-a0460aa8dc6c',
    "Host": 'www.lazada.vn',
    'Connection' : 'keep-alive',
    # 'Sec-Ch-Ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    # 'Sec-Ch-Ua-Mobile': '?0',
    # 'Sec-Ch-Ua-Platform':"Windows",
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-csrf-token' : '701f83e8e3e8e',
    'x-requested-with': 'XMLHttpRequest'
}

params = {
    'ajax' : 'true',
    'from' : 'wangpu',
    'isFirstRequest' : 'true',
    'langFlag' : 'vi',
    'page' : 1,
    'pageTypeId' : 2,
    'q' : 'All-Products'
}

if __name__=='__main__':
    with open('list_url.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("Shop: "+row[0])
            url  = "https://www.lazada.vn/" + row[0]
            response = requests.request("GET", url=url, params=params, headers=headers)
            if response.status_code != 200:
                exit

            res_json = response.json()
            mods = res_json["mods"]
            lisItems = mods["listItems"]

            # Duyệt qua các item
            lisItemsJson = []
            for item in lisItems: 
                # chuyển số lượt mua sang dạng số
                number = 0
                if "itemSoldCntShow" in item:
                    itemSoldCntShow = item["itemSoldCntShow"]
                    matches = re.search(r'(\d[\d,]+)|(\d)', itemSoldCntShow)
                    if matches:
                        # Lấy số từ kết quả tìm kiếm và loại bỏ dấu ","
                        number = int(matches.group(0).replace(',', ''))
                    else:
                        number = 0


                itemJson = {
                    "name" : item["name"],
                    "nid" : item["nid"],
                    "itemId" : item["itemId"],
                    "originalPrice" : int(item["originalPrice"]),
                    "price": int(item["price"]),
                    "discount" : item["discount"],
                    "ratingScore": item["ratingScore"],
                    "review" : item["review"],
                    "inStock" : item["inStock"],
                    "itemSoldCntShow" : number

                }
                lisItemsJson.append(itemJson)
            # Ghi vào file
            fileName = "./data/" + row[0] +".json"
            with open(fileName, "a", encoding="utf-8") as json_file:
                json.dump(lisItemsJson, json_file, ensure_ascii=False, indent=4)

            time.sleep(10)
            break
