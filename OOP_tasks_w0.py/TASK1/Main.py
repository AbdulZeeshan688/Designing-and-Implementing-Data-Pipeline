# counter.py file se Counter class import kar rahe hain
from Counter import Counter

def main():
    print("Program starting.")
    print("Initializing counter...")

    # Counter class ka object bana rahe hain
    counter = Counter()

    print("Counter initialized.")

    # infinite loop taake program bar bar options dikhaye
    while True:
        print("\nOptions:")
        print("1) Add count")
        print("2) Get count")
        print("3) Zero count")
        print("0) Exit program")

        # user se choice le rahe hain
        choice = input("Choice: ")

        if choice == "1":
            # count barha rahe hain
            counter.addCount()
            print("Count increased")

        elif choice == "2":
            # current count show kar rahe hain
            print(f"Current count '{counter.getCount()}'")

        elif choice == "3":
            # count ko zero kar rahe hain
            counter.zeroCount()
            print("Count zeroed")

        elif choice == "0":
            # program band kar rahe hain
            print("Program ending.")
            break

        else:
            # agar user ghalat option dale
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
