# ⚔ TaskHero – Your Personal Quest Board

A task manager with an RPG twist. Instead of boring to-do lists,
your tasks become **quests**. Finish them, earn **XP**, and level up your hero!

---

## 🎮 What Makes This Different?

Most students make a plain white Tkinter window with a list.

**TaskHero** has:
- A dark RPG theme with gold, red and navy colours
- Tasks have **difficulty levels**: Easy / Medium / Hard
- Finishing a task gives you **XP points** (10, 25, or 50)
- Earn 100 XP → your hero levels up with a celebration message!
- A visual XP progress bar in the header
- Filter tasks: show All / Active / Completed

---

## 📁 File Structure (what each file does)

```
taskhero/
 │
 ├── app.py          ← START HERE. Run this to launch the app.
 │                     Sets up the database and opens the login window.
 │
 ├── database.py     ← The "memory" of the app.
 │                     Handles everything database-related:
 │                     creating tables, saving/loading tasks, user login, XP.
 │
 ├── login.py        ← The login screen.
 │                     First window the user sees. They can log in or register.
 │
 ├── main.py         ← The main quest board.
 │                     Shows after login. Lists all tasks with
 │                     Add / Edit / Complete / Delete buttons.
 │
 └── taskhero.db     ← Created automatically when you first run the app.
                       This is the SQLite database file. Don't delete it!
```

---

## ⚙ How to Install and Run

### Step 1 – Make sure Python is installed
Go to **https://www.python.org** → Download the latest version.
During installation, **tick the box that says "Add Python to PATH"**. This is important!

### Step 2 – Check it worked
Open **Command Prompt** (Windows: search "cmd" in start menu).
Type this and press Enter:
```
python --version
```
You should see something like: `Python 3.12.0`

### Step 3 – No extra libraries needed!
This project uses only Tkinter (comes with Python) and SQLite (also built in).
No `pip install` required.

### Step 4 – Run the app
Open Command Prompt, go to your project folder, then type:
```
python app.py
```

The app will open!

---

## 🧪 How to Use the App

1. **Open the app** → you see the login screen
2. **Create an account** → click "Create New Account", enter a username and password
3. **Log in** → enter your credentials and press Login (or hit Enter)
4. **Add a quest** → click "✦ Add", fill in the title, difficulty, and due date
5. **Complete a quest** → click the task, then click "✔ Complete" to earn XP
6. **Edit a quest** → click the task, then click "✎ Edit"
7. **Delete a quest** → click the task, then click "✖ Delete"
8. **Filter your list** → use the All / Active / Completed radio buttons
9. **Logout** → click "⇦ Logout" to switch users

---

## 💡 XP and Level System

| Difficulty | XP Earned |
|------------|-----------|
| Easy       | +10 XP    |
| Medium     | +25 XP    |
| Hard       | +50 XP    |

- Every **100 XP** = 1 level up
- A special pop-up appears when you level up!
- Your XP total and level are saved in the database permanently

---

## 🗄 Database Design

The app uses **SQLite** - a lightweight database that saves everything to a single `.db` file.

**Table 1: users**
| Column   | Type    | What it stores                        |
|----------|---------|---------------------------------------|
| id       | number  | Auto-assigned ID for each user        |
| username | text    | Login name (must be unique)           |
| password | text    | Their password                        |
| xp       | number  | Total XP earned (starts at 0)         |
| level    | number  | Current hero level (starts at 1)      |

**Table 2: tasks**
| Column      | Type   | What it stores                             |
|-------------|--------|--------------------------------------------|
| id          | number | Auto-assigned ID for each task             |
| user_id     | number | Links to the user who owns this task       |
| title       | text   | The name of the quest                      |
| description | text   | Extra details (optional)                   |
| difficulty  | text   | Easy, Medium, or Hard                      |
| status      | text   | Active or Completed                        |
| due_date    | text   | Deadline date as text                      |

---

## 🐛 Common Problems & Fixes

| Problem | Fix |
|---------|-----|
| `python` not recognized | Python wasn't added to PATH during install. Reinstall and tick the box. |
| Window doesn't open | Make sure you're running `app.py`, not another file. |
| Can't log in | Double-check username and password. They are case-sensitive. |
| Database error | Delete `taskhero.db` and restart. A fresh one will be created. |

---

## 📚 Technologies Used

- **Python 3** – the programming language
- **Tkinter** – Python's built-in GUI library (no install needed)
- **SQLite** – Python's built-in mini database (no install needed)

---

*Made as a school project. Theme inspired by RPG quest boards.*
