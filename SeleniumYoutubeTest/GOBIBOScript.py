from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import cmath

mySer = Service('C:\\selenium broweser drivers\\edgedriver_win64\\msedgedriver.exe')
driver = webdriver.Edge(service= mySer)
driver.get("https://www.goibibo.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@class = 'sc-GEbAx kenSRj']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//span[@class ='sc-kfPuZi dprjVP fswDownArrow']").click()
driver.find_element(By.XPATH,"//p[text()='25']").click()
driver.find_element(By.XPATH,"//p[text()='28']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Done']").click()