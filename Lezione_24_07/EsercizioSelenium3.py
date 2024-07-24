"""Visita https://www.w3schools.com/html/html_tables.asp
Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")

elemento=driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[3]/div")

dati=elemento.find_element(By.TAG_NAME, "tr")
#dati=list(dati)

#print(type(dati))

informazioni=[]



for riga in dati:
    celle = riga.find_elements(By.TAG_NAME, "td")
    for cella in celle:
        informazioni.append(cella.text)

    
print(informazioni)

driver.quit()