import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configure logging to suppress specific warnings/errors
logging.basicConfig(level=logging.INFO)  # Only show INFO and above

def retrieve_chollos():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Open Chrome in maximized mode
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--disable-notifications")  # Disable extensions
    chrome_options.add_argument("--log-level=3")  # Suppress logs
    chrome_options.add_argument("--no-default-browser-check")  # Disable the default browser check
    chrome_options.add_argument("--default-browser-check=no")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #DISABLE WHEN DEBUGGING
    # chrome_options.add_argument("--headless")  # Run in headless mode
    # Headless produce SSL errors, so I deactivated it.

    # Suppress SSL certificate errors
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.analiticafantasy.com/chollos-fantasy/fantasy-relevo")
    wait = WebDriverWait(driver, 20)  # 20 seconds timeout
    element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' css-y8g67k']"))
    )
    element.click()
    list_of_chollos = []
    for i in range(10):
        # Find all elements with the specified class name
        next_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.player-full__name.player-full__name--clickable")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});",
                              next_button)
        player_elements = driver.find_elements(By.CSS_SELECTOR, "p.player-full__name.player-full__name--clickable")
        # Extract the text from each element and store in a list
        list_of_chollos.extend([player.text for player in player_elements])
        time.sleep(0.2)
        next_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to next page']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});",
                              next_button)
        time.sleep(0.6)
        next_button.click()
        time.sleep(0.2)
    # Print the extracted player names
    driver.close()
    return list_of_chollos
