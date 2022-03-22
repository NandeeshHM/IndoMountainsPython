
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

ser = Service("C:\\selenium broweser drivers\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service = ser)
driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
WebTitle = driver.title
driver.maximize_window()
driver.find_element(By.NAME,"txtUsername").send_keys("Nandeesh")
#driver.quit()