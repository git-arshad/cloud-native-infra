from flask import Flask
import os
import datetime

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV","development")
APP_VERSION = os.getenv("APP_VERSION","1.0")
PORT = int(os.getenv("PORT",5000))

def log_request(endpoint):
    timestamp = datetime.datetime.utcnow().isoformat()
    print(f"[{timestamp}] Request recieved at {endpoint}",flush=True)
    

@app.route("/")
def home():
    log_request("/")
    return f"""
InfraReady Service\n
Environment: (APP_ENV)
Version: {APP_VERSION}
"""

@app.route("/health")
def health():
    log_request("/health")
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)