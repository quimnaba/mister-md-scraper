import PrivateData as pvdata
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def getPlayersCurrentMister():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Open Chrome in maximized mode
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--disable-notifications")  # Disable extensions
    # Headless doesnt work with mister for unknown reasons

    # ENTER TO MISTER
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://mister.mundodeportivo.com/market")

    wait = WebDriverWait(driver, 20)
    red_button = wait.until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
    red_button.click()
    time.sleep(0.2)

    for i in range(4):
        accept = driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--primary")
        time.sleep(0.2)
        accept.click()
        time.sleep(0.2)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn--capsule.btn--plain")))
    set_email = driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--plain")
    set_email.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#email")))
    write_email = driver.find_element(By.CSS_SELECTOR, "#email")
    write_email.send_keys(pvdata.user_email)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--primary").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[2]/div/form/div[2]/input")))
    pwd_mister = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div/form/div[2]/input")
    pwd_mister.send_keys(pvdata.pwd)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--primary").click()
    time.sleep(0.4)
    # TODO: Investigate why driver.get takes so long. Maybe remove next wait until.
    driver.get("https://mister.mundodeportivo.com/market")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "timer")))

    # Extract player names that have no owner
    # Find all <a> elements with data-title inside <li> elements with data-owner="0"
    player_elements = driver.find_elements(By.XPATH, '//li[@data-owner="0"]//a[@data-title]')

    # Extract the data-title attributes into a list
    player_names = [player.get_attribute("data-title") for player in player_elements]
    driver.close()
    # Print the extracted player names
    return player_names
