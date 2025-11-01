# 🧭 Command Literacy Cheat Sheet  
_For macOS, zsh, and VS Code Terminal_

Learn concepts, not rote commands — this guide focuses on what each command **means** and **why** it matters.

---

## 🗂️ File & Folder Navigation

| Command | Concept | Example & Explanation |
|----------|----------|-----------------------|
| `pwd` | “Where am I?” | Shows your **current working directory**. |
| `ls` | “What’s here?” | Lists files/folders in the current directory. |
| `ls -l` | “Show me details.” | Displays permissions, owner, size, date. |
| `ls -a` | “Include hidden files.” | Shows files that start with a dot (like `.zshrc`). |
| `cd foldername` | “Go into that folder.” | Example: `cd app`. |
| `cd ..` | “Go up one level.” | Moves back to the parent folder. |
| `cd ~` | “Go home.” | Takes you to `/Users/yourname`. |
| `mkdir foldername` | “Make a folder.” | Example: `mkdir app/templates`. |
| `touch filename` | “Create an empty file.” | Example: `touch app/routes.py`. |

**💡 Concept takeaway:**  
You “move around” your computer’s filesystem with words instead of clicks.

---

## ⚙️ File Operations

| Command | Concept | Example & Explanation |
|----------|----------|-----------------------|
| `cp fileA fileB` | Copy files. | Example: `cp .env.example .env`. |
| `mv fileA folder/` | Move or rename something. | Example: `mv README.md docs/`. |
| `rm file` | Delete a file. | Use carefully. |
| `rm -r folder` | Delete a folder (recursively). | `-r` = “go inside subfolders.” |
| `cat filename` | Read a file’s contents. | Quick preview of text. |
| `open .` | Open this folder in Finder. | macOS shortcut. |

---

## 🧑‍💻 Development Essentials

| Command | Concept | Example & Explanation |
|----------|----------|-----------------------|
| `python3 --version` | Check Python version. | Verifies your Python install. |
| `python3 -m venv venv` | Create a virtual environment. | Isolates project dependencies. |
| `source venv/bin/activate` | Activate your virtual environment. | Prepares Python for local packages. |
| `pip install flask` | Install a Python package. | Downloads from PyPI. |
| `pip freeze > requirements.txt` | Record dependencies. | Saves your environment for teammates. |
| `deactivate` | Exit the virtual environment. | Returns to your system Python. |

**💡 Concept takeaway:**  
A *virtual environment* is like a sandbox — each project has its own packages.

---

## 🧩 Git & GitHub (Version Control)

| Command | Concept | Example & Explanation |
|----------|----------|-----------------------|
| `git init` | Start version control here. | Creates a `.git` folder. |
| `git status` | “What’s changed?” | Lists modified/untracked files. |
| `git add .` | Stage files for commit. | Prepares for a snapshot. |
| `git commit -m "message"` | Save a version checkpoint. | Adds a labeled point in history. |
| `git log --oneline` | Show recent commits. | Compact history. |
| `git remote add origin URL` | Link to GitHub. | Connect local repo to GitHub. |
| `git push -u origin main` | Upload to GitHub. | Shares your code. |
| `git pull` | Get latest from GitHub. | Keeps in sync. |

**💡 Concept takeaway:**  
Git = “time machine for your code.” Track, rewind, or branch off safely.

---

## 🐘 PostgreSQL Basics

| Command | Concept | Example & Explanation |
|----------|----------|-----------------------|
| `psql` | Enter Postgres shell. | Write SQL directly. |
| `\l` | List databases. | Shows all DBs. |
| `\c dbname` | Connect to a database. | Switch DBs. |
| `\dt` | List tables. | Shows tables in current DB. |
| `CREATE DATABASE name;` | Make a new database. | Creates a fresh schema. |
| `\q` | Quit psql. | Exit SQL shell. |

**💡 Concept takeaway:**  
PostgreSQL stores your data. You can talk to it directly via `psql` or through your app.

---

## 🧩 System Awareness

| Command | Concept | Example & Explanation |
|----------|----------|-----------------------|
| `which command` | “Where is this installed?” | Example: `which python3`. |
| `echo $SHELL` | See which shell you’re using. | Should return `/bin/zsh`. |
| `echo $PATH` | Show where shell looks for programs. | Useful for fixing “command not found.” |
| `chmod u+w file` | Give yourself write permission. | Example: `chmod u+w ~/.zshrc`. |
| `sudo command` | Run as admin (superuser). | Asks for your Mac password. |

**💡 Concept takeaway:**  
These commands help you *understand* your system — essential for debugging.

---

## 🧠 Learning Philosophy

1. **Pattern recognition beats memorization.**  
   - Notice how `--version` or `--help` appear across tools.

2. **Muscle memory, not flashcards.**  
   - Repetition (like `cd`, `ls`, `git status`) builds intuition.

3. **Understand intent.**  
   - Ask: What am I trying to do? What’s the object? What options am I using?

4. **The terminal is a conversation, not a test.**  
   - Mistakes = feedback, not failure.

---

### 💬 Quick Debugging Tips
- When something says “command not found,” check:
  - `which <command>` → Is it installed?
  - `echo $PATH` → Does your shell know where to find it?
- When something says “permission denied,” check:
  - `ls -l <file>` → Who owns it?
  - Use `chmod` or `chown` only when you understand why.

---

### ✨ How to Use This Cheat Sheet
- Keep it open in VS Code while working through tutorials.
- Use **Cmd + F** to quickly find a concept.
- Add your own notes and examples as you learn new commands.

---

**Next:**  
With this command literacy in place, you’ll understand what each step means as we install and integrate PostgreSQL into your Flask app in **Module 2**.

---
