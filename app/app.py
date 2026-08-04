from flask import Flask, request
import hashlib
import os
import subprocess
import random
import pickle

app = Flask(__name__)

# Vulnerability 1: Hardcoded password
ADMIN_PASSWORD = "SuperSecretPassword123"


# Vulnerability 2: Hardcoded API key
API_KEY = "AKIAIOSFODNN7EXAMPLE"


# Vulnerability 3: Weak cryptography (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# Vulnerability 4: Command injection using os.system()
@app.route("/ping")
def ping():
    host = request.args.get("host")

    command = "ping -c 1 " + host

    output = os.system(command)

    return f"Command executed: {output}"


# Vulnerability 5: Command injection using subprocess shell=True
@app.route("/backup")
def backup():
    filename = request.args.get("file")

    result = subprocess.check_output(
        "cat " + filename,
        shell=True
    )

    return result


# Vulnerability 6: Unsafe eval()
@app.route("/calculate")
def calculate():
    expression = request.args.get("expression")

    result = eval(expression)

    return str(result)


# Vulnerability 7: Weak random token generation
@app.route("/token")
def token():
    token = random.random()

    return str(token)


# Vulnerability 8: Unsafe deserialization
@app.route("/load")
def load():
    data = request.args.get("data")

    obj = pickle.loads(data.encode())

    return str(obj)


@app.route("/")
def home():
    return "PayliteNG Vulnerable Flask Application"


if __name__ == "__main__":
    app.run(debug=True)
