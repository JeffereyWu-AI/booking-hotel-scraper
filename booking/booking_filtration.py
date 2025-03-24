# This file will include a class with instance methods.
# That will be responsible to interact with our website.
# After we have some results, we apply filtration.
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time



class BookingFiltration():
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def apply_star_rating(self, star_values):
        try:
            star_filtration_box = self.driver.find_element(
                By.CSS_SELECTOR,
                'div[data-filters-group="class"]')
            for star_value in star_values:
                star_element = star_filtration_box.find_element(
                    By.CSS_SELECTOR, 
                    f'div[data-filters-item="class:class={star_value}"]')
                star_element.click()
            time.sleep(1)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")

    def apply_sorters(self, sorter_type):
        try:
            sorter_box = self.driver.find_element(
                By.CSS_SELECTOR, 
                'button[data-testid="sorters-dropdown-trigger"]')
            sorter_box.click()
            sorter_element = self.driver.find_element(
                By.CSS_SELECTOR, 
                f'button[aria-label="{sorter_type}"]')
            sorter_element.click()
            time.sleep(1)
        except(NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")
        
