


#Program to substract
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.refresh()
driver.find_element(By.NAME,"name").send_keys("Testing")
driver.find_element(By.ID,"exampleCheck1").click()