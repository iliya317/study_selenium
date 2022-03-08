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
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser.get(link)
    link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций

    time.sleep(30)
    browser.quit()