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
    elements = browser.find_elements(By.CSS_SELECTOR, ".first_block [type='text']")
    for element in elements:
        element.send_keys("Мой")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # закрываем браузер после всех манипуляций

    time.sleep(30)
    browser.quit()