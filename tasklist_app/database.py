# ============================================================
#  database.py
#  This file handles SAVING and LOADING data.
#  Think of it as the "memory" of our app.
#  We use SQLite - it's a mini database that saves to a file.
# ============================================================

import sqlite3  # sqlite3 comes with Python - no install needed!
                # It lets us create a database file and store data in it.


# ------------------------------------
#  STEP 1: Connect to the database
# ------------------------------------

def connect_to_database():
    # This creates a file called "taskhero.db" in your project folder.
    # If the file already exists, it just opens it.
    # Think of it like opening a notebook to write in.
    connection = sqlite3.connect("taskhero.db")
    return connection  # We return the connection so other functions can use it


# ------------------------------------
#  STEP 2: Create the tables (like Excel sheets inside the database)
# ------------------------------------

def create_tables():
    # We open the database
    connection = connect_to_database()

    # A "cursor" is like a pen - we use it to write/read from the database
    cursor = connection.cursor()

    # ----- TABLE 1: users -----
    # This table stores every person who registers in the app.
    # Each row = one user
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            xp       INTEGER DEFAULT 0,
            level    INTEGER DEFAULT 1
        )
    """)
    # "IF NOT EXISTS" means: only create it if it doesn't already exist.
    # "AUTOINCREMENT" means Python automatically gives each user a number (1, 2, 3...)
    # "UNIQUE" means two people can't have the same username
    # "DEFAULT 0" means xp starts at 0 automatically

    # ----- TABLE 2: tasks -----
    # This table stores every task/quest that users create.
    # Each row = one task
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            title       TEXT NOT NULL,
            description TEXT DEFAULT '',
            difficulty  TEXT DEFAULT 'Easy',
            status      TEXT DEFAULT 'Active',
            due_date    TEXT DEFAULT ''
        )
    """)
    # "user_id" links each task to the person who created it.
    # So when user 3 logs in, we only show tasks where user_id = 3.

    connection.commit()   # commit() = save the changes. Like pressing Save in Word.
    connection.close()    # close() = close the notebook when done.


# ------------------------------------
#  STEP 3: User functions (register & login)
# ------------------------------------

def register_user(username, password):
    # This function creates a new account.
    # It returns True if it worked, or False if the username is taken.

    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Try to insert the new user into the users table
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
            # The two "?" are placeholders. Python fills them in safely.
            # This protects against hackers. Always use ? instead of writing
            # values directly into the SQL string!
        )
        connection.commit()  # Save the new user
        connection.close()
        return True  # It worked!

    except sqlite3.IntegrityError:
        # IntegrityError happens when the username already exists (UNIQUE rule)
        connection.close()
        return False  # Username taken


def login_user(username, password):
    # This function checks if the username + password match anything in the database.
    # Returns the user's info if correct, or None if wrong.

    connection = connect_to_database()
    cursor = connection.cursor()

    # Look for a row where BOTH username AND password match
    cursor.execute(
        "SELECT id, username, xp, level FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    # fetchone() grabs ONE result row.
    # If nothing matches, user = None (meaning login failed)
    # If it matches, user = (id, username, xp, level)  e.g. (1, "Ahmed", 50, 1)

    connection.close()
    return user  # Either the user info, or None


# ------------------------------------
#  STEP 4: Task functions (add, edit, delete, get)
# ------------------------------------

def get_all_tasks(user_id, filter_status="All"):
    # Gets all tasks for a specific user.
    # filter_status can be "All", "Active", or "Completed"

    connection = connect_to_database()
    cursor = connection.cursor()

    if filter_status == "All":
        # Get every task for this user
        cursor.execute(
            "SELECT id, title, description, difficulty, status, due_date FROM tasks WHERE user_id = ?",
            (user_id,)
        )
    else:
        # Get only tasks matching the filter (Active or Completed)
        cursor.execute(
            "SELECT id, title, description, difficulty, status, due_date FROM tasks WHERE user_id = ? AND status = ?",
            (user_id, filter_status)
        )

    tasks = cursor.fetchall()
    # fetchall() gets ALL the matching rows as a list.
    # Each item in the list looks like: (id, title, description, difficulty, status, due_date)

    connection.close()
    return tasks  # Returns a list of tasks


def add_task(user_id, title, description, difficulty, due_date):
    # Saves a new task into the database

    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (user_id, title, description, difficulty, due_date) VALUES (?, ?, ?, ?, ?)",
        (user_id, title, description, difficulty, due_date)
    )

    connection.commit()  # Save it!
    connection.close()


def edit_task(task_id, new_title, new_description, new_difficulty, new_due_date):
    # Updates an existing task with new information.
    # We find the task by its id, then overwrite the old values.

    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, difficulty = ?, due_date = ? WHERE id = ?",
        (new_title, new_description, new_difficulty, new_due_date, task_id)
    )
    # UPDATE means "change existing data"
    # SET says "what to change"
    # WHERE id = ? makes sure we only change THAT specific task

    connection.commit()
    connection.close()


def delete_task(task_id):
    # Permanently removes a task from the database.

    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    # DELETE removes the row where id matches

    connection.commit()
    connection.close()


def mark_task_complete(task_id):
    # Changes the status of a task from "Active" to "Completed"

    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE tasks SET status = 'Completed' WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()


def add_xp_to_user(user_id, difficulty):
    # Gives the user XP points based on how hard the task was.
    # Easy = 10 XP, Medium = 25 XP, Hard = 50 XP

    # Dictionary = like a lookup table
    xp_table = {
        "Easy":   10,
        "Medium": 25,
        "Hard":   50
    }

    # Look up how much XP this difficulty gives
    xp_to_add = xp_table[difficulty]

    connection = connect_to_database()
    cursor = connection.cursor()

    # Get the user's current XP and level
    cursor.execute("SELECT xp, level FROM users WHERE id = ?", (user_id,))
    current_xp, current_level = cursor.fetchone()

    # Calculate new XP total
    new_xp = current_xp + xp_to_add

    # Calculate new level: go up a level for every 100 XP
    # Example: 110 XP // 100 + 1 = level 2
    new_level = (new_xp // 100) + 1

    # Save the updated XP and level back into the database
    cursor.execute(
        "UPDATE users SET xp = ?, level = ? WHERE id = ?",
        (new_xp, new_level, user_id)
    )

    connection.commit()
    connection.close()

    # Did they level up? Compare old level to new level
    leveled_up = new_level > current_level

    return new_xp, new_level, leveled_up
    # We return all three values so the main window can show a message
