# list of school supplies
available_items = ["Pencil", "Eraser", "Notebook", "Ruler", "Crayons"]

#  Inventory dictionary
inventory = {}

#  Program loop
while True:
    print("\n--- 📚 School Supplies Inventory ---")
    print("Available items: ", ", ".join(available_items))
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    #  Add item
    if choice == '1':
        item = input("Enter item name from the list above: ").capitalize()
        if item not in available_items:
            print("❗Item not in available list.")
            continue
        quantity = int(input("Enter quantity: "))
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        print(f"✅ {quantity} {item}(s) added. Total: {inventory[item]}")

    # View inventory
    elif choice == '2':
        print("\n📋 Current Inventory:")
        if not inventory:
            print("Inventory is empty.")
        else:
            for item, qty in inventory.items():
                print(f"- {item}: {qty}")

    #  Remove item
    elif choice == '3':
        item = input("Enter item name to remove: ").capitalize()
        if item in inventory:
            del inventory[item]
            print(f"❌ {item} removed from inventory.")
        else:
            print(f"⚠️ {item} not found.")

    # 🚪 Exit
    elif choice == '4':
        print("👋 Exiting the program. Bye!")
        break

    # 🚫 Invalid choice
    else:
        print("Please enter a valid option (1-4).")
