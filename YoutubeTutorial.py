

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
import time
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/API")
driver.maximize_window()
websiteURL = driver.title
if "API - Wikipedia" in websiteURL:
    print("Yes,finally achieved")
else:
    print("Need to learn a lot")

driver.quit()