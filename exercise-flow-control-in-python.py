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
initial_funds = funds

### DISPLAY MENU AND TRANSACTION PROCESS

#Track Purchases
purchase_history = []
total_spent = 0.0



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
            initial_funds += additional
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
        total_spent += item_price
        # Add to purchase history
        purchase_history.append({
            'item': selected_item,
            'price': item_price})
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
            initial_funds += additional
            print(f"Updated balance: ${funds:.2f}")
        else:
            print("Transaction cancelled.")
            break



#### FINAL MESSAGE

print("\n" + "="*40)
print("           PURCHASE SUMMARY")
print("="*40)

if purchase_history:
    print("Items purchased:")
    print("-" * 25)
    
    # Count quantities of each item
    item_counts = {}
    for purchase in purchase_history:
        item_name = purchase['item']
        if item_name in item_counts:
            item_counts[item_name] += 1
        else:
            item_counts[item_name] = 1
    
    # Display each item with quantity and individual price
    for item_name, quantity in item_counts.items():
        item_price = items[item_name]
        item_total = item_price * quantity
        if quantity == 1:
            print(f"{item_name.capitalize():<15} x{quantity:<3} ${item_price:.2f}")
        else:
            print(f"{item_name.capitalize():<15} x{quantity:<3} ${item_price:.2f} each = ${item_total:.2f}")
    
    print("-" * 25)
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Money inserted: ${initial_funds:.2f}")
    print(f"Change returned: ${funds:.2f}")
    
else:
    print("No items purchased.")
    print(f"Money returned: ${funds:.2f}")

print("="*40)
print("Thank you for using the vending machine!")