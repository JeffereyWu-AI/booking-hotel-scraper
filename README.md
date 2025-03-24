# Booking Automation with Selenium

This project automates the process of searching for hotels on a booking website using Selenium. It allows users to specify search criteria such as location, dates, number of guests, and filters (e.g., star ratings and sorting by price). The search results are then extracted and saved to an Excel file for further analysis.

## Features

- **Language Selection**: Automatically changes the website language to the specified option (e.g., `en-us` for US English).
- **Location Search**: Searches for hotels in a specified location (e.g., "Yinchuan, Ningxia, China").
- **Date Selection**: Allows users to specify check-in and check-out dates.
- **Guest Configuration**: Configures the number of adults for the booking.
- **Filters**: Applies star rating filters and sorts results by price (lowest first).
- **Report Generation**: Extracts hotel details (name, price, rating, and score) and saves them to an Excel file.

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **Selenium**: Install Selenium using pip:
   ```bash
   pip install selenium
   ```
3. **Pandas**: Install pandas for Excel file generation:
   ```bash
   pip install pandas openpyxl
   ```
4. **ChromeDriver**: Download the ChromeDriver executable compatible with your Chrome version from [ChromeDriver](https://sites.google.com/chromium.org/driver/). Ensure the executable is added to your system's PATH or specify its location in the code.

## Project Structure

The project consists of the following files:

- **`booking.py`**: Contains the main `Booking` class with methods for automating the booking website.
- **`booking_report.py`**: Contains the `BookingReport` class for extracting and processing hotel data.
- **`run.py`**: The main script to execute the automation process.
- **`hotel_report.xlsx`**: The output Excel file containing the extracted hotel data.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JeffereyWu-AI/booking-hotel-scraper.git
   cd booking-hotel-scraper
   ```

2. **Run the Script**:
   Execute the `run.py` script to start the automation process:
   ```bash
   python run.py
   ```

3. **View the Results**:
   After the script completes, the extracted hotel data will be saved in `hotel_report.xlsx`.

## Customization

You can customize the search criteria by modifying the parameters in `run.py`:

- **Location**: Change the `place_to_go` parameter.
- **Dates**: Modify the `check_in_date` and `check_out_date` parameters.
- **Guests**: Adjust the `adult_counts` parameter.
- **Filters**: Update the `star_values` and `sorter_type` parameters.

## Example

Here’s an example of how to search for hotels in Yinchuan, Ningxia, China, for a stay from April 3, 2025, to April 4, 2025, with 1 adult:

```python
bot = Booking()
bot.land_first_page()
bot.change_language(language="en-us")
bot.enter_place_to_go(place_to_go="Yinchuan, Ningxia, China")
bot.select_dates(check_in_date="2025-04-03", check_out_date="2025-04-04")
bot.select_guests(adult_counts=1)
bot.click_search()
bot.apply_filtrations(star_values=[3, 4, 5], sorter_type="Price (lowest first)")
bot.deal_report()
input("Press Enter to close the browser...")
```

## Notes

- Ensure the ChromeDriver executable is compatible with your installed version of Chrome.
- The script uses implicit waits to handle dynamic content loading. Adjust the wait times if necessary.


 
