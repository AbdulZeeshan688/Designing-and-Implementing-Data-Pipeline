from file_handler import FileHandler

filename = "inventory.csv"
inventory_file = FileHandler(filename) # create an object 
rows = inventory_file.read() # read the file from the previous created object
print (f'#####Start : {filename} #####' )

for row in rows:
    print(row)
print (f'##### {filename} #####' )