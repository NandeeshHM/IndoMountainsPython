

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(Path)
Verify = driver.find_elements(By.XPATH,'Submit').click()
assert 'Submit' in Verify
print("Button is available")


