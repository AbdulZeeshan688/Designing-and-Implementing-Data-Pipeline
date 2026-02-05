from file_handler import FileHandler
from items import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename) 
rows = inventory_file.read() 

# 1. Deserialize: Convert strings to Objects
items = []
for row in rows:
    items.append(Item.deserialize(row))

# 2. Display Objects
print ('#### inventory ####')
for item in items:
    item.display_info()
print ('#### inventory ####')

# 3. User Interaction to change value
try:
    # We subtract 1 because Python lists start at 0, but humans count from 1
    selection = int(input(f"Change item value (enter 1 - {len(items)}): ")) - 1
    
    if 0 <= selection < len(items):
        selected_item = items[selection]
        new_price = float(input(f"Set new value for {selected_item.name}: "))
        
        # Update the object
        selected_item.value = new_price
        
        # 4. Serialize: Convert Objects back to Strings
        print ("Serializing items into rows.")
        print ("### Rows ###")
        for item in items:
            print(item.serialize())
            
        print("Program ending")
    else:
        print("Invalid selection number.")

except ValueError:
    print("Invalid input. Please enter a number.")