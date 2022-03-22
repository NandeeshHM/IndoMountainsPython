import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


ser= Service("C:\\selenium broweser drivers\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=ser)
driver.get('https://opensource-demo.orangehrmlive.com/')
myCurrentLocation = driver.current_url
driver.maximize_window()
print(driver.title)
print("My Current location is : " + myCurrentLocation)

driver.find_element(By.NAME,'txtUsername').send_keys("admin")
driver.find_element(By.NAME,'txtPassword').send_keys("admin123")
driver.find_element(By.NAME,'Submit').click()
driver.find_element(By.CSS_SELECTOR,"a[id='welcome']").click()
driver.find_element(By.XPATH,"//a[@href='/index.php/auth/logout']").click()
time.sleep(3)
#driver.find_element(By.XPATH,"//img[@src='/webres_622c1bfeebcab0.03534043/orangehrmLeavePlugin/images/MyLeave.png']").click()
#driver.find_element(By.XPATH,"//input[@id='leaveList_chkSearchFilter_3']").click()

#driver.find_element(By.XPATH,"//input[@name='btnSave']").click()
#driver.quit()