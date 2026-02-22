# Zaroori classes import kar rahe hain
from devices import SmartLight, SmartThermostat, SmartLock

# Devices ko store karne ke liye list
home_devices = []

def perform_operation(device_list):
    # Yeh function polymorphism use karta hai
    # Har device ka apna 'operate' method call hoga
    if not device_list:
        print("No devices found in the system.")
        return

    print("\n#### Operating All Devices ####")
    for device in device_list:
        device.operate()
    print("###############################")

while True:
    print("\n--- Smart Home Menu ---")
    print("1 - Add Smart Device")
    print("2 - Operate Devices")
    print("0 - Exit")

    choice = input("Option select karein: ")

    try:
        if choice == '1':
            # Naya device add karne ka logic
            print("\nSelect Device Type: 1-Light, 2-Thermostat, 3-Lock")
            dev_type = input("Choice: ")
            name = input("Enter device name: ")

            if dev_type == '1':
                level = int(input("Enter brightness (0-100): "))
                home_devices.append(SmartLight(device_name=name, brightness=level))
                print(f"Light '{name}' is added .")
            
            elif dev_type == '2':
                temp = int(input("Enter target temperature: "))
                home_devices.append(SmartThermostat(device_name=name, temperature=temp))
                print(f"Thermostat '{name}' add ho gaya.")
            
            elif dev_type == '3':
                home_devices.append(SmartLock(device_name=name))
                print(f"Lock '{name}' add ho gaya.")
            
            else:
                print("Invalid device type selection.")

        elif choice == '2':
            # Polymorphism demonstrate karne ke liye function call
            perform_operation(home_devices)

        elif choice == '0':
            # Program khatam karne ke liye
            print("Exiting Smart Home System. Allah Hafiz!")
            break
        
        else:
            # Ghalat menu selection handle kar rahe hain
            print("Invalid menu choice. Dubara koshish karein.")

    except ValueError:
        # Agar user text enter kare jahan number chahiye
        print("Error: Invalid input format. Please enter numbers where required.")
    except Exception as e:
        # Kisi bhi aur error ko catch karne ke liye
        print(f"An unexpected error occurred: {e}")