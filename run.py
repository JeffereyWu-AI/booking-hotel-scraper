from booking.booking import Booking

bot = Booking()
bot.land_first_page()
bot.change_language(language="en-us")
bot.enter_place_to_go(place_to_go="Yinchuan, Ningxia, China")
bot.select_dates(check_in_date="2025-04-03", 
                 check_out_date="2025-04-04")
bot.select_guests(adult_counts=1)
bot.click_search()  
bot.apply_filtrations(star_values=[3,4,5], sorter_type="Price (lowest first)")
bot.deal_report()


input("Press Enter to close the browser...")