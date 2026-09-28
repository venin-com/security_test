from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def user():
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    return str(cursor.fetchall())