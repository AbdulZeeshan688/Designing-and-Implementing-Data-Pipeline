# Zaroori classes import kar rahe hain
from file_handler import FileHandler
from items import Item

# Inventory file ka naam
filename = "inventory.csv"

# FileHandler ka object bana kar file read kar rahe hain
inventory_file = FileHandler(filename) 
rows = inventory_file.read() 


# 1. Deserialize: file ki rows ko Item objects mein convert kar rahe hain
items = []
for row in rows:
    items.append(Item.deserialize(row))


# 2. Saare items display kar rahe hain
print('#### inventory ####')
for item in items:
    item.display_info()
print('#### inventory ####')


# 3. User ko allow kar rahe hain ke kisi item ki value change kare
try:
    # User se item number le rahe hain (list 0 se start hoti hai is liye -1 kar rahe hain)
    selection = int(input(f"Change item value (enter 1 - {len(items)}): ")) - 1
    
    # Check kar rahe hain ke number valid range mein hai
    if 0 <= selection < len(items):
        selected_item = items[selection]
        
        # Nayi price user se le rahe hain
        new_price = float(input(f"Set new value for {selected_item.name}: "))
        
        # Object ki value update kar rahe hain
        selected_item.value = new_price
        
        # 4. Serialize: updated objects ko dobara string format mein convert kar rahe hain
        print("Serializing items into rows.")
        print("### Rows ###")
        for item in items:
            print(item.serialize())
            
        print("Program ending")
    else:
        print("Invalid selection number.")

# Agar user ghalat input de (text ya invalid value)
except ValueError:
    print("Invalid input. Please enter a number.")

