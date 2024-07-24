"""Visita https://demoqa.com/dynamic-properties
Attendi che il bottone "Visible After 5 Seconds" appaia
Cliccalo e verifica che l'azione sia stata eseguita con successo"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
time.sleep(10)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "visibleAfter")))
try:
    oggetto = driver.find_element(By.ID, "visibleAfter")
    oggetto.click()
    print("Cliccato con successo")
except:
    print("Errore")

driver.quit()