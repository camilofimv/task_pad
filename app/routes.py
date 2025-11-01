from flask import Blueprint, jsonify, request, render_template, url_for, redirect
from app.db import get_db

bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
    db = get_db()
    with db.cursor() as cur:
        cur.execute(
            "SELECT id, title, done, created_at FROM tasks ORDER BY created_at DESC;"
        )
        rows = cur.fetchall()
    # rows are tuples: (id, title, done, created_at)
    return render_template("index.html", tasks=rows)


@bp.route("/health")
def health():
    return jsonify({"status": "OK"}), 200


@bp.route("/tasks", methods=["GET"])
def list_tasks():
    db = get_db()
    with db.cursor() as cur:
        cur.execute("""
            SELECT id, title, done, created_at
            FROM tasks
            ORDER BY created_at DESC
        """)
        rows = cur.fetchall()

    tasks = [
        {
            "id": r[0],
            "title": r[1],
            "done": r[2],
            "created_at": (r[3].isoformat() if r[3] else None),
        }
        for r in rows
    ]
    return {"tasks": tasks}, 200


@bp.route("/tasks", methods=["POST"])
def create_task():
    # Try JSON first; fall back to form fields (HTMX/HTML)
    data = request.get_json(silent=True)
    if data is None:
        title = (request.form.get("title") or "").strip()
    else:
        title = (data.get("title") or "").strip()

    if not title:
        # For HTMX, return a small error snippet or JSON error
        if request.headers.get("HX-Request"):
            return '<li class="empty">Title is required.</li>', 400
        return {"error": "title is required"}, 400

    db = get_db()
    with db.cursor() as cur:
        cur.execute(
            "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title, done, created_at;",
            (title,),
        )
        new = cur.fetchone()
        db.commit()

    # If this is an HTMX request, return the HTML snippet for a single item
    if request.headers.get("HX-Request"):
        t = (new[0], new[1], new[2], new[3])  # (id, title, done, created_at)
        return render_template("_task_item.html", t=t), 201

    # Otherwise, API JSON or normal form redirect
    if request.is_json:
        return {
            "id": new[0],
            "title": new[1],
            "done": new[2],
            "created_at": new[3].isoformat() if new[3] else None,
        }, 201

    return redirect(url_for("routes.index"))


@bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    # If using form (HTMX), merge form fields into data
    if not data and request.form:
        data = request.form.to_dict()

    title = data.get("title")
    done = data.get("done")

    sets, params = [], []
    if title is not None:
        sets.append("title = %s")
        params.append(title.strip())
    if done is not None:
        # form sends 'true'/'false' strings; JSON sends booleans
        val = done if isinstance(done, bool) else (str(done).lower() == "true")
        sets.append("done = %s")
        params.append(val)

    if not sets:
        return {"error": "Nothing to update"}, 400
    params.append(task_id)

    db = get_db()
    with db.cursor() as cur:
        cur.execute(
            f"UPDATE tasks SET {', '.join(sets)} WHERE id = %s RETURNING id, title, done, created_at;",
            params,
        )
        row = cur.fetchone()
        if not row:
            return {"error": "Task not found"}, 404
        db.commit()

    # HTMX expects the updated HTML for the item
    if request.headers.get("HX-Request"):
        t = (row[0], row[1], row[2], row[3])
        return render_template("_task_item.html", t=t), 200

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2],
        "created_at": row[3].isoformat() if row[3] else None,
    }, 200


@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    db = get_db()
    with db.cursor() as cur:
        cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id;", (task_id,))
        row = cur.fetchone()
        if not row:
            return {"error": "Task not found"}, 404
        db.commit()
    return "", 200  # Let HTMX remove the element automatically
