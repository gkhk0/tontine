import os
os.system("install-pkg firefox")
os.system("install-pkg java-jdk")

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


password=""
email=""


driver = webdriver.Firefox('/home/runner/tontine-2/dir/geckodriver')#'/home/erik/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://tontine.cash/');

#time.sleep(10) # Let the user actually see something!
time.sleep(7)
login_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[@class='stats-controls']/button")
print(login_button)
login_button.click()
body = driver.find_element(By.XPATH, '/html/body')

email_filed = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/input[1]")
password_filed = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/input[2]")
login_submit = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/button")
email_filed.send_keys(email)
password_filed.send_keys(password)
login_submit.click()

time.sleep(5)

alive = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/button")
if driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/button/div").get_attribute('inner_text').replace("\n", "").replace(" ", "") == "stayalive":
	alive.click()

time.sleep(20)

driver.quit()
