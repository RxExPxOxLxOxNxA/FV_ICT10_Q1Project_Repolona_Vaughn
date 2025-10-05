from pyscript import display, document

# ordering form system (skills test)

# Menu dictionary - item: price 
menu_prices = {
    "Burger": 199.99,
    "Pasta": 249.50,
    "Fries": 89.00,
    "Steak": 599.00,
    "Pizza": 399.75
}

# function triggered when the "Create Order" button is clicked
def create_order(event):
    """
    collects order, customer details, and total price then displaying the summary
    """

    # collects checked items from form
    checkboxes = document.querySelectorAll("input[name='item']:checked")
    selected_items = [cb.value for cb in checkboxes] # from skillstest using copilot 

    # retrieves customer input values
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number").value  

    # checks that all fields are filled and number format looks valid
    if not name.strip() or not address.strip() or not number.strip(): # .strip codes are from copilot had a hard time making sure the user input was truly filled in asked copilot for help and gave this code 
        display("⚠️ Please fill in all customer details.", target="output")
        return

    if not number.isdigit() or len(number) < 11: # 11 because philippines is 11 digits long including the 0 at the start
        display("Please enter a valid phone number (at least 11 digits).", target="output") # line 34-36 this as well from coipilot same problem had a hard time making sure that the phone number was only numbers and not anything else
        return

    # total price calculation code
    total_price = sum(menu_prices[item] for item in selected_items)

    # if nothing gets selected, reminds the user to select something
    if not selected_items:
        display("Please select at least one menu item.", target="output")
        return

    # order summary output
    summary = f"""
    ORDER SUMMARY
    Name: {name}
    Address: {address}
    Contact: {number}

    Items Ordered: {', '.join(selected_items)}
    Total Price: ₱{total_price:.2f}

    Thank you for ordering at Vaughn's Fast Food Place!
    """

    display(summary, target="output")
