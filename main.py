from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_drive_path = your chromedrivr path
ser = Service(chrome_drive_path)
driver = webdriver.Chrome(service=ser, options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3533239256&geoId=106187582&keywords=web%20devlopment&location=Delhi%2C%20India&refresh=true")
signin = driver.find_element(By.LINK_TEXT, "Sign in")
signin.click()

time.sleep(5)


def log_in():
    username = input("Write your username")
    password = input("write your password")
    emailfeild = driver.find_element(By.ID, "username")
    emailfeild.send_keys(username)

    passwordfeild = driver.find_element(By.ID, "password")
    passwordfeild.send_keys(password)
    time.sleep(2)
    sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in_button.click()

    time.sleep(5)


def save_job():
    save_elements = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
    for job in save_elements:
        job.click()
        driver.execute_script("arguments[0].scrollIntoView();", job)
        time.sleep(3)

        try:
            saved = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
            if saved.is_enabled():
                saved.click()

        except NoSuchElementException:
            print('No save button, skipped.')
            continue

log_in()
save_job()
