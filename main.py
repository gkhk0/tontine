import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()#'/home/erik/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://tontine.cash/');

#time.sleep(10) # Let the user actually see something!
time.sleep(7)
login_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[@class='stats-controls']/button")
print(login_button)
login_button.click()
body = driver.find_element(By.XPATH, '/html/body')

email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/input[1]")
password = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/input[2]")
login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[4]/div[2]/div/button")
email.send_keys("donkeygenitalia@gmail.com")
password.send_keys("1234")
login.click()




time.sleep(5)
#el = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[5]/div")
#person = None
#row = True
time.sleep(10)
#while row:
#map = []
#for i in range(1000):
#    map.append([])
#    for i in range(1000):
#        body.send_keys(Keys.LEFT)
#        if 'player-text' in el.get_attribute('class').split():
#            map[-1].append(1)
#            #if driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[5]/div/div[2]").get_attribute('innerText') == person:
#            #    row = False
#            #if person == None:
#            #    person = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[5]/div/div[2]").get_attribute('innerText')
#            print("onplayer")
#        elif 'move-text' in el.get_attribute('class').split():
#            map[-1].append(0)
#            print("notonplayer")
#        else:
#            for i in range(100):
#                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#    body.send_keys(Keys.UP)

#mapstring = ""
#for i in map:
#    for i2 in i:
#        mapstring = f"{mapstring}{i2}"
#    mapstring = f"{mapstring}\n"
#print(mapstring)

#driver.quit()
