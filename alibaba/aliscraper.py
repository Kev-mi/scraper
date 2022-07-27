import os
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import argparse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import pyautogui
BASE_URL = "https://www.amazon.com/Best-Sellers/zgbs"

def scraping_thread(website_url):
    driver_path = "C:chromedriver.exe"
    options = Options()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    driver.get(website_url)
    img_search = driver.find_element(By.CLASS_NAME, 'ui-searchbar-imgsearch-icon')
    img_search.click()
    input = driver.find_element(By.XPATH, "//input[@type='file']")
    driver.execute_script("arguments[0].style.display = 'block';", input)
    input.send_keys("C:\\Users\\kevin\\Desktop\\Python\\alibabascraper\\alibaba\\test1.jpg")
    #img_search_upload = driver.find_element(By.XPATH, '//*[@id="html5_1g8ta96e2qe41t14eqkirj1ugq3"]' )
    #img_search_upload = driver.find_element(By.ID, "html5_1g8ta96e2qe41t14eqkirj1ugq3")
    #img_search_upload = driver.find_element(By.CLASS_NAME, 'upload-btn')
    #img_search_upload.click()
    #time.sleep(1/4)
    #img_search_upload.send_keys(os.getcwd()+"/test1.jpg")
    #pyautogui.write("C:\\Users\\kevin\\Desktop\\Python\\alibabascraper\\alibaba\\test1.jpg")
    #pyautogui.press('enter')
    time.sleep(10)



