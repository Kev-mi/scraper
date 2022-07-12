import amazon.websites as websites
import os
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import amazon.websites as websites


#options = Options()
#options.add_argument("--headless")
#self.driver =webdriver.Chrome
#(options=options)


class Engine_thread_1(webdriver.Chrome(executable_path=ChromeDriverManager(version='102.0.5005.27').install(), chrome_options=r"C:\chromedriver.exe")):
    def __init__(self, driver_path=r"C:\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Engine_thread_1, self).__init__()
        self.driver.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def scraping_thread_1(self, website_url, amazon_category, thread_nr):
        self.get(website_url)
        category_selected = self.find_element(By.LINK_TEXT, f'{amazon_category}')
        category_selected.click()
        time.sleep(10)
        current_url = self.current_url
        self.get(current_url[:-1] + thread_nr)
        for bsr_rank in range(0, 50):
            link_selected = self.find_element(By.XPATH, f'//*[@id="p13n-asin-index-{bsr_rank}"]')
            link_selected.click()
            self.back()

    def add_extension(self, extension_path):
        options = Options()
        options.add_extension(extension_path)
        # webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)
        self.get("http://stackoverflow.com")
        time.sleep(10)


    class Engine_thread_2(webdriver.Chrome):
        def __init__(self, driver_path=r"C:\chromedriver.exe", teardown=False):
            self.driver_path = driver_path
            self.teardown = teardown
            os.environ["PATH"] += self.driver_path
            super(Engine_thread_2, self).__init__()
            self.implicitly_wait(15)

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.teardown:
                self.quit()

        def scraping_thread_2(self, website_url, amazon_category, thread_nr):
            self.get(website_url)
            category_selected = self.find_element(By.LINK_TEXT, f'{amazon_category}')
            category_selected.click()
            current_url = self.current_url
            self.get(current_url[:-5] + f"pg_{thread_nr}?_encoding=UTF8&pg={thread_nr}")
            for bsr_rank in range(0, 50):
                link_selected = self.find_element(By.XPATH, f'//*[@id="p13n-asin-index-{bsr_rank}"]')
                link_selected.click()
                self.back()






