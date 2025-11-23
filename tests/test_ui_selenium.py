# Simple Selenium example (requires chromedriver and a running app)
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

def test_ui_create_account():
    driver = webdriver.Chrome()  # ensure chromedriver on PATH
    try:
        driver.get(BASE_URL + '/create-account')
        driver.find_element(By.NAME, 'name').send_keys('Selenium User')
        driver.find_element(By.NAME, 'email').send_keys('sel.user@example.com')
        driver.find_element(By.NAME, 'initial_deposit').send_keys('50')
        driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        time.sleep(1)
        assert 'Account created' in driver.page_source or driver.current_url.endswith('/accounts')
    finally:
        driver.quit()
