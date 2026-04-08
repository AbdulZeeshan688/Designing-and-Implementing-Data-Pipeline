# ============================================================
#  login.py
#  This file creates the LOGIN SCREEN - the first window
#  the user sees when they open the app.
#  They can log in OR create a new account here.
# ============================================================

import tkinter as tk                  # tkinter = Python's built-in GUI tool
from tkinter import messagebox        # messagebox = pop-up alerts (info, error, warning)
import database                       # our own database.py file


# ── Colours we'll use everywhere in this file ──────────────
# It's easier to change one variable than to hunt through every line!
DARK_BG     = "#1a1a2e"   # very dark navy - main background
CARD_BG     = "#16213e"   # slightly lighter navy - for the login box
RED_ACCENT  = "#e94560"   # red/pink - for buttons
LIGHT_TEXT  = "#eaeaea"   # almost white - for regular text
GOLD        = "#f5a623"   # gold - for the title
INPUT_BG    = "#0f3460"   # dark blue - for text input fields


class LoginScreen:
    """
    This class builds and runs the login window.
    A "class" is a blueprint. We use it to group
    all the login-related code together neatly.
    """

    def __init__(self, window, after_login_function):
        # __init__ runs automatically when we create a LoginScreen.
        # "window" = the main Tkinter window passed in from app.py
        # "after_login_function" = the function to call AFTER a successful login

        self.window = window                            # save the window so other methods can use it
        self.after_login = after_login_function        # save the callback function

        # ── Set up the window ────────────────────
        self.window.title("TaskHero - Login")          # title shown in the top bar
        self.window.configure(bg=DARK_BG)              # set background colour
        self.window.geometry("420x540")                # width x height in pixels
        self.window.resizable(False, False)            # prevent resizing (looks cleaner)

        # Now build all the visual parts
        self.build_screen()


    def build_screen(self):
        # This method creates ALL the widgets (labels, buttons, etc.)
        # We split building into a separate method to keep __init__ clean.

        # ── BIG TITLE at the top ─────────────────
        title_label = tk.Label(
            self.window,
            text="⚔  TASKHERO  ⚔",          # the text shown
            font=("Courier New", 22, "bold"), # font, size, style
            bg=DARK_BG,                       # background colour (must match window bg)
            fg=GOLD                           # text colour (fg = foreground)
        )
        title_label.pack(pady=(50, 6))
        # pack() places the widget on screen
        # pady=(50, 6) adds 50 pixels space above, 6 below

        # ── Subtitle ─────────────────────────────
        subtitle = tk.Label(
            self.window,
            text="Turn your tasks into quests",
            font=("Courier New", 10),
            bg=DARK_BG,
            fg=RED_ACCENT
        )
        subtitle.pack(pady=(0, 30))

        # ── The login CARD (a box that holds the inputs) ──
        card = tk.Frame(self.window, bg=CARD_BG, padx=35, pady=30)
        card.pack(fill="x", padx=40)
        # Frame = a container box. padx/pady = inner padding (breathing room)

        # ── Username label + input ────────────────
        username_label = tk.Label(
            card,
            text="Username",
            font=("Courier New", 11, "bold"),
            bg=CARD_BG,
            fg=LIGHT_TEXT
        )
        username_label.pack(anchor="w")  # anchor="w" means align to the left (West)

        # This is the actual text box where the user types their username
        self.username_input = tk.Entry(
            card,
            font=("Courier New", 12),
            bg=INPUT_BG,
            fg=LIGHT_TEXT,
            insertbackground=LIGHT_TEXT,  # cursor colour inside the input box
            relief="flat",                # no border style
            bd=6                          # inner padding
        )
        self.username_input.pack(fill="x", pady=(4, 16))
        # fill="x" means stretch to fill the full width of the card
        # We save it as self.username_input so we can READ it later in _do_login()

        # ── Password label + input ────────────────
        password_label = tk.Label(
            card,
            text="Password",
            font=("Courier New", 11, "bold"),
            bg=CARD_BG,
            fg=LIGHT_TEXT
        )
        password_label.pack(anchor="w")

        self.password_input = tk.Entry(
            card,
            show="●",                     # show dots instead of the real text (hidden password)
            font=("Courier New", 12),
            bg=INPUT_BG,
            fg=LIGHT_TEXT,
            insertbackground=LIGHT_TEXT,
            relief="flat",
            bd=6
        )
        self.password_input.pack(fill="x", pady=(4, 24))

        # Allow pressing ENTER to log in (instead of clicking the button)
        self.password_input.bind("<Return>", lambda event: self._do_login())
        # bind() means: "when this key is pressed, run this function"
        # lambda event: is needed because bind() always passes an event object

        # ── LOGIN button ──────────────────────────
        login_button = tk.Button(
            card,
            text="⚔  LOGIN",
            font=("Courier New", 12, "bold"),
            bg=RED_ACCENT,
            fg="white",
            activebackground="#c73652",   # colour when you hover/click the button
            relief="flat",
            cursor="hand2",               # changes mouse pointer to a hand (like a link)
            pady=8,
            command=self._do_login        # call this function when clicked
        )
        login_button.pack(fill="x", pady=(0, 10))

        # ── REGISTER button ───────────────────────
        register_button = tk.Button(
            card,
            text="✦  Create New Account",
            font=("Courier New", 11),
            bg=CARD_BG,
            fg=GOLD,
            activebackground=INPUT_BG,
            relief="flat",
            cursor="hand2",
            pady=6,
            command=self._do_register
        )
        register_button.pack(fill="x")

        # ── Hint text at the bottom ───────────────
        hint = tk.Label(
            self.window,
            text="First time here? Click 'Create New Account'",
            font=("Courier New", 9),
            bg=DARK_BG,
            fg="#555577"   # dim grey - not important info
        )
        hint.pack(pady=20)


    # ── The functions that run when buttons are clicked ──────

    def _do_login(self):
        # This runs when the user clicks LOGIN (or presses Enter).

        # .get() reads what the user typed into the input box
        # .strip() removes any accidental spaces at start/end
        username = self.username_input.get().strip()
        password = self.password_input.get().strip()

        # Check they didn't leave either field empty
        if username == "" or password == "":
            messagebox.showwarning(
                "Missing Info",                         # pop-up window title
                "Please enter your username and password."  # message inside it
            )
            return  # stop the function here, don't try to log in

        # Ask the database if this username + password combo exists
        user = database.login_user(username, password)
        # user = None  means wrong credentials
        # user = (id, username, xp, level)  means success!

        if user is None:
            # Login failed - show an error
            messagebox.showerror(
                "Wrong Details",
                "Username or password is incorrect.\nPlease try again."
            )
        else:
            # Login worked! Call the function we were given in __init__
            self.after_login(user)


    def _do_register(self):
        # This runs when the user clicks "Create New Account"

        username = self.username_input.get().strip()
        password = self.password_input.get().strip()

        # Validation: both fields must be filled in
        if username == "" or password == "":
            messagebox.showwarning("Missing Info", "Please fill in both fields.")
            return

        # Validation: password should be at least 4 characters
        if len(password) < 4:
            messagebox.showwarning(
                "Password Too Short",
                "Your password needs at least 4 characters."
            )
            return

        # Ask the database to create the account
        success = database.register_user(username, password)

        if success:
            messagebox.showinfo(
                "Account Created! ✦",
                f"Welcome, {username}!\nYour account has been created.\nYou can now log in."
            )
            # Note: we don't auto-login. The user presses Login themselves.
        else:
            messagebox.showerror(
                "Username Taken",
                f"Sorry, '{username}' is already taken.\nPlease choose a different username."
            )
