import tkinter as tk
from tkinter import messagebox
import os

# --- This function runs your other files when a button is clicked ---
def open_program(filename):
    # This command tells your Mac to run the other python files
    os.system(f'python3 {filename}')

def login():
    username = entry_user.get()
    password = entry_pass.get()
    
    # Simple test login
    if username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login Successful!")
        show_main_menu() # Go to the 6th view!
    else:
        messagebox.showerror("Error", "Wrong username or password")

def show_main_menu():
    # Hide the login stuff
    frame_login.pack_forget()
    
    # Show the Main Menu stuff
    frame_menu.pack(pady=20)

# --- SETUP THE MAIN WINDOW ---
window = tk.Tk()
window.title("My Python UI App")
window.geometry("400x400")
window.configure(bg="white")

# --- VIEW 1: THE LOGIN SCREEN ---
frame_login = tk.Frame(window, bg="white")
frame_login.pack(pady=50)

tk.Label(frame_login, text="Username:", bg="white", font=("Arial", 12)).pack()
entry_user = tk.Entry(frame_login)
entry_user.pack(pady=5)

tk.Label(frame_login, text="Password:", bg="white", font=("Arial", 12)).pack()
entry_pass = tk.Entry(frame_login, show="*")
entry_pass.pack(pady=5)

tk.Button(frame_login, text="Login", width=15, command=login).pack(pady=15)

# --- VIEW 2 (The 6th View): THE MAIN MENU ---
# (This starts hidden until you log in)
frame_menu = tk.Frame(window, bg="white")

tk.Label(frame_menu, text="Main Dashboard", bg="white", font=("Arial", 18, "bold")).pack(pady=10)

# Buttons that open your other homework files!
tk.Button(frame_menu, text="1. Matrix Calculator", width=20, command=lambda: open_program("matrix_calc.py")).pack(pady=5)
tk.Button(frame_menu, text="2. Rotate Square", width=20, command=lambda: open_program("rotate_square.py")).pack(pady=5)
tk.Button(frame_menu, text="3. Rotate Cube", width=20, command=lambda: open_program("rotate_cube.py")).pack(pady=5)
tk.Button(frame_menu, text="4. Rocket Launch", width=20, command=lambda: open_program("rockets.py")).pack(pady=5)

# Start the app
window.mainloop()