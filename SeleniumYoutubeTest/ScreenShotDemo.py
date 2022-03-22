from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.hdfc.com/")
driver.maximize_window()
driver.get_screenshot_as_file("HomeLoanWebPage2.apng")
driver.get_screenshot_as_file("HomeLoanWebPage3.avif")
driver.get_screenshot_as_file("HomeLoanwenPage4.gif")
driver.get_screenshot_as_file("HomeLoanWebPage5.jpeg")
driver.get_screenshot_as_file("HomeLoanwebPage6.png")
driver.get_screenshot_as_file("HomeLoanWebPage7.svg")
driver.get_screenshot_as_file("HomeLoanWebPage8.webp")
driver.quit()


