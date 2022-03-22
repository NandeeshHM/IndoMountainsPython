from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

my_ser = Service("C:\\selenium broweser drivers\\edgedriver_win64\\msedgedriver.exe")
driver = webdriver.edge(my_ser)
driver.get('https://opensource-demo.orangehrmlive.com/')
