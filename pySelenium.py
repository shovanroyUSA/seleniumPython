from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to chromedriver
chromedriver_path = "C:\\Users\\shova\\Documents\\MSCS\\youtube-sele\\MyTutorial\\src\\drivers\\chromedriver.exe"
# Set up Chrome service
service = Service(executable_path=chromedriver_path)

# Initialize the Chrome driver with the service
driver = webdriver.Chrome(service=service)
# Navigate to Google
driver.get("https://www.google.com")

# Print the title of the webpage
print(driver.title)

# Find the search box using its class name, enter text, and submit the form
search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)  # Alternatively, you can use search_box.submit()

# Wait for 1 second to see the results
time.sleep(1)

# Close the browser
driver.close()
driver.quit()

# Firefox browser ############################################################
geckodriver_path = "C:\\Users\\shova\\Documents\\MSCS\\youtube-sele\\MyTutorial\\src\\drivers\\geckodriver.exe"
service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service)
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
print(driver.title)

# Find the search box using its class name, enter text, and submit the form
search_box = driver.find_element(By.NAME, "no_type")
if search_box.is_displayed():
    search_box.clear()
    search_box.send_keys("Selenium WebDriver")
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)  # Alternatively, you can use search_box.submit()

# Wait for 1 second to see the results
time.sleep(1)

driver.close()
driver.quit()

