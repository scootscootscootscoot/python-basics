
## Setup

# values from the instructions
burger = 5.99
pizza = 8.49
salad = 4.99
drink = 1.99

##Functions and Loops


## This function calculates the total cost of the items ordered and rounds them to 2 decimal places
def calculate_total(burger_qty, pizza_qty, salad_qty, drink_qty):
    total = burger_qty * burger + pizza_qty * pizza + salad_qty * salad + drink_qty * drink
    return round(total, 2)

##This function Displays the menu with prices, I included some print("\n" + "="*40) lines to make the design look nicer
def display_menu():
    print("\n" + "="*40)
    print("           RESTAURANT MENU")
    print("="*40)
    print(f"1. Burger     - ${burger:.2f}")
    print(f"2. Pizza      - ${pizza:.2f}")
    print(f"3. Salad      - ${salad:.2f}")
    print(f"4. Drink      - ${drink:.2f}")
    print("="*40)

## This function displays the order summary after the items have been ordered for a particular order. I used If statements to calculate the total and output it
def display_order_summary(burger_qty, pizza_qty, salad_qty, drink_qty, order_total):
    print("\n" + "-"*40)
    print("         ORDER SUMMARY")
    print("-"*40)

    if burger_qty > 0:
        burger_total = burger_qty * burger
        print(f"Burger x{burger_qty} - ${burger_total:.2f}")

    if pizza_qty > 0:
        pizza_total = pizza_qty * pizza
        print(f"Pizza x{pizza_qty} - ${pizza_total:.2f}")

    if salad_qty > 0:
        salad_total = salad_qty * salad
        print(f"Salad x{salad_qty} - ${salad_total:.2f}")

    if drink_qty > 0:
        drink_total = drink_qty * drink
        print(f"Drink x{drink_qty} - ${drink_total:.2f}")
        
    print("-"*40)
    print(f"TOTAL: ${order_total:.2f}")
    print("-"*40)

## This will display a final summary of not only one of the orders but all orders that can potentially be placed while the while loop is active
def display_final_summary(all_orders):
    print("\n" + "="*50)
    print("           FINAL SESSION SUMMARY")
    print("="*50)

    grand_total = 0
    order_num = 1
    
    for order in all_orders:
        burger_qty, pizza_qty, salad_qty, drink_qty, order_total = order
        
        print(f"\nOrder #{order_num}:")
        print("-" * 20)
        
        ## essentially the exact same calculations here as in the order summary
        if burger_qty > 0:
            burger_total = burger_qty * burger
            print(f"  Burger x{burger_qty} - ${burger_total:.2f}")
        
        if pizza_qty > 0:
            pizza_total = pizza_qty * pizza
            print(f"  Pizza x{pizza_qty} - ${pizza_total:.2f}")
        
        if salad_qty > 0:
            salad_total = salad_qty * salad
            print(f"  Salad x{salad_qty} - ${salad_total:.2f}")
        
        if drink_qty > 0:
            drink_total = drink_qty * drink
            print(f"  Drink x{drink_qty} - ${drink_total:.2f}")
        
        print(f"  Order Total: ${order_total:.2f}")
        grand_total += order_total
        order_num += 1
    
    print("="*50)
    print(f"GRAND TOTAL FOR ALL ORDERS: ${grand_total:.2f}")
    print("="*50)



## This is the key function that will prompt the user and store all the inputs as the values that are needed for calculation, it all contains the while loop that
## allows them to order while they are still able to order
def main():
    
    all_orders = []  
    
    print("Welcome to our Restaurant Ordering System!")
    print("We're delighted to serve you today!")
    
    while True:
        ## Sets quantities for current order
        burger_qty = 0
        pizza_qty = 0
        salad_qty = 0
        drink_qty = 0
        
        # Display menu and take orders
        while True:
            display_menu() ## Display menu function we defined earlier with all the lines and spaces
            
            # Get user's menu selection via 1, 2, 3, or 4 for simplicity
            choice = input("\nPlease select an item (1-4) or 'done' to finish this order: ").strip().lower()
            
            if choice == 'done':
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid selection. Please choose 1, 2, 3, 4, or 'done'.")
                continue
            
            # Get quantity, only positive ints allowed, no random characters
            try:
                quantity = int(input("How many would you like? "))
                if quantity <= 0:
                    print("Please enter a positive number.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            # Add to current order based on choice, returns output to verify they got what they wanted
            if choice == '1':
                burger_qty += quantity
                print(f"Added {quantity} Burger(s) to your order!")
            elif choice == '2':
                pizza_qty += quantity
                print(f"Added {quantity} Pizza(s) to your order!")
            elif choice == '3':
                salad_qty += quantity
                print(f"Added {quantity} Salad(s) to your order!")
            elif choice == '4':
                drink_qty += quantity
                print(f"Added {quantity} Drink(s) to your order!")
        
        # Check if any items were ordered
        if burger_qty == 0 and pizza_qty == 0 and salad_qty == 0 and drink_qty == 0:
            print("No items were ordered.")
        else:
            # Calculate and display order summary
            order_total = calculate_total(burger_qty, pizza_qty, salad_qty, drink_qty) ## calculate total function from earlier
            display_order_summary(burger_qty, pizza_qty, salad_qty, drink_qty, order_total) ## Display order summary, note, not the final
            
            all_orders.append((burger_qty, pizza_qty, salad_qty, drink_qty, order_total)) # this adds all quantities and the going total to our list
            
            print("Thank you for your order!")
        
        # Ask if user wants to place another order
        while True:
            another_order = input("\nWould you like to place another order? (yes/no): ").strip().lower()
            if another_order in ['yes', 'y']:
                print("\nStarting a new order...")
                break
            elif another_order in ['no', 'n']:
                # Display final summary if there were any orders
                if all_orders:
                    display_final_summary(all_orders) ## function that displays the final summary, we made this earlier 
                    print("\nThank you for dining with us today!")
                    print("Have a wonderful day!")
                else:
                    print("Thank you for visiting our restaurant!")
                    print("We hope to serve you soon!")
                return
            else:
                print("Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    main()