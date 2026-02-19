# from file_handler import FileHandler
# from items import Item

# class Main :
#     def __init__(self) -> None:
#         filename = "inventory.csv"
#         inventory_file = FileHandler(filename)
#         rows = inventory_file.read()
#         print("### Inventory ###")
#         inventory: list[Item] = []
#         for row in rows:
#             _item = Item.deserialize(row)
#             _item.display_price()
#             inventory.append(_item)
#         print("### Inventory ###")
#         feed = input(f"Change item value (enter 1 - {len(inventory)}): ")
#         try:
#             index =int(feed) - 1
#             feed = input(f"Set new value for {inventory[index].name}: ")
#             inventory[index].set_value(float(feed))
#         except Exception:
#             print("Invalid input. Please enter a number.")
#             return None

# if __name__ == "__main__":
#     Main()
