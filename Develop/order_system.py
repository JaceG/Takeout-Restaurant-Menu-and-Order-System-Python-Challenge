def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    # TODO: Create a continuous while loop so customers can order multiple items
    # Solution: Create a ordering variable and set it to True for continuous loop
    ordering = True
    while ordering:

        # TODO: Ask the customer what they want to order
        # Solution: This will be handled after showing the menu

        # Create a variable for the menu item number
        i = 1

        # Print the menu header
        print_menu_heading()

        # TODO: Loop through the menu dictionary
        # TODO: Extract the food category and the options for each category
        # Solution: Use a for loop with .items() to get both keys and values
        for food_category, options in menu.items():

            # TODO: Loop through the options for each food category
            # TODO: Extract the meal and the price for each option
            # Solution: Nested for loop to get meal and price
            for meal, price in options.items():

                # Print the menu item number, food category, meal, and price
                print_menu_line(i, food_category, meal, price)

                # Update the menu selection number
                i += 1

        # TODO: Ask customer to input menu item number
        # Solution: Use input() to get customer selection
        menu_selection = input("\nWhat would you like to order? (Enter item number): ")

        # TODO: Update the order list using the update_order function
        # TODO: Send the order list, menu selection, and menu items as arguments
        # Solution: Call update_order with required parameters
        order = update_order(order, menu_selection, menu_items)

        # TODO: Ask the customer if they would like to order anything else
        # TODO: Let the customer know if they should type 'n' or 'N' to quit
        # Solution: Ask for continuation with clear instructions
        continue_order = input("\nWould you like to order anything else? (Enter 'n' or 'N' to quit): ")

        # TODO: Write a conditional statement that checks the user's input
        # TODO: The conditional statement should check for 'n' or 'N'
        # Solution: Check for both lowercase and uppercase 'n'
        if continue_order.lower() == 'n':
            # TODO: Write a print statement that thanks the customer for their order
            # Solution: Print thank you message
            print("\nThank you for your order!")

            # TODO: Use list comprehension to create a list called prices_list
            # TODO: which contains the total prices for each item in the order list
            # TODO: The total price for each item should multiply the price by quantity
            # Solution: List comprehension to calculate total prices
            prices_list = [item["Price"] * item["Quantity"] for item in order]

            # TODO: Create an order_total from the prices list using sum()
            # TODO: Round the prices to 2 decimal places.
            # Solution: Calculate total and round to 2 decimal places
            order_total = round(sum(prices_list), 2)

            # TODO: Exit the ordering loop
            # TODO: Either use a break statement or set the condition to False
            # Solution: Set ordering to False to exit loop
            ordering = False

    # TODO: Return the order list and the order total
    # Solution: Return both required values
    return order, order_total

def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # TODO: Check if the customer typed a number
    # Solution: Use try-except to check if input can be converted to int
    try:
        # TODO: Convert the menu selection to an integer
        # Solution: Convert string to integer
        menu_selection = int(menu_selection)

        # TODO: Check if the menu selection is in the menu items keys
        # Solution: Check if selection exists in menu_items
        if menu_selection in menu_items:
            # TODO: Store the item name as a variable
            # Solution: Get item name from menu_items dictionary
            item_name = menu_items[menu_selection]["Item name"]

            # TODO: Ask the customer for the quantity of the menu item
            # TODO: Use the item name variable in the question
            # Solution: Ask for quantity with item name
            quantity_input = input(f"How many {item_name} would you like? ")

            # TODO: Check if the quantity is a number, default to 1 if not
            # Solution: Try to convert to int, default to 1 if fails
            try:
                quantity = int(quantity_input)
            except ValueError:
                quantity = 1
                print("Invalid quantity. Defaulting to 1.")

            # TODO: Add a dictionary to the order list 
            # TODO: The dictionary should include the item name, price, and quantity
            # Solution: Create and append dictionary with required keys
            order.append({
                "Item name": item_name,
                "Price": menu_items[menu_selection]["Price"],
                "Quantity": quantity
            })
        else:
            # TODO: When the user's input isn't valid, tell the customer
            # Solution: Print error for invalid menu selection
            print(f"\nMenu selection {menu_selection} is not valid.")
    except ValueError:
        # TODO: When the menu selection wasn't valid, print error message
        # Solution: Print error for non-numeric input
        print(f"\nInvalid input: {menu_selection} is not a number.")

    # TODO: Return the updated order
    # Solution: Return the order list
    return order

def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt
    #print(receipt)

    # TODO: Loop through the items in the customer's receipt
    # Solution: Use for loop to iterate through receipt items
    for item in receipt:
        # TODO Store the dictionary items as variables
        # Solution: Extract values from dictionary
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # TODO: Print the receipt line using the print_receipt_line function
        # TODO: Send the item name, price, and quantity as separate arguments
        # Solution: Call print_receipt_line with extracted values
        print_receipt_line(item_name, price, quantity)

##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
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
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

