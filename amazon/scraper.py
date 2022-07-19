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
    options = Options()
    option.add_extension("testing.crx")
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManger().install(), options=options)
    return driver


def scraping_thread_1(website_url, amazon_category, thread_nr):
    # driver path for windows below
    #driver_path = "C:\chromedriver.exe"
    driver = add_plugin(driver_path)
    driver.implicitly_wait(10)
    driver.get(website_url)
    category_selected = driver.find_element(By.LINK_TEXT, f'{amazon_category}')
    category_selected.click()
    current_url = driver.current_url
    driver.get(current_url[:-1] + thread_nr)
    for bsr_rank in range(0, 50):
        current_url = driver.current_url
        link_selected = driver.find_element(By.XPATH, f'//*[@id="p13n-asin-index-{bsr_rank}"]')
        link_selected.click()
        try:
            link_selected_2 = driver.find_element(By.XPATH, '//*[@id="scxt-stock-btn"]')
            link_selected_2.click()
            print("start3")
            driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="scxt-widget"]/iframe'))
            #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="scxt-widget"]/iframe')))
            time.sleep(5)
            testing = driver.find_element(By.CLASS_NAME, "counts-total").text
            print(testing)
        except NoSuchElementException:
            print("Not in stock")
            driver.get(current_url)
        except ElementNotInteractableException:
            print("this crashes the program")
            print(current_url)
            driver.get(current_url)
        driver.get(current_url)
        #driver.switch_to.parent_frame()
        #driver.switch_to.default_content()
        #driver.back()
            
