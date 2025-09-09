# seatwork 2
from pyscript import display

restaurant_name = 'SugarTooth'  # string
owner_name = 'Owner: Marie'  # string
year_established = 'Since 2001'  # string

popular_item = ['Oreo Cheesecake', 'Blackberry Pie', 'Black Forest Cake']  # list
popular_item_price = 19.39  # float

product_name1 = 'Blueberry Cheesecake'  # string
menu_price1 = 22.45  # float

product_name2 = 'Yema Cheesecake'  # string
menu_price2 = 21.25  # float

product_name3 = 'Chocolate Cheesecake'  # string
menu_price3 = 15.65  # float

product_name4 = 'Cheesecake'  # string
menu_price4 = 19.45  # float 


business_hours = 'Open: 11:30 AM to 10:30 PM'  # string
has_delivery = True  # boolean


# restaurant details for display
display(f'{restaurant_name}', target='div1')
display(f'{owner_name}', target='div2')
display(f'{year_established}', target='div2')


# products for display
display(f'{popular_item[0]}', target='popular_product')
display(f'{popular_item_price}', target='popular_price')

display(f'{product_name1}', target='product_1')
display(f'{menu_price1}', target='price_1')

display(f'{product_name2}', target='product_2')
display(f'{menu_price2}', target='price_2')

display(f'{product_name3}', target='product_3')
display(f'{menu_price3}', target='price_3')

display(f'{product_name4}', target='product_4')
display(f'{menu_price4}', target='price_4')


# buisness hours for display

display(f'{business_hours}', target='div3')
