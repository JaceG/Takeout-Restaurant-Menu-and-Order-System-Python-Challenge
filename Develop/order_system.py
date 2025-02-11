def place_order(menu):
    order = []
    menu_items = get_menu_items_dict(menu)
    print("Welcome to the Generic Take Out Restaurant.")
    
    ordering = True
    while ordering:
        print("What would you like to order? ")
        print_menu_heading()
        
        i = 1
        for food_category, options in menu.items():
            for meal, price in options.items():
                print_menu_line(i, food_category, meal, price)
                i += 1
        
        menu_selection = input("\nType menu number: ")
        order = update_order(order, menu_selection, menu_items)
        
        continue_order = input("\nWould you like to keep ordering? (N) to quit: ")
        if continue_order.lower() == 'n':
            print("Thank you for your order.")
            print("This is what we are preparing for you.\n")
            print_receipt_heading()
            print_itemized_receipt(order)
            prices_list = [item["Price"] * item["Quantity"] for item in order]
            order_total = round(sum(prices_list), 2)
            print_receipt_footer(order_total)
            ordering = False
    
    return order, order_total

def update_order(order, menu_selection, menu_items):
    try:
        menu_selection = int(menu_selection)
        if menu_selection in menu_items:
            item_name = menu_items[menu_selection]["Item name"]
            price = menu_items[menu_selection]["Price"]
            quantity_input = input(f"What quantity of {item_name} would you like? \n(This will default to 1 if number is not entered)\n")
            try:
                quantity = int(quantity_input)
            except ValueError:
                quantity = 1
            order.append({
                "Item name": item_name,
                "Price": price,
                "Quantity": quantity
            })
        else:
            print(f"{menu_selection} was not a menu option.")
    except ValueError:
        print(f"{menu_selection} was not a menu option.")
    return order

def print_itemized_receipt(receipt):
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        print_receipt_line(item_name, price, quantity)

def print_receipt_line(item_name, price, quantity):
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    if index < 10:
        index_space = " " * 6
    else:
        index_space = " " * 5
    
    item_name = f"{food_category} - {meal}"
    spaces = " " * (32 - len(item_name))
    
    print(f"{index}{index_space}| {item_name}{spaces} | ${price:.2f}")

def get_menu_items_dict(menu):
    menu_items = {}
    i = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1
    return menu_items

def get_menu_dictionary():
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    return meals