import os
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import argparse

# ROI

#def save():
    #os.environ["webdriver.chrome.driver"] = executable_path
    #options = webdriver.ChromeOptions()
    #options.add_argument("headless")
    #options.add_extension(extension)


def add_plugin(executable_path):
    extension = 'C:/0.9.39_0.crx'
    options = Options()
    options.headless = True
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(ChromeDriverManger().install(), options=options)
    print("test")
    print("test2")
    return driver


def scraping_thread_1(website_url, amazon_category, thread_nr):
    driver_path = "C:\chromedriver.exe"
    driver = add_plugin(driver_path)
    driver.implicitly_wait(10)
    driver.get(website_url)
    category_selected = driver.find_element(By.LINK_TEXT, f'{amazon_category}')
    category_selected.click()
    current_url = driver.current_url
    driver.get(current_url[:-1] + thread_nr)
    for bsr_rank in range(0, 50):
        link_selected = driver.find_element(By.XPATH, f'//*[@id="p13n-asin-index-{bsr_rank}"]')
        link_selected.click()
        driver.back()
