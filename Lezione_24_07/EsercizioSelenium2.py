"""Visita https://practicetestautomation.com/practice-test-login/
Effettua il login con username "student" e password "Password123"
Verifica che il login sia avvenuto con successo"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")


username = driver.find_element(By.ID, 'username')
username.send_keys('student')

pas = driver.find_element(By.ID, 'password')
pas.send_keys('Password123')

click= driver.find_element(By.ID, 'submit')
click.click()

try:
    successo=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/p[1]/strong")))
    print("Login effettuato")
except:
    print("login errato")

driver.quit()