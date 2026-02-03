# temperature_converter.py se class import kar rahe hain
from temperature_converter import TemperatureConverter

print("Program starting.")
print("Initializing temperature converter...")

# TemperatureConverter ka object bana rahe hain
converter = TemperatureConverter()

print("Temperature converter initialized.")

# loop taake program bar bar options dikhaye
while True:
    print("\nOptions:")
    print("1) Set temperature")
    print("2) Convert to Celsius")
    print("3) Convert to Fahrenheit")
    print("4) Convert to Kelvin")
    print("0) Exit program")

    # user se option le rahe hain
    choice = input("Choice: ")

    if choice == "1":
        # user se temperature input le rahe hain
        temp = float(input("Enter temperature: "))
        converter.setTemperature(temp)
        print(f"Temperature set to {temp}")

    elif choice == "2":
        # Celsius mein temperature show kar rahe hain
        print(f"Temperature in Celsius: {converter.toCelsius()}")

    elif choice == "3":
        # Fahrenheit mein temperature show kar rahe hain
        print(f"Temperature in Fahrenheit: {converter.toFahrenheit()}")

    elif choice == "4":
        # Kelvin mein temperature show kar rahe hain
        print(f"Temperature in Kelvin: {converter.toKelvin()}")

    elif choice == "0":
        # program band kar rahe hain
        print("Program ending.")
        break

    else:
        # ghalat option ke liye message
        print("Invalid choice, try again.")
