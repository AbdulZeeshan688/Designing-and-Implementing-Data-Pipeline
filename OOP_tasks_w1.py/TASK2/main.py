from characters import Warrior, Mage, Archer

# List to store created characters
party = []

def simulate_battle(character_list):
    # Function jo kisi bhi GameCharacter child class ko handle kar sakti hai
    if not character_list:
        print("No characters available for battle!")
        return

    print("\n--- BATTLE SIMULATION START ---")
    for char in character_list:
        print(f"Turn: {char.TYPE_LABEL} - {char.name}")
        char.attack()# IDHAR POLYMORPHISM USE HO RAH HUM KISI KO CALL NI KAR RAHAH PYTHON AUTO .
        char.defend()
    print("\n--- BATTLE SIMULATION END ---")

while True:
    print("\n--- Game Character Menu ---")
    print("1 - Create Character")
    print("2 - Simulate Battle")
    print("0 - Exit")

    choice = input("Select an option: ")

    try:
        if choice == '1':
            # Character creation logic
            print("\nChoose Class: 1-Warrior, 2-Mage, 3-Archer")
            class_type = input("Enter choice: ")
            name = input("Enter character name: ")

            if class_type == '1':
                party.append(Warrior(name=name))
                print(f"Warrior {name} joined the party.")
            elif class_type == '2':
                party.append(Mage(name=name))
                print(f"Mage {name} joined the party.")
            elif class_type == '3':
                party.append(Archer(name=name))
                print(f"Archer {name} joined the party.")
            else:
                print("Invalid class selection.")

        elif choice == '2':
            # Battle simulate karne ke liye function call
            simulate_battle(party)# ALL CHARACTER TAKE TURNS 

        elif choice == '0':
            # Program khatam karne ke liye
            print("Exiting game. Goodbye!")
            break

        else:
            # Ghalat menu choice handle karna
            print("Invalid menu choice. Please try again.")

    except Exception as e:
        # Generic error handling jaisa aapki file mein tha
        print(f"An error occurred: {e}")