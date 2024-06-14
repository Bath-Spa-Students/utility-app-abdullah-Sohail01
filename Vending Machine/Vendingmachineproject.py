# Vending Machine
# Drinks menu
drinks_menu = {
    "D1": {"item": "Coke", "price": 5.5},
    "D2": {"item": "Sprite", "price": 5.5},
    "D3": {"item": "Iced Tea", "price": 4.75},
    "D4": {"item": "Water", "price": 4.0}
}

# Snacks menu
snacks_menu = {
    "S1": {"item": "Chips", "price": 4.0},
    "S2": {"item": "Chocolate Bar", "price": 4.75},
    "S3": {"item": "Popcorn", "price": 6.25},
    "S4": {"item": "Pretzels", "price": 5.5}
}

# Function to display the menu
def display_menu(menu, menu_type):
    print(f"--- {menu_type} Menu ---")
    for code, item in menu.items():
        print(f"{code}: {item['item']} - AED {item['price']}")

# Function to get user's selection
def get_selection(menu, menu_type):
    while True:
        selection = input(f"Enter the code of your {menu_type} selection: ").upper()
        if selection in menu:
            return selection
        else:
            print("Invalid selection. Please try again.")

# Function to calculate change
def calculate_change(amount_paid, total_price):
    change = amount_paid - total_price
    return change

# Main function
def main():
    choice = input("Do you want to see the snack menu, drink menu, or both? (Type 'snack', 'drink', or 'both'): ")
    
    if choice.lower() == 'snack':
        display_menu(snacks_menu, "Snacks")
        snack_selection = get_selection(snacks_menu, "snack")
        snack = snacks_menu[snack_selection]
        snack_price = snack["price"]
        total_price = snack_price
        items = [snack["item"]]
    elif choice.lower() == 'drink':
        display_menu(drinks_menu, "Drinks")
        drink_selection = get_selection(drinks_menu, "drink")
        drink = drinks_menu[drink_selection]
        drink_price = drink["price"]
        total_price = drink_price
        items = [drink["item"]]
    elif choice.lower() == 'both':
        display_menu(drinks_menu, "Drinks")
        drink_selection = get_selection(drinks_menu, "drink")
        drink = drinks_menu[drink_selection]
        drink_price = drink["price"]
        
        display_menu(snacks_menu, "Snacks")
        snack_selection = get_selection(snacks_menu, "snack")
        snack = snacks_menu[snack_selection]
        snack_price = snack["price"]
        
        total_price = drink_price + snack_price
        items = [drink["item"], snack["item"]]
    else:
        print("Invalid choice. Please try again.")
        return True  # Indicate to continue

    amount_paid = float(input(f"Please insert money for {', '.join(items)} (AED {total_price}): "))
    while amount_paid < total_price:
        amount_paid += float(input(f"Please insert AED {total_price - amount_paid:.2f} more: "))

    change = calculate_change(amount_paid, total_price)

    print(f"Dispensing {', '.join(items)}...")
    if change > 0:
        print(f"Please take your change: AED {change:.2f}")
    else:
        print("No change due.")

    order_again = input("Do you want to order something else? (Type 'quit' to exit): ")
    if order_again.lower() == 'quit':
        return False  # Indicate to exit
    return True  # Indicate to continue

if __name__ == "__main__":
    while main():
        pass
