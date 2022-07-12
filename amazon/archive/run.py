from booking.booking import *
import booking.websites as websites
import time
import threading
from selenium.webdriver.chrome.options import Options

def webscrape(page):
    with Engine() as bot:
        # bot.add_extension("C:/0.9.39_0.crx")
        category_list = ["Amazon Devices & Accessories", "Amazon Launchpad", "Apps & Games"]
        for category in category_list:
            for x in range(0, 3):
                bot.open_page(websites.BASE_URL)
                bot.category_select(category, x)


def thread_1():
    category_list = ["Amazon Devices & Accessories"]
    category = category_list[0]
    with Engine_thread_1() as bot:
        bot.scraping_thread_1(websites.BASE_URL, category, "1")
            #threading.Thread(target=bot.scraping_thread_1, args=(websites.BASE_URL, category, "1", )).start()
            #threading.Thread(target=bot.scraping_thread_2, args=(websites.BASE_URL, category, "2", )).start()


def main():
    #option = Options()
    #option.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='104.0.5112.29').install()), options=option)
    threading.main_thread(target=thread_1(), args=( )).start()


if __name__ == '__main__':
    main()


