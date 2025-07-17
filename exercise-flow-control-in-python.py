### DISPLAY PRODUCT MENU

items = {
 "coca cola": 1.50,
 "chips": 2.00,
 "candy": 1.00,
 "chocolate bar": 0.50,
 "warm fish head": 500.00
}


### PROMPT FOR INITIAL FUNDS


user_input = input("How much are you inserting into the machine, good buddy?")
funds = float(user_input)


### DISPLAY MENU AND TRANSACTION PROCESS

# Transaction loop
while funds > 0:

    # Display affordable items

    print("\n" + "="*40)
    print("   PRODUCTS YOU CAN AFFORD, GOOD BUDDY")
    print("="*40)
    
    affordable_items = {item: price for item, price in items.items() if price <= funds}
    
    if affordable_items:
        for item, price in affordable_items.items():
            print(f"{item.capitalize()} ${price:.2f}")
    else:
        print("No items available within your budget. Get a job good buddy")
        
    print("="*40)
    print(f"Your funds: ${funds:.2f}")
    
    # If no affordable items, ask to add funds or exit

    if not affordable_items:
        add_funds = input("Would you like to add more funds, good buddy? (y/n): ").lower()
        if add_funds == 'y':
            additional = float(input("How much additional money are you inserting, good buddy? $"))
            funds += additional
            continue
        else:
            break
    
    # Prompt for item selection
    selected_item = input("\nPlease select an item by typing its name, good buddy: ").lower()
    
    # Check if item exists
    if selected_item not in items:
        print("Error: Item not found. Please select from the available items, good buddy.")
        continue
    
    # Check if item is affordable
    item_price = items[selected_item]
    
    if item_price <= funds:
        # Sufficient funds - process transaction
        funds -= item_price
        print(f"\n{selected_item.capitalize()} dispensed!")
        print(f"Remaining balance: ${funds:.2f}")
        
        # Ask if user wants to make another purchase
        if funds > 0:
            another_purchase = input("Would you like to make another purchase, good buddy? (y/n): ").lower()
            if another_purchase != 'y':
                break
        else:
            print("No funds remaining. Transaction complete. So long good buddy.")
            break
            
    else:
        # Insufficient funds
        print(f"Insufficient funds. {selected_item.capitalize()} costs ${item_price:.2f}, but you only have ${funds:.2f}")
        
        add_more = input("Would you like to insert more money or cancel, good buddy? (add/cancel): ").lower()
        
        if add_more == 'add':
            additional = float(input("How much additional money are you inserting, good buddy? $"))
            funds += additional
            print(f"Updated balance: ${funds:.2f}")
        else:
            print("Transaction cancelled.")
            break



# Final message
print(f"\nThank you for using the vending machine, good buddy!")
if funds > 0:
    print(f"Your remaining balance is ${funds:.2f}")
