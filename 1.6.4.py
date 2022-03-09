import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import re
import datetime as dt
from selenium.webdriver.common.by import By
import time
import math
service = ChromeService(executable_path='C:\\Users\\Илья\\.wdm\\drivers\\chromedriver\\win32\\97.0.4692.71\\chromedriver.exe')
browser = webdriver.Chrome(service=service)
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    element = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/button[3]")
    element.click()

finally:
    # закрываем браузер после всех манипуляций

    time.sleep(30)
    browser.quit()