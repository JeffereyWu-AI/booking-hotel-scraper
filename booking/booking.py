import booking.constants as const
import os
import time
import pandas as pd
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"Your driver path"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def close_dialog(self):
        try:
            close_button = WebDriverWait(self, 0.01).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'))
        )
            # 点击关闭按钮
            close_button.click()
            print("Dialog closed successfully.")
        except (NoSuchElementException, TimeoutException):
            print("Dialog not found, skipping close action.")

    def land_first_page(self):
        self.get(const.BASE_URL)
    def change_language(self, language=None):
        try:
            # 等待元素出现
            language_element = WebDriverWait(self, 15).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, 
                    'button[data-testid="header-language-picker-trigger"]'))
            )
            language_element.click()

            selected_language_element = self.find_element(By.CSS_SELECTOR, f'button[lang="{language}"]')
            selected_language_element.click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")

    def enter_place_to_go(self, place_to_go):
        self.place_to_go = place_to_go
        try:
            # 等待输入框出现
            search_field = WebDriverWait(self, 15).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, 
                    'input[placeholder="Where are you going?"]'))
            )
            search_field.clear()
            search_field.send_keys(self.place_to_go)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")

    def select_dates(self, check_in_date, check_out_date):
        try:
            # 找到日期选择框
            date_element = self.find_element(
                By.CSS_SELECTOR, 
                "div[data-testid='searchbox-dates-container']"
            )
            date_element.click()
            check_in_date_element = self.find_element(
                By.CSS_SELECTOR, 
                f'span[data-date="{check_in_date}"]'
            )
            check_in_date_element.click()
            check_out_date_element = self.find_element(
                By.CSS_SELECTOR, 
                f'span[data-date="{check_out_date}"]'
            )
            check_out_date_element.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")

    def select_guests(self, adult_counts=None):
        try:
            # 点击客人配置按钮
            guests_element = self.find_element(
                By.CSS_SELECTOR, "button[data-testid='occupancy-config']"
            )
            guests_element.click()

            # 等待成人数量输入框出现
            adult_field = WebDriverWait(self, 15).until(
                EC.presence_of_element_located((By.ID, "group_adults"))
            )

            # 获取当前值
            adult_value = int(adult_field.get_attribute("value"))

            if adult_counts is not None:
                # 找到增加和减少按钮
                decrease_button = self.find_element(By.XPATH, '//input[@id="group_adults"]/following-sibling::div/button[1]')
                increase_button = self.find_element(By.XPATH, '//input[@id="group_adults"]/following-sibling::div/button[2]')

                # 根据目标值点击按钮
                if adult_counts > adult_value:
                    diff = adult_counts - adult_value
                    for _ in range(diff):
                        increase_button.click()
                        time.sleep(0.1)  # 等待按钮点击生效
                elif adult_counts < adult_value:
                    diff = adult_value - adult_counts
                    for _ in range(diff):
                        decrease_button.click()
                        time.sleep(0.1)  # 等待按钮点击生效

                # 验证值是否更新
                adult_value = self.find_element(By.ID, "group_adults").get_attribute("value")
            
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")

    def click_search(self):
        try:
            self.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            # self.close_dialog()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")

    def apply_filtrations(self, star_values, sorter_type):
        filtration = BookingFiltration(driver=self)
        filtration.apply_sorters(sorter_type)
        filtration.apply_star_rating(star_values)
        # self.close_dialog()

    def deal_report(self, output_file="_hotel_report.xlsx"):
        try:
            hotel_boxes = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
            # print(f"Found {len(hotel_boxes)} hotel boxes.")
            report = BookingReport(hotel_boxes)
            result = report.pull_deal_box_attributes()

            # 将结果转换为 DataFrame
            df = pd.DataFrame(result, columns=["Hotel Name", "Price", "Rating (out of 5)", "Score"])
            # 保存为 Excel 文件
            output_file_full_name = self.place_to_go + "_hotel_report.xlsx"
            df.to_excel(output_file_full_name, index=True)
            print(f"Report saved to {output_file_full_name}")

            # table = PrettyTable(
            #     field_names=["Hotel Name", "Price", "Rating (out of 5)", "Score"]
            # )
            # table.add_rows(result)
            # print("Deal Report:")
            # print(table)

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")