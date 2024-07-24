"""Uno script per visitare Wikipedia, cerca "Python (programming language)"
e stampare il primo paragrafo della pagina risultante."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://it.wikipedia.org/wiki/Pagina_principale")
cerca = driver.find_element(By.NAME, "search")
cerca.send_keys("Python (programming language)" + Keys.RETURN)
testo=driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[3]/div[4]/ul/li[1]/div/div[2]/div[2]")
print(testo.text)
driver.quit()