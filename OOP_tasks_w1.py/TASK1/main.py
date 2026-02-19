from file_handler import FileHandler
from devices import IoTDevice

def simple_cipher(text: str, encrypt: bool = True) -> str:
    # Simple logic to shift characters for encryption/decryption
    shift = 1 if encrypt else -1
    return "".join(chr(ord(c) + shift) for c in text)

filename = "iot_inventory.csv"
handler = FileHandler(filename)
devices = []

while True:
    print("\n--- IoT Device Management ---")
    print("1 - Add IoT Device")
    print("2 - Serialize Data")
    print("3 - Deserialize Data")
    print("4 - Encrypt Data")
    print("5 - Decrypt Data")
    print("0 - Exit")

    choice = input("Select an option: ")

    try:
        if choice == '1':
            # User se naya device data lena
            d_id = input("Enter Device ID: ")
            loc = input("Enter Location: ")
            val = float(input("Enter Data Value: "))
            print("Types: 1-Temp, 2-Humidity, 3-Motion")
            t_choice = input("Select Type: ")
            
            d_type = "Temperature" if t_choice == '1' else "Humidity" if t_choice == '2' else "Motion"
            new_device = IoTDevice(d_id, loc, val, d_type)
            devices.append(new_device)
            print("Device added to list.")

        elif choice == '2':
            # Objects ko strings mein badal kar file mein save karna
            serialized_data = [d.serialize() for d in devices]
            handler.write(serialized_data)
            print("Data serialized and saved to file.")

        elif choice == '3':
            # File se data parh kar objects banana
            rows = handler.read()
            devices = [IoTDevice.deserialize(r) for r in rows if r.strip()]
            print("### Current Devices ###")
            for d in devices:
                d.display_info()

        elif choice == '4':
            # File content ko encrypt karke save karna
            rows = handler.read()
            raw_text = "\n".join(rows)
            encrypted_text = simple_cipher(raw_text, encrypt=True)
            with open(filename, 'w') as f:
                f.write(encrypted_text)
            print("File data encrypted.")

        elif choice == '5':
            # File content ko decrypt karke wapis save karna
            with open(filename, 'r') as f:
                encrypted_text = f.read()
            decrypted_text = simple_cipher(encrypted_text, encrypt=False)
            with open(filename, 'w') as f:
                f.write(decrypted_text)
            print("File data decrypted.")

        elif choice == '0':
            print("Exiting program.")
            break
        
        else:
            # Invalid menu selection handle karna
            print("Invalid selection. Please try again.")

    except ValueError:
        # Ghalat input type handle karna
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")