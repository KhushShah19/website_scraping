
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import random
from urllib.request import urlretrieve

class FreepikScraper:
    def __init__(self, url='https://www.freepik.com/'):
        service = Service('C:/Users/2me41/Downloads/chromedriver_win32(3)/chromedriver.exe')

        self.driver = webdriver.Chrome(service=service)
        self.driver.get(url)
        sleep(random.uniform(4, 7))
        try:
            cookie = self.driver.find_element(By.CSS_SELECTOR, '[id="onetrust-accept-btn-handler"]')
            cookie.click()
        except:
            pass

    def Search(self, to_search_for):
        self.to_search_for = to_search_for
        search_value = self.driver.find_element(By.CSS_SELECTOR, '[id="search-value-fake"]')
        search_button = self.driver.find_element(By.CSS_SELECTOR, '[class="button button--lg button--white button--icon"]')
        search_value.send_keys(self.to_search_for)
        sleep(random.uniform(1, 3))
        search_button.click()
        sleep(random.uniform(2, 4))

    def Get_img_list(self):
        img_list = self.driver.find_elements(By.CSS_SELECTOR, 'a.showcase__link > img')
        self.img_list = [i.get_attribute('src') for i in img_list]
        return self.img_list

    def Download_img(self,  img_list=None, file_path=None):
        
        if img_list == None:
            img_list = self.img_list
        if file_path == None:
            file_path= 'C:/Users/2me41/Saved_games/mockup_images'
            
        # Create a directory to save the images (if doesn't exist)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        for i, url in enumerate(img_list):
            urlretrieve(url, f"{file_path}/{self.to_search_for}_{i}.jpg")

    def Multi_page1(self):
        next_button = 'button[class="pagination__next button button--xs button--icon"]'
        total_pages = self.driver.find_element(By.CSS_SELECTOR, 'span[class="pagination__pages"]')
        total_pages = total_pages.text
        total_pages = int(total_pages)
        j = 0
        for i in range(int(total_pages)):
            j += i
            img_list = self.get_img_list
            self.download_img(img_list)

            # in the end go to next page
            self.driver.find_element(By.CSS_SELECTOR, next_button).click()
            sleep(random.uniform(1, 3))

        return  'All img downloaded.'

    def Multi_page(self):
        next_button = 'button[class="pagination__next button button--xs button--icon"]'
        total_pages = self.driver.find_element(By.CSS_SELECTOR, 'span[class="pagination__pages"]')
        total_pages = total_pages.text
        total_pages = int(total_pages)
        
        for i in range(total_pages):
            img_list = self.get_img_list()
            self.download_img(self, img_list)

            # in the end go to next page
            self.driver.find_element(By.CSS_SELECTOR, next_button).click()
            sleep(random.uniform(1, 3))

        return  'All img downloaded.'
