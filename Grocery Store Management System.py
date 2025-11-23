# Simple Grocery Store System
# stored as {id: [name, price, stock]}
inventory = {} 

def add_item():
    p_id = input("Enter Item ID: ")
    
    # check if id exists
    if p_id in inventory:
        print("Error: ID already exists!")
        return

    name = input("Product Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    
    # Storing as a list is simpler
    inventory[p_id] = [name, price, qty] 
    print("Item added.")

def show_items():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\nID   Name    Price   Qty")
        print("=" * 30)
        for key, val in inventory.items():
            # val[0] is name, val[1] is price, val[2] is stock
            print(f"{key}    {val[0]}    {val[1]}    {val[2]}")
        print("=" * 30)

def edit_item():
    target_id = input("Enter ID to edit: ")
    
    if target_id in inventory:
        current = inventory[target_id]
        print("Current details:", current)
        
        # Simple update - just overwrite everything
        new_name = input("Enter New Name: ")
        new_price = float(input("Enter New Price: "))
        new_qty = int(input("Enter New Stock: "))
        
        inventory[target_id] = [new_name, new_price, new_qty]
        print("Updated successfully.")
    else:
        print("Item not found.")

def remove_item():
    target = input("Enter ID to delete: ")
    if target in inventory:
        del inventory[target]
        print("Deleted.")
    else:
        print("ID not found.")

def main():
    while True:
        print("\n1. Add New Item")
        print("2. View All")
        print("3. Edit Item")
        print("4. Delete Item")
        print("5. Quit")
        
        opt = input("Choose option (1-5): ")
        
        if opt == '1':
            add_item()
        elif opt == '2':
            show_items()
        elif opt == '3':
            edit_item()
        elif opt == '4':
            remove_item()
        elif opt == '5':
            print("Bye!")
            break
        else:
            print("Wrong input.")

# Start the program
main()