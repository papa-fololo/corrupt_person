from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

os.environ['PATH'] += ":/home/user/chrome-linux64/chrome"
driver = webdriver.Chrome()
driver.maximize_window()

# get the google_docs page
URL = ("https://docs.google.com/forms/d/e/1FAIpQLSeOXMDQ09jupP0RsqgQaer74C_Wi_BrFLJLj30HG-ZxAf3Bkw/viewform?usp"
       "=send_form")
driver.get(URL)
time.sleep(3)

reasons_list = ["He is corrupt ,he stole from the Kimwarer dam project",
                "he is very corrupt ,he steals money and hides in churches",
                "he is very corrupt ,he steals money and hides in churches",
                "He is corrupt ,he stole from the Kimwarer dam project"]

for reason in reasons_list:
    person_input = driver.find_element(by=By.XPATH, value="//div/input[contains(@type,'text')]")
    reason_input = driver.find_element(by=By.XPATH, value="//div/textarea")
    submit_button = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Submit')]")
    person_input.click()
    person_input.send_keys("William Ruto")

    reason_input.click()
    reason_input.send_keys(reason)

    submit_button.click()

    # we are on the next page ,
    # click submit another response
    while True:
        try:
            submit_again_button = driver.find_element(by=By.XPATH, value="//div/a[contains(text(),'Submit')]")
            submit_again_button.click()
            break
        except NoSuchElementException:
            time.sleep(2)

