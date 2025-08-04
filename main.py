import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)


USERNAME = "admin"
PASSWORD = "admin123"  

@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    pwd = request.form["password"]
    
   
    if user == USERNAME and pwd == PASSWORD:
        return "Logged in successfully!"
    else:
        return "Invalid credentials", 401

@app.route("/query")
def query():

    name = request.args.get("name")
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    query = f"SELECT * FROM users WHERE name = '{name}'"  
    cursor.execute(query)
    results = cursor.fetchall()
    return {"results": results}

@app.route("/ping")
def ping():
    host = request.args.get("host")
    # OS Command Injection vulnerability
    os.system(f"ping -c 1 {host}")  
    return "Ping executed!"

if __name__ == "__main__":
    app.run(debug=True)
