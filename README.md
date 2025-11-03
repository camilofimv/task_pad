# 🧩 TaskPad

A lightweight task manager built with **Flask**, **PostgreSQL**, and **HTMX** — developed as a learning project to understand full-stack web development and deployment.

---

## 🚀 Features

- Create, view, update, and delete tasks
- Live updates using HTMX (no page reloads)
- PostgreSQL database for data persistence
- Flask backend with RESTful routes
- Simple responsive UI

---

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| Backend | Flask (Python) |
| Database | PostgreSQL |
| Frontend | Jinja Templates + HTMX |
| Styling | CSS (vanilla) |
| Hosting | Render (for both app and DB) |

---

## ⚙️ Getting Started (Local Setup)

1. **Clone the repository**
   ```bash
   git clone https://github.com/camilovelezcorrea/task_pad.git
   cd task_pad
Create and activate a virtual environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Create a local PostgreSQL database

bash
Copy code
createdb taskpad_dev
Set up your .env file

ini
Copy code
DATABASE_URL=postgresql://<your-username>@localhost:5432/taskpad_dev
Run the app

bash
Copy code
python run.py
Visit → http://127.0.0.1:5000

🌍 Deployment
This app can be deployed on Render (free tier) with a managed PostgreSQL instance.

Add DATABASE_URL to Render’s environment variables.

Use the command:

nginx
Copy code
gunicorn 'app:create_app()'
(we’ll set this up in Module 5.3)

🧠 Learning Objectives
This project demonstrates:

Flask app structure and routing

REST API design

Database integration (PostgreSQL)

Server-side rendering with Jinja

Client-side interactivity with HTMX

Environment-based configuration and deployment

📸 Screenshots (optional)
Add here once deployed.

✨ Author
Camilo Vélez Correa
Technical Program Manager | Aspiring Full-Stack Developer
LinkedIn • GitHub
