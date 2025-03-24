# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from selenium.webdriver.common.by import By

class BookingReport():
    def __init__(self, hotel_boxes):
        self.deal_boxes = hotel_boxes

    def pull_deal_box_attributes(self):
        collection = []
         # 在循环外检查哪种方法可用
        method_1_flag = len(self.deal_boxes[0].find_elements(By.CSS_SELECTOR, 'div[class="b3f3c831be"]')) > 0
        method_2_flag = len(self.deal_boxes[0].find_elements(By.CSS_SELECTOR, 'div[class="d8c86a593f"] div[aria-label]')) > 0

        for index, deal_box in enumerate(self.deal_boxes):
            # Pulling the hotel name
            hotel_name = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text
            print(f'{index+1}. {hotel_name}')

            hotel_price = deal_box.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').text
            print(f'Price: {hotel_price}')

            if method_1_flag:
                rating_squares = deal_box.find_element(By.CSS_SELECTOR, 'div[class="b3f3c831be"]')
                hotel_rating = rating_squares.get_attribute('aria-label').split()[0]
            elif method_2_flag:
                rating_squares = deal_box.find_element(By.CSS_SELECTOR, 'div[class="d8c86a593f"] div[aria-label]')
                hotel_rating = rating_squares.get_attribute('aria-label').split()[0]
            else:
                hotel_rating = 'N/A'

            print(f'Rating: {hotel_rating}')

            try:
                hotel_score = deal_box.find_element(By.CSS_SELECTOR, 'div[class="a3b8729ab1 d86cee9b25"]').text.split()[-1]
            except:
                hotel_score = 'N/A'
            print(f'Score: {hotel_score}')
            print()

            collection.append([hotel_name, hotel_price, hotel_rating, hotel_score])
        return collection
