from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pickle



cookie_file = "cookie.data"

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)
def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:/chromedriver.exe"
# x = os.system("chrome.exe --remote-debugging-port=9222 --user-data-dir=\"C:/selenum/ChromeProfile\"")
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
title = driver.title

print(title)
driver.get("https://google.com")
# input("Sign in and press enter")
# save_cookie(driver,cookie_file)
load_cookie(driver,cookie_file)
print("saved")







# driver.get("https://accounts.google.com/login")
