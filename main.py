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


service = ChromeService(executable_path='C:\\Users\\Илья\\.wdm\\drivers\\chromedriver\\win32\\97.0.4692.71\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

