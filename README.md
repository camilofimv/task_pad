# 🧩 TaskPad

TaskPad is a lightweight **Flask + PostgreSQL + HTMX** web application that I’m building as part of my personal learning journey to understand full-stack software development — from backend architecture and database design to frontend interactivity and deployment.

This project began as a guided coding-tutor exercise to help me learn the **Software Development Life Cycle (SDLC)** by doing: planning, building, testing, and deploying a real-world app from scratch.

---

## 🚀 Features

- 🧠 Create, read, update, and delete tasks (Full CRUD)
- ⚡ Instant updates using **HTMX** (no full-page reloads)
- 🗄️ Data persistence via **PostgreSQL**
- 🔧 Backend powered by **Flask**
- 💅 Clean, minimal HTML/CSS UI
- 🌍 Ready for cloud deployment on **Render**

---

## 🧱 Tech Stack

| Layer | Tool / Technology |
|-------|-------------------|
| Backend | Flask (Python) |
| Database | PostgreSQL |
| Driver / Adapter | psycopg (Postgres driver for Python) |
| Frontend | Jinja Templates + HTMX |
| Styling | Custom CSS |
| Hosting | Render (App + Managed Postgres) |
| Version Control | Git + GitHub |
| Environment Mgmt | `.env` (via python-dotenv) |

---

## ⚙️ Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/camilovelezcorrea/task_pad.git
   cd task_pad
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a local PostgreSQL database**

   ```bash
   createdb taskpad_dev
   ```

5. **Set up your environment variables**

   Create a file called `.env` in the project root:

   ```
   DATABASE_URL=postgresql://<your-username>@localhost:5432/taskpad_dev
   ```

6. **Run the Flask app**

   ```bash
   python run.py
   ```

   Then open → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌍 Deployment (Production Setup)

This app is designed to deploy easily to **Render** using a managed PostgreSQL database.

1. **Push your code to GitHub**

   ```bash
   git add .
   git commit -m "Initial commit"
   git push
   ```

2. **Create a new Web Service on Render**
   - Connect your GitHub repo  
   - Choose environment → **Python 3**
   - **Build command:**
     ```
     pip install -r requirements.txt
     ```
   - **Start command:**
     ```
     gunicorn 'app:create_app()'
     ```

3. **Add environment variables**
   - `DATABASE_URL` → use your hosted Postgres connection string  
     (Render provides this automatically if you add a Postgres service)

4. **Deploy and verify**
   - Visit your Render URL (e.g. https://taskpad-camilo.onrender.com)  
   - Add a few tasks and confirm they persist in the cloud DB

---

## 🧠 What I’m Learning Through This Project

- End-to-end **Software Development Life Cycle (SDLC)**
- How Flask routes map URLs to backend logic
- Connecting and querying data from PostgreSQL
- Using environment variables for secure configuration
- RESTful API design (GET, POST, PATCH, DELETE)
- Server-side rendering (Jinja) + client interactivity (HTMX)
- Fundamentals of deploying full-stack apps to production

---

## 🧩 Project Structure

```
task_pad/
├── app/
│   ├── __init__.py          # Initializes the Flask app
│   ├── db.py                # Database connection helper
│   ├── routes.py            # API + frontend routes
│   ├── templates/           # Jinja templates (HTML)
│   │   ├── base.html
│   │   ├── index.html
│   │   └── _task_item.html
│   └── static/              # Static files (CSS, JS)
│       └── styles.css
├── run.py                   # App entry point
├── .env                     # Environment variables (ignored by Git)
├── .gitignore               # Files to exclude from VCS
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🌱 Future Enhancements

- 🔒 Add user authentication (login / signup)  
- 🗂️ Filter & sort tasks (completed / pending)  
- 🎨 Improve styling with TailwindCSS  
- 🌍 Add deployment badge + screenshots  
- 🧰 Introduce automated tests  

---

## ✨ Author

**Camilo Vélez Correa**  
Technical Program Manager @ Apple • Aspiring Full-Stack Developer  
🎯 Focus: Building data-driven systems & learning full-stack architecture  
🌐 [LinkedIn](https://linkedin.com/in/camilovelezcorrea)  
💻 [GitHub](https://github.com/camilovelezcorrea)
