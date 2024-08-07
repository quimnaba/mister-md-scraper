from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import MisterMDSide as mister
import AnaliticasFantasy as af


chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open Chrome in maximized mode
chrome_options.add_argument("--disable-infobars")  # Disable infobars
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-notifications")  # Disable extensions

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://mister.mundodeportivo.com/market")

#Accepto cookies i dono 4 cops a continuar
# Wait until the red button is present and clickable, use the text or CSS selector
wait = WebDriverWait(driver, 10)  # 2 seconds timeout
red_button = driver.find_element(By.ID, "didomi-notice-agree-button")
red_button.click()
time.sleep(0.2)

for i in range(4):
    accept = driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--primary")
    time.sleep(0.2)
    accept.click()
    time.sleep(0.2)

#Login to market page
mister.loginToPage(driver, wait)
in_market = mister.getPlayersCurrentMister(driver)
list_of_chollos = af.retrieve_chollos()


