import scrapy
from shoppe_crawl.items import ShoppeCrawlItem
from scrapy_splash import SplashRequest 
import base64


lua_script = """
function main(splash, args)
    splash:init_cookies(splash.args.cookies)
    -- Mở trang web đăng nhập
    splash:go(args.url)

    -- Đợi cho trang web tải xong
    splash:wait(1)

    -- Tìm và nhập email
    local email_input = splash:select("input[name=loginKey]")
    email_input:send_keys("0336548815")

    -- Tìm và nhập password
    local password_input = splash:select("input[type=password]")
    password_input:send_keys("Hoaihcb1*")

    -- Chờ một chút cho dữ liệu được gửi đi
    splash:wait(2)

    -- Bấm nút đăng nhập (nếu có)
    local login_button = splash:select("#main > div > div.vtexOX > div > div > div > div:nth-child(2) > form > div > div.yXry6s > button")
    login_button:mouse_click()

    -- Chờ cho đến khi đăng nhập hoàn thành (hoặc đợi trang web chuyển hướng)
    splash:wait(3)

    -- Lấy nội dung của trang sau khi đăng nhập thành công
    local page_content = splash:html()

    -- Trả về kết quả cho Splash
    return {
        html=splash:html(),
        url = splash:url(),
        cookies = splash:get_cookies(),
    }
    -- Các kết quả khác mà bạn muốn trả về
end
"""

lua_script2 = """
function main(splash, args)
    -- Mở trang web đăng nhập
    splash:go(args.url)

    -- Đợi cho trang web tải xong
    splash:wait(5)

    local screenshot = splash:png()

    -- Trả về kết quả cho Splash
    return {
        screenshot = screenshot,
    }
end
"""

class ShoppeSpider(scrapy.Spider):
    name = 'shoppe'

    def start_requests(self):
        url = 'https://shopee.vn/buyer/login'
        yield SplashRequest(url, 
                            callback=self.parse,
                            endpoint='execute',
                            args={'wait': 2, 'lua_source': lua_script, 
                                  url: 'https://shopee.vn/buyer/login',
                                }
            )

    def parse(self, response):
        cookies_dict = {cookie['name']: cookie['value'] for cookie in response.data['cookies']}
        url_list = ['https://shopee.vn']
        for url in url_list:
            yield SplashRequest(url=url,  
                                callback=self.parse1, 
                                endpoint='execute', 
                                cookies=cookies_dict,
                                args={
                                    'wait': 1,
                                    'lua_source': lua_script2,
            })
    
    def parse1(self, response):
        screenshot = response.data['screenshot']

        # Lưu bản chụp màn hình vào một tệp hoặc làm bất kỳ điều gì khác
        with open('screenshot.png', 'wb') as f:
            f.write(screenshot)