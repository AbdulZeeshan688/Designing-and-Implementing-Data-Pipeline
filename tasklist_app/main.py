# ============================================================
#  main.py
#  This file creates the MAIN WINDOW - the quest board.
#  This is what the user sees AFTER logging in.
#  It shows their tasks and lets them add/edit/delete/complete them.
# ============================================================

import tkinter as tk
from tkinter import messagebox
import database                    # our database.py

# ── Same colour palette as login.py ────────────────────────
DARK_BG    = "#1a1a2e"
CARD_BG    = "#16213e"
RED_ACCENT = "#e94560"
LIGHT_TEXT = "#eaeaea"
GOLD       = "#f5a623"
INPUT_BG   = "#0f3460"
GREEN      = "#4ade80"    # for Easy tasks
YELLOW     = "#facc15"    # for Medium tasks
RED        = "#f87171"    # for Hard tasks
DIM_GREY   = "#555577"    # for completed tasks


class QuestBoard:
    """
    The main screen after login.
    Shows the user's quests (tasks) and lets them manage them.
    """

    def __init__(self, window, user_info):
        # user_info is the tuple from database.login_user()
        # It looks like: (1, "Ahmed", 50, 1)
        #                  id  name   xp  level

        self.window   = window
        self.user_id  = user_info[0]    # the number ID of this user
        self.username = user_info[1]    # their name e.g. "Ahmed"
        self.xp       = user_info[2]    # their XP e.g. 50
        self.level    = user_info[3]    # their level e.g. 1

        # This will store which task is currently selected in the list
        # We'll fill it in when the user clicks a task
        self.selected_task_id = None

        # This stores a copy of the tasks currently shown on screen
        # Format: { list_position: (id, title, desc, difficulty, status, due_date) }
        self.task_map = {}

        # ── Set up the window ────────────────────
        self.window.title(f"TaskHero  –  {self.username}'s Quest Board")
        self.window.configure(bg=DARK_BG)
        self.window.geometry("780x600")

        # Build all the visual parts
        self.build_header()
        self.build_filter_buttons()
        self.build_task_list()
        self.build_action_buttons()
        self.build_detail_area()

        # Load tasks from the database and show them
        self.load_and_show_tasks()


    # ============================================================
    #  BUILDING THE SCREEN - each method builds one section
    # ============================================================

    def build_header(self):
        # Top bar: app name, username, and level badge

        top_bar = tk.Frame(self.window, bg=CARD_BG, pady=10)
        top_bar.pack(fill="x")  # fill="x" stretches it all the way across

        # App title on the left
        tk.Label(
            top_bar,
            text="⚔  TASKHERO",
            font=("Courier New", 17, "bold"),
            bg=CARD_BG,
            fg=GOLD
        ).pack(side="left", padx=18)

        # Level badge on the right
        self.level_badge = tk.Label(
            top_bar,
            text=f"LVL {self.level}",
            font=("Courier New", 10, "bold"),
            bg=RED_ACCENT,
            fg="white",
            padx=8, pady=2
        )
        self.level_badge.pack(side="right", padx=(6, 18))
        # side="right" pushes it to the right side

        # Username next to the badge
        tk.Label(
            top_bar,
            text=f"Hero: {self.username}",
            font=("Courier New", 11),
            bg=CARD_BG,
            fg=LIGHT_TEXT
        ).pack(side="right")

        # ── XP Progress Bar ──────────────────────
        xp_row = tk.Frame(self.window, bg=DARK_BG, pady=5)
        xp_row.pack(fill="x", padx=18)

        xp_in_this_level = self.xp % 100   # e.g. if xp=150, they're 50% into level 2
        xp_needed        = 100             # 100 XP needed per level

        # Text showing XP numbers
        self.xp_text = tk.Label(
            xp_row,
            text=f"XP: {self.xp}  —  {xp_needed - xp_in_this_level} XP until next level",
            font=("Courier New", 9),
            bg=DARK_BG,
            fg=DIM_GREY
        )
        self.xp_text.pack(anchor="w")

        # Canvas = a drawing area. We draw the progress bar on it.
        self.xp_bar_canvas = tk.Canvas(
            xp_row,
            height=8,
            bg=INPUT_BG,
            highlightthickness=0   # removes the border around the canvas
        )
        self.xp_bar_canvas.pack(fill="x", pady=(3, 0))
        # We draw the actual coloured bar AFTER the window loads (in update_xp_bar)
        self.window.after(100, self.update_xp_bar)
        # after(100, ...) = wait 100ms then call update_xp_bar
        # This is needed because we need the canvas to be drawn first to know its width


    def update_xp_bar(self):
        # Draws/redraws the gold bar inside the XP canvas
        xp_in_this_level = self.xp % 100
        self.xp_bar_canvas.delete("all")          # clear any old bar
        full_width  = self.xp_bar_canvas.winfo_width()  # how many pixels wide the canvas is
        bar_width   = int(full_width * (xp_in_this_level / 100))  # how wide the gold part should be
        self.xp_bar_canvas.create_rectangle(
            0, 0, bar_width, 8,    # x1, y1, x2, y2
            fill=GOLD,
            outline=""             # no border on the rectangle
        )


    def build_filter_buttons(self):
        # Row of radio buttons to filter tasks: All / Active / Completed

        filter_row = tk.Frame(self.window, bg=DARK_BG, pady=8)
        filter_row.pack(fill="x", padx=18)

        tk.Label(
            filter_row,
            text="Show:",
            font=("Courier New", 10),
            bg=DARK_BG,
            fg=DIM_GREY
        ).pack(side="left", padx=(0, 8))

        # StringVar = a special variable that Tkinter widgets can "watch"
        # When it changes, the radio buttons update automatically
        self.filter_choice = tk.StringVar(value="All")

        for option in ["All", "Active", "Completed"]:
            tk.Radiobutton(
                filter_row,
                text=option,
                variable=self.filter_choice,   # all three buttons share this variable
                value=option,                  # this button's value
                font=("Courier New", 10),
                bg=DARK_BG,
                fg=LIGHT_TEXT,
                selectcolor=INPUT_BG,          # background of the selected dot
                activebackground=DARK_BG,
                cursor="hand2",
                command=self.load_and_show_tasks   # reload tasks when filter changes
            ).pack(side="left", padx=5)


    def build_task_list(self):
        # The main list of tasks in the middle of the screen

        list_area = tk.Frame(self.window, bg=DARK_BG)
        list_area.pack(fill="both", expand=True, padx=18, pady=(0, 4))
        # expand=True means this section grows if the window is made bigger

        # Column headers row
        headers = tk.Frame(list_area, bg=CARD_BG)
        headers.pack(fill="x")

        # We create a label for each column header
        for header_text, col_width in [("Diff.", 6), ("Task Name", 38), ("Due Date", 14), ("Status", 10)]:
            tk.Label(
                headers,
                text=f"  {header_text}",
                font=("Courier New", 9, "bold"),
                bg=CARD_BG,
                fg=DIM_GREY,
                anchor="w",       # align text to the left within the label
                width=col_width
            ).pack(side="left", pady=4)

        # Listbox container (to hold listbox + scrollbar side by side)
        list_container = tk.Frame(list_area, bg=DARK_BG)
        list_container.pack(fill="both", expand=True)

        # Scrollbar on the right side
        scrollbar = tk.Scrollbar(list_container)
        scrollbar.pack(side="right", fill="y")

        # The actual listbox - this is where tasks appear
        self.task_listbox = tk.Listbox(
            list_container,
            font=("Courier New", 11),
            bg=INPUT_BG,
            fg=LIGHT_TEXT,
            selectbackground=RED_ACCENT,  # highlight colour when an item is selected
            selectforeground="white",
            activestyle="none",           # removes underline on active item
            relief="flat",
            bd=0,
            yscrollcommand=scrollbar.set  # connect the scrollbar to this listbox
        )
        self.task_listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)  # connect listbox scrolling to scrollbar

        # When the user clicks on a task, run _on_task_clicked
        self.task_listbox.bind("<<ListboxSelect>>", self._on_task_clicked)
        # Double click = open edit window
        self.task_listbox.bind("<Double-Button-1>", lambda e: self._open_edit_window())


    def build_action_buttons(self):
        # The row of buttons at the bottom: Add, Edit, Complete, Delete, Logout

        button_bar = tk.Frame(self.window, bg=CARD_BG, pady=10)
        button_bar.pack(fill="x")

        # Shared styling for all buttons
        button_style = dict(
            font=("Courier New", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6
        )

        # ADD button - always active
        tk.Button(
            button_bar,
            text="✦ Add",
            bg=GREEN,
            fg="#111111",   # dark text on bright background
            command=self._open_add_window,
            **button_style   # "**" unpacks the dictionary as keyword arguments
        ).pack(side="left", padx=(18, 5))

        # EDIT button - only active when a task is selected
        self.edit_btn = tk.Button(
            button_bar,
            text="✎ Edit",
            bg=YELLOW,
            fg="#111111",
            command=self._open_edit_window,
            state="disabled",   # greyed out by default
            **button_style
        )
        self.edit_btn.pack(side="left", padx=5)

        # COMPLETE button - only active for Active tasks
        self.complete_btn = tk.Button(
            button_bar,
            text="✔ Complete",
            bg=GOLD,
            fg="#111111",
            command=self._complete_task,
            state="disabled",
            **button_style
        )
        self.complete_btn.pack(side="left", padx=5)

        # DELETE button - only active when a task is selected
        self.delete_btn = tk.Button(
            button_bar,
            text="✖ Delete",
            bg=RED_ACCENT,
            fg="white",
            command=self._delete_task,
            state="disabled",
            **button_style
        )
        self.delete_btn.pack(side="left", padx=5)

        # LOGOUT button - goes to the far right
        tk.Button(
            button_bar,
            text="⇦ Logout",
            bg=CARD_BG,
            fg=DIM_GREY,
            command=self._logout,
            **button_style
        ).pack(side="right", padx=18)


    def build_detail_area(self):
        # Small section at the very bottom showing the selected task's description

        detail_frame = tk.Frame(self.window, bg=DARK_BG)
        detail_frame.pack(fill="x", padx=18, pady=(0, 14))

        tk.Label(
            detail_frame,
            text="Details:",
            font=("Courier New", 9, "bold"),
            bg=DARK_BG,
            fg=DIM_GREY
        ).pack(anchor="w")

        self.detail_text = tk.Label(
            detail_frame,
            text="Click on a quest to see its description here.",
            font=("Courier New", 10),
            bg=DARK_BG,
            fg=DIM_GREY,
            anchor="w",
            justify="left",
            wraplength=720   # text wraps after 720px
        )
        self.detail_text.pack(anchor="w")


    # ============================================================
    #  LOADING DATA FROM DATABASE
    # ============================================================

    def load_and_show_tasks(self):
        # Clears the listbox and reloads all tasks from the database.
        # Called on startup and every time something changes.

        # Clear the listbox completely
        self.task_listbox.delete(0, "end")
        # 0 = start from the first item, "end" = delete until the last

        # Reset selection
        self.selected_task_id = None
        self.task_map = {}
        self.detail_text.config(text="Click on a quest to see its description here.")
        self._update_button_states(task_selected=False, is_active=False)

        # Get the current filter value (All / Active / Completed)
        current_filter = self.filter_choice.get()

        # Ask the database for all tasks matching this filter
        tasks = database.get_all_tasks(self.user_id, current_filter)

        if not tasks:
            # No tasks found - show a helpful message
            self.task_listbox.insert("end", "  No quests here. Add one to get started!")
            self.task_listbox.itemconfig(0, fg=DIM_GREY)
            return

        # Loop through every task and add it to the listbox
        for position, task in enumerate(tasks):
            task_id, title, description, difficulty, status, due_date = task
            # We unpack the tuple into named variables - much easier to read!

            # Save a reference so we can look up task details when user clicks it
            self.task_map[position] = task

            # Format the difficulty as a short tag: [E] [M] [H]
            diff_short = f"[{difficulty[0]}]"   # difficulty[0] = first letter
            # e.g. "Easy"[0] = "E"

            # Check mark for completed, circle for active
            status_icon = "✔" if status == "Completed" else "○"

            # Format the due date (show "-" if empty)
            due = due_date if due_date else "–"

            # Build the text line that appears in the listbox
            # Numbers after :<> control padding/alignment
            line = f"  {diff_short:<6} {title:<37} {due:<14} {status_icon}"

            self.task_listbox.insert("end", line)

            # Colour code each row based on difficulty or completion
            if status == "Completed":
                self.task_listbox.itemconfig(position, fg=DIM_GREY)
            elif difficulty == "Easy":
                self.task_listbox.itemconfig(position, fg=GREEN)
            elif difficulty == "Medium":
                self.task_listbox.itemconfig(position, fg=YELLOW)
            elif difficulty == "Hard":
                self.task_listbox.itemconfig(position, fg=RED)


    # ============================================================
    #  EVENT HANDLERS - what happens when user interacts
    # ============================================================

    def _on_task_clicked(self, event=None):
        # Runs whenever the user clicks a row in the listbox.
        # "event" is passed automatically by Tkinter (we don't use it directly).

        # Get which row is selected (returns a tuple like (2,) or empty ())
        selection = self.task_listbox.curselection()

        if not selection:
            return  # nothing selected, do nothing

        position = selection[0]  # the index (0, 1, 2...) of the clicked row

        if position not in self.task_map:
            return  # clicked on the empty message, not a real task

        # Get the task data for this row
        task = self.task_map[position]
        task_id, title, description, difficulty, status, due_date = task

        # Remember which task is selected
        self.selected_task_id = task_id

        # Show the description at the bottom
        desc_to_show = description if description else "(no description)"
        self.detail_text.config(
            text=f"{title}  |  Difficulty: {difficulty}  |  Due: {due_date or '–'}\n{desc_to_show}"
        )

        # Enable or disable buttons based on the task's status
        self._update_button_states(
            task_selected=True,
            is_active=(status == "Active")
        )


    def _update_button_states(self, task_selected, is_active):
        # Enables/disables buttons based on what's selected.
        # task_selected = True if any task is clicked
        # is_active     = True if the selected task has status "Active"

        # Edit and Delete work on any selected task
        if task_selected:
            self.edit_btn.config(state="normal")
            self.delete_btn.config(state="normal")
        else:
            self.edit_btn.config(state="disabled")
            self.delete_btn.config(state="disabled")

        # Complete only works on Active tasks (can't complete a completed task!)
        if task_selected and is_active:
            self.complete_btn.config(state="normal")
        else:
            self.complete_btn.config(state="disabled")


    # ============================================================
    #  ACTIONS - what happens when buttons are clicked
    # ============================================================

    def _open_add_window(self):
        # Opens a small pop-up window for adding a new task.

        # We create a new Toplevel (a second window)
        add_window = tk.Toplevel(self.window)
        add_window.title("New Quest")
        add_window.configure(bg=DARK_BG)
        add_window.geometry("440x460")
        add_window.resizable(False, False)
        add_window.grab_set()   # makes the pop-up "modal" - you can't click behind it

        # Build the form inside this window
        self._build_task_form(add_window, existing_task=None)


    def _open_edit_window(self):
        # Opens the task form pre-filled with the selected task's data.

        if not self.selected_task_id:
            return  # no task selected, do nothing

        # Find the task data in our task_map
        selected_task_data = None
        for task in self.task_map.values():
            if task[0] == self.selected_task_id:
                selected_task_data = task
                break

        if not selected_task_data:
            return

        edit_window = tk.Toplevel(self.window)
        edit_window.title("Edit Quest")
        edit_window.configure(bg=DARK_BG)
        edit_window.geometry("440x460")
        edit_window.resizable(False, False)
        edit_window.grab_set()

        self._build_task_form(edit_window, existing_task=selected_task_data)


    def _build_task_form(self, form_window, existing_task):
        # Builds the task add/edit form inside a given window.
        # If existing_task is None = adding new task.
        # If existing_task is a tuple = editing existing task.

        is_editing = existing_task is not None

        # Title of the form
        heading = "✎  EDIT QUEST" if is_editing else "✦  NEW QUEST"
        tk.Label(
            form_window,
            text=heading,
            font=("Courier New", 15, "bold"),
            bg=DARK_BG,
            fg=GOLD
        ).pack(pady=(22, 14))

        # The form card
        card = tk.Frame(form_window, bg=CARD_BG, padx=24, pady=20)
        card.pack(fill="both", expand=True, padx=22, pady=(0, 22))

        # --- Task Title ---
        tk.Label(card, text="Quest Title *", font=("Courier New", 10, "bold"),
                 bg=CARD_BG, fg=LIGHT_TEXT).pack(anchor="w")

        title_input = tk.Entry(
            card, font=("Courier New", 12),
            bg=INPUT_BG, fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT,
            relief="flat", bd=6
        )
        title_input.pack(fill="x", pady=(4, 12))

        # --- Description ---
        tk.Label(card, text="Description (optional)", font=("Courier New", 10, "bold"),
                 bg=CARD_BG, fg=LIGHT_TEXT).pack(anchor="w")

        desc_input = tk.Text(
            card, font=("Courier New", 11),
            bg=INPUT_BG, fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT,
            relief="flat", bd=6, height=3
        )
        desc_input.pack(fill="x", pady=(4, 12))

        # --- Difficulty (radio buttons) ---
        tk.Label(card, text="Difficulty", font=("Courier New", 10, "bold"),
                 bg=CARD_BG, fg=LIGHT_TEXT).pack(anchor="w")

        difficulty_var = tk.StringVar(value="Easy")
        diff_row = tk.Frame(card, bg=CARD_BG)
        diff_row.pack(fill="x", pady=(4, 12))

        diff_colours = {"Easy": GREEN, "Medium": YELLOW, "Hard": RED}
        diff_xp      = {"Easy": "+10 XP", "Medium": "+25 XP", "Hard": "+50 XP"}

        for diff in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(
                diff_row,
                text=f"{diff} ({diff_xp[diff]})",
                variable=difficulty_var,
                value=diff,
                font=("Courier New", 10),
                bg=CARD_BG,
                fg=diff_colours[diff],
                selectcolor=INPUT_BG,
                activebackground=CARD_BG,
                cursor="hand2"
            ).pack(side="left", padx=(0, 12))

        # --- Due Date (simple text entry - no extra library needed) ---
        tk.Label(card, text="Due Date (e.g. 15.06.2025)", font=("Courier New", 10, "bold"),
                 bg=CARD_BG, fg=LIGHT_TEXT).pack(anchor="w")

        due_input = tk.Entry(
            card, font=("Courier New", 12),
            bg=INPUT_BG, fg=LIGHT_TEXT, insertbackground=LIGHT_TEXT,
            relief="flat", bd=6
        )
        due_input.pack(fill="x", pady=(4, 16))

        # If we're editing, fill in the existing values
        if is_editing:
            _, title, description, difficulty, status, due_date = existing_task
            title_input.insert(0, title)                    # 0 = insert at the start
            desc_input.insert("1.0", description)           # "1.0" = line 1, char 0
            difficulty_var.set(difficulty)
            due_input.insert(0, due_date)

        # --- Save button ---
        save_label = "💾  Save Changes" if is_editing else "⚔  Add Quest"
        tk.Button(
            card,
            text=save_label,
            font=("Courier New", 12, "bold"),
            bg=RED_ACCENT,
            fg="white",
            activebackground="#c73652",
            relief="flat",
            cursor="hand2",
            pady=8,
            command=lambda: self._save_task(
                form_window,
                title_input.get().strip(),
                desc_input.get("1.0", "end").strip(),
                difficulty_var.get(),
                due_input.get().strip(),
                is_editing
            )
            # lambda: lets us pass arguments to the function
        ).pack(fill="x")


    def _save_task(self, form_window, title, description, difficulty, due_date, is_editing):
        # Runs when the Save button is clicked inside the task form.

        if not title:
            messagebox.showwarning("Missing Title", "Please give your quest a name!", parent=form_window)
            return

        if is_editing:
            # Update the existing task in the database
            database.edit_task(self.selected_task_id, title, description, difficulty, due_date)
        else:
            # Add a brand new task to the database
            database.add_task(self.user_id, title, description, difficulty, due_date)
            messagebox.showinfo("Quest Added!", f"'{title}' added to your quest board!")

        form_window.destroy()   # close the pop-up window
        self.load_and_show_tasks()   # refresh the list to show the changes


    def _complete_task(self):
        # Marks the selected task as done and gives the user XP.

        if not self.selected_task_id:
            return

        # Find the task data to get its difficulty
        task_title      = ""
        task_difficulty = "Easy"
        for task in self.task_map.values():
            if task[0] == self.selected_task_id:
                task_title      = task[1]
                task_difficulty = task[3]
                break

        # Mark as complete in the database
        database.mark_task_complete(self.selected_task_id)

        # Add XP to the user - returns new totals
        new_xp, new_level, leveled_up = database.add_xp_to_user(self.user_id, task_difficulty)

        # Update our local variables
        self.xp    = new_xp
        self.level = new_level

        # Refresh the XP display in the header
        xp_in_level = self.xp % 100
        self.xp_text.config(
            text=f"XP: {self.xp}  —  {100 - xp_in_level} XP until next level"
        )
        self.level_badge.config(text=f"LVL {self.level}")
        self.update_xp_bar()

        # Reload the task list
        self.load_and_show_tasks()

        # XP amounts per difficulty
        xp_earned = {"Easy": 10, "Medium": 25, "Hard": 50}

        if leveled_up:
            # Special message for leveling up!
            messagebox.showinfo(
                "⭐  LEVEL UP!",
                f"You completed: '{task_title}'\n"
                f"+{xp_earned[task_difficulty]} XP earned!\n\n"
                f"🌟 You are now LEVEL {new_level}! 🌟\n"
                f"Total XP: {new_xp}"
            )
        else:
            messagebox.showinfo(
                "✔  Quest Done!",
                f"'{task_title}' is complete!\n"
                f"+{xp_earned[task_difficulty]} XP earned.\n"
                f"Total XP: {new_xp}"
            )


    def _delete_task(self):
        # Deletes the selected task after asking for confirmation.

        if not self.selected_task_id:
            return

        # Find the task title for the confirmation message
        task_title = ""
        for task in self.task_map.values():
            if task[0] == self.selected_task_id:
                task_title = task[1]
                break

        # Ask the user to confirm before deleting
        confirmed = messagebox.askyesno(
            "Delete Quest?",
            f"Are you sure you want to delete:\n\n'{task_title}'?\n\nThis cannot be undone."
        )

        if confirmed:
            database.delete_task(self.selected_task_id)
            self.load_and_show_tasks()   # refresh the list


    def _logout(self):
        # Closes the quest board and goes back to the login screen.

        # We import here to avoid a circular import issue at the top of the file
        from login import LoginScreen

        # Remove all widgets from the window
        for widget in self.window.winfo_children():
            widget.destroy()

        # Make the window small again (login size)
        self.window.geometry("420x540")

        # Show the login screen again
        LoginScreen(self.window, self._after_relogin)


    def _after_relogin(self, user_info):
        # Called when someone logs in from the logout screen.
        # Clears the login screen and opens a new quest board.

        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.geometry("780x600")
        QuestBoard(self.window, user_info)
