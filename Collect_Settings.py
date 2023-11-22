# Top shopee mall
# top_shopee_mall_username = ['sp.btw2', 'poloman.vn', 'tsla.store', 'coolmate.vn', '5s_official', 'rough.vn', 'patternvn', 'levents.vn', 'guzado.vn', 'thoitrangmando', 'tsimple_official', 'owen.fashion', 'thoitrangbiluxury', 'feaer_store', 'sukiyafashion.vn', '4menstores', 'haidang.fashion', 'thoitrangnam4u', 'thoitrangeverest', 'kojibavn', 'hara.vn', 'sges.clothing', 'aremishop_2020']
# top_shopee_mall_name = ['Aviano Menswear', 'HAPPYHOW', 'TSLA Store Quần áo legging nam', '\x08Coolmate - Official Store', '5S OFFICIAL', 'ROUGH', 'Pattern', 'Levents .vn', 'Guzado Official', 'Thời Trang MANDO', 'TSIMPLE_OFFICIAL', 'Thời trang nam Owen', 'Biluxury Official', 'FEAER STORE PREMIUM', 'SUKIYA OFFICAL STORE', '4MEN_OFFICIAL ', 'haidang.fashion', '4U SHOP', 'THỜI TRANG EVEREST', 'Kojiba Việt Nam', 'Balo HARAS VietNam', 'SGES.Unisex', 'AREMI']
top_shopee_mall_id = [40342563, 225909574, 68613764, 24710134, 127217331, 60297616, 111639450,\
                      317477677, 201774917, 59596762, 168678363, 92937520, 68988783, 263713672,\
                      38038824, 277366270, 70677296, 1620236, 17893078, 31522834, 16649961,\
                      296132807, 257412160]
normal_shop_id = [999122826, 952153869, 47401874, 80968732,744060250,127049276,324062232,205125399,\
                  427693365, 360972139, 168195778, 913496573, 299977840, 183199642, 416018485,\
                  264542552, 78461361, 329002439, 108136164, 75123404]

# Headers 
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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
}

# Url  
SHOPS_URL = 'https://shopee.vn/api/v4/product/get_shop_info?shopid='
ITEMS_URL = "https://shopee.vn/api/v4/recommend/recommend?bundle=shop_page_product_tab_main&limit=99999&offset=0&shopid="
