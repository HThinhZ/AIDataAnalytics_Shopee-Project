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