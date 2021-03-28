from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
#https://selenium-python.readthedocs.io/installation.html


try:
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://dailyhealth.rit.edu/")
    username = "cel8473"
    password = "Lgst6575!@#"

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "j_username")))
    print("Entering Username")
    element.clear()
    element.send_keys(username)
    
    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "j_password")))
    print("Entering Password")
    element.clear()
    element.send_keys(password)

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "_eventId_proceed")))
    print("Click Log In")
    element.click()

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "I agree. Let's Start.")))
    print("Click I agree")
    element.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div')))
    element.click()
    print("Click NO")
    time.sleep(5)
except selenium.common.exceptions.SessionNotCreatedException:
    print("The driver is out of date, the link is in the comments")
    #https://chromedriver.storage.googleapis.com/LATEST_RELEASE
    input("Press Enter to Continue")
except:
    driver.quit()

f = open("checkup-dates.txt",'a')
today = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print(today)
f.write("\nCheckup Complete on : " + today)
f.close

driver.quit()
