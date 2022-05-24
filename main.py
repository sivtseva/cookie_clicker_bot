from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_driver_path = r"C:\Users\sivts\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")

game_is_on = True

store = driver.find_element(by=By.ID, value="store")
store_goods = store.find_elements(by=By.CLASS_NAME, value="grayed")
item_price_dict = {}

for n in range(len(store_goods)-1):
    txt = store_goods[n].text
    list_of_item_and_price = txt.split("\n")[0].split("-")
    name = list_of_item_and_price[0].strip()
    price = int(list_of_item_and_price[1].strip().replace(",", ""))
    item_price_dict[name] = price
items_to_buy = []
item_to_buy = ''
timeout = 300 #seconds i.e 5 minutes
time_start = time.time()

while time.time() < time_start + timeout:
    cookie.click()
    if (time.time() - time_start) % 5 == 0:
        money = int(driver.find_element(by=By.ID, value="money").text)
        for element in item_price_dict:
            if item_price_dict[element] < money:
                item_to_buy = element
        buy_item = driver.find_element(by=By.ID, value=f"buy{item_to_buy}").click()






