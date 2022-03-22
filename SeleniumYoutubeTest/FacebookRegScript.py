from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

ser=Service("C:\\selenium broweser drivers\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=ser)
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'Forgotten password?').click()
driver.find_element(By.ID,'identify_email').send_keys('9480187713')
driver.find_element(By.XPATH,"//button[@value='1']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//button[@value='1']").click()

time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='_9o1v']").click()
time.sleep(5)
'''
driver.find_element(By.NAME,'reset_action').click()
'''
