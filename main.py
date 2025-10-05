from pyscript import display, window

# business details
restaurant_name = "Vaughn's Fast Food Place"  # String - Business name
owner_name = "Vaughn Repolona"                # String - Owner's name
year_established = 1950                       # Integer - Year business started

# featured item
popular_item_price = 199.99                   # Float - Price of most popular item

# delivery availability
has_delivery = True                           # Boolean - True = Available False = Not available

# menu and products
product_names = ["Burger", "Pasta", "Fries", "Steak", "Pizza"]  # List - Product names

# operating hours
business_hours = {"open": "9:00 AM", "close": "10:00 PM"}       # Dict - Opening and closing times

# Menu with Prices
menu_prices = {
    "Burger": 199.99,
    "Pasta": 249.50,
    "Fries": 89.00,
    "Steak": 599.00,
    "Pizza": 399.75
}

# common allergens
common_allergens = ["Peanuts", "Dairy", "Gluten"]

# tax rate
tax_rate = 0.08


# display's 

# Display top info
display(restaurant_name, target="restaurantName")
display(owner_name, target="ownerName")
display(year_established, target="yearEstablished")
display(popular_item_price, target="popularItemPrice")

# Display the menu in a table format
menu_table = window.document.getElementById("menuPrices")
for item, price in menu_prices.items():
    row = f"<tr><td>{item}</td><td>₱{price:.2f}</td></tr>"
    menu_table.innerHTML += row

# Display product list
products_ul = window.document.getElementById("productNames")
for product in product_names:
    products_ul.innerHTML += f"<li>{product}</li>"

# Display allergen list
allergens_ul = window.document.getElementById("commonAllergens")
for allergen in common_allergens:
    allergens_ul.innerHTML += f"<li>{allergen}</li>"

# Display business hours and tax rate
display(f"{business_hours['open']} - {business_hours['close']}", target="businessHours")
display(f"{tax_rate * 100}%", target="taxRate")

# Show delivery availability with colored badge
delivery = window.document.getElementById("delivery")
if has_delivery:
    delivery.innerHTML = '<span class="badge bg-success">Delivery Available</span>'
else:
    delivery.innerHTML = '<span class="badge bg-danger">Not Available</span>'
