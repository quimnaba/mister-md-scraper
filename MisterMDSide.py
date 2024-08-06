import time
from selenium.webdriver.support import wait
import PrivateData as pvdata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def loginToPage(driver: webdriver, wait: wait):
    set_email = driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--plain")
    set_email.click()

    time.sleep(0.2)
    write_email = driver.find_element(By.CSS_SELECTOR, "#email")
    write_email.send_keys(pvdata.user_email)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--primary").click()
    time.sleep(1)
    pwd_mister = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div/form/div[2]/input")
    pwd_mister.send_keys(pvdata.pwd)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn--capsule.btn--primary").click()
    time.sleep(0.4)
    # wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "navbar-switch-tab")))
    # TODO: Investigate why driver.get takes so long. Maybe remove next wait until.
    driver.get("https://mister.mundodeportivo.com/market")
    wait.until(EC.presence_of_element_located((By.ID, "btn-filter-market")))
    # TODO: Check if the next lines can be removed as the filter is only visual
    driver.find_element(By.ID, "btn-filter-market").click()
    time.sleep(0.2)
    driver.find_element(By.XPATH, "//*[@id='filters-market']/div[3]/div[2]/label[2]").click()
    driver.find_element(By.ID, "btn-filters-market-apply").click()


def getPlayersCurrentMister(driver):
    # Extract player names that have no owner
    # Find all <a> elements with data-title inside <li> elements with data-owner="0"
    player_elements = driver.find_elements(By.XPATH, '//li[@data-owner="0"]//a[@data-title]')

    # Extract the data-title attributes into a list
    player_names = [player.get_attribute("data-title") for player in player_elements]

    # Print the extracted player names
    print(player_names)
