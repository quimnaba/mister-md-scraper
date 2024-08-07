import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open Chrome in maximized mode
chrome_options.add_argument("--disable-infobars")  # Disable infobars
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-notifications")  # Disable extensions

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.analiticafantasy.com/chollos-fantasy/fantasy-relevo")
wait = WebDriverWait(driver, 10)  # 2 seconds timeout
time.sleep(0.2)
driver.find_element(By.CSS_SELECTOR, "button[class=' css-y8g67k']").click()

#Retrieve names
#list_of_chollos = driver.find_elements(By.CLASS_NAME, "player-full__name player-full__name--clickable").get_attribute()
def retrieve_chollos():
    list_of_chollos = []
    for i in range (10):
        # Find all elements with the specified class name
        player_elements = driver.find_elements(By.CLASS_NAME, "player-full__name")
        # Extract the text from each element and store in a list
        list_of_chollos.extend([player.text for player in player_elements])
        time.sleep(0.2)
        next_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Go to next page']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", next_button)
        time.sleep(0.6)
        next_button.click()
        time.sleep(0.2)
    # Print the extracted player names
    return list_of_chollos