from amazon.scraper import *
import amazon.websites as websites
import time
import threading


def thread_1():
    category_list = ["Amazon Devices & Accessories"]
    category = category_list[0]
    scraping_thread_1(websites.BASE_URL, category, "1")
    #scraping_thread_1(websites.BASE_URL, category, "1")
            #threading.Thread(target=bot.scraping_thread_1, args=(websites.BASE_URL, category, "1", )).start()
            #threading.Thread(target=bot.scraping_thread_2, args=(websites.BASE_URL, category, "2", )).start()


def main():
    threading.Thread(target=thread_1).start()


if __name__ == '__main__':
    main()


