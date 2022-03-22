from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time

ser= Service("C:\\selenium broweser drivers\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=ser)
driver.get('https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads')