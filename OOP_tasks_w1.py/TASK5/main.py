# =====================================================================
# Coder Name: Abdul Zeeshan Mirza
# Course: Designing and Implementing Data Pipelines
# Date: 2026-03-01
# Time: 12:01 EET
# Description: Main menu script for Virtual Reality Simulation.
# =====================================================================

from entities import Player, NPC, Object

# Tamam entities ko store karne ke liye list
vr_world = []

def simulate_interaction(entities_list):
    # Yeh function polymorphism demonstrate karta hai
    # Har entity ka apna 'interact' method call hoga, chahay wo Player ho ya NPC
    if not entities_list:
        print("No entities found in the VR world.")
        return

    print("\n--- Commencing VR Interactions ---")
    for entity in entities_list:
        entity.interact()
    print("----------------------------------")

while True:
    print("\n--- VR Simulation Menu ---")
    print("1 - Add Entity")
    print("2 - Interact with Entities")
    print("3 - Exit")

    choice = input("Select an option: ")

    try:
        if choice == '1':
            # Nayi entity add karne ka logic
            print("\nSelect Entity Type: 1-Player, 2-NPC, 3-Object")
            ent_type = input("Choice: ")
            
            ent_name = input("Enter entity name: ")
            ent_pos = input("Enter position (e.g., 10x, 20y): ")

            if ent_type == '1':
                hp = int(input("Enter player health (e.g., 100): "))
                vr_world.append(Player(name=ent_name, position=ent_pos, health=hp))
                print(f"Player '{ent_name}' added to the simulation.")
            
            elif ent_type == '2':
                npc_role = input("Enter NPC role (e.g., Merchant, Guard): ")
                vr_world.append(NPC(name=ent_name, position=ent_pos, role=npc_role))
                print(f"NPC '{ent_name}' added to the simulation.")
            
            elif ent_type == '3':
                obj_kind = input("Enter object type (e.g., Tree, Rock, Door): ")
                vr_world.append(Object(name=ent_name, position=ent_pos, object_type=obj_kind))
                print(f"Object '{ent_name}' added to the simulation.")
            
            else:
                # Agar user ghalat entity type select kare
                print("Invalid entity type selected.")

        elif choice == '2':
            # Polymorphism demonstrate karne ke liye function ko call karna
            simulate_interaction(vr_world)

        elif choice == '3':
            # Program se bahar nikalne ke liye
            print("Exiting VR Simulation. Goodbye!")
            break
        
        else:
            # Ghalat menu selection handle kar rahe hain
            print("Invalid menu choice. Please try again.")

    except ValueError:
        # Agar text input dede kahan numbers zaroori the (like health)
        print("Error: Invalid input format. Please enter correct data types.")
    except Exception as e:
        # Kisi bhi aur unexpected error ko catch karne ke liye
        print(f"An unexpected error occurred: {e}")