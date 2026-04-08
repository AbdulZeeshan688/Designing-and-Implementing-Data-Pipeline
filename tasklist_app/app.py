# ============================================================
#  app.py  ← RUN THIS FILE TO START THE APP
#
#  This is the entry point - the very first file that runs.
#  It sets up the database, creates the window,
#  and shows the login screen.
#
#  HOW TO RUN:
#      python app.py
# ============================================================

import tkinter as tk       # tkinter = Python's GUI library (comes with Python)
import database            # our database.py file
from login import LoginScreen   # our login.py file, importing the LoginScreen class
from main import QuestBoard     # our main.py file, importing the QuestBoard class


def after_login(user_info):
    # This function is called automatically when the user logs in successfully.
    # "user_info" is the logged-in user's data: (id, username, xp, level)

    # Remove all login widgets from the window
    for widget in main_window.winfo_children():
        widget.destroy()

    # Expand the window for the main quest board
    main_window.geometry("780x600")

    # Open the main quest board with this user's info
    QuestBoard(main_window, user_info)


# ============================================================
#  MAIN STARTUP CODE
#  Everything below runs when you type: python app.py
# ============================================================

# 1. Create the database tables (only happens once - safe to call every time)
database.create_tables()

# 2. Create the main Tkinter window
main_window = tk.Tk()          # This creates the actual window
main_window.resizable(True, True)  # Allow resizing

# 3. Show the login screen inside the window
LoginScreen(main_window, after_login)

# 4. Start the app loop - keeps the window open and responsive
main_window.mainloop()
# mainloop() = "keep running and wait for user input"
# Without this, the window would open and close immediately!
