from flask import Flask, request
import hashlib
import os
import subprocess
import pickle
import random

app = Flask(__name__)

# Vulnerability 1 - Hardcoded password
DB_PASSWORD = "Admin123!"

# Vulnerability 2 - Hardcoded API key
API_KEY = "AKIAIOSFODNN7EXAMPLE"


@app.route("/")
def home():
    return "Week 10 DevSecOps Vulnerable Application"


# Vulnerability 3 - Weak hashing (MD5)
@app.route("/hash")
def hash_password():
    password = request.args.get("password", "")
    return hashlib.md5(password.encode()).hexdigest()


# Vulnerability 4 - Command Injection
@app.route("/list")
def list_files():
    directory = request.args.get("dir", "")
    os.system("ls " + directory)
    return "Done"


# Vulnerability 5 - subprocess(shell=True)
@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    subprocess.call(f"ping -c 1 {host}", shell=True)
    return "Ping sent"


# Vulnerability 6 - Unsafe pickle
@app.route("/load")
def load_pickle():
    data = request.args.get("data", "").encode()
    pickle.loads(data)
    return "Loaded"


# Vulnerability 7 - Weak random token
@app.route("/token")
def token():
    return str(random.random())


if __name__ == "__main__":
    app.run(debug=True)
