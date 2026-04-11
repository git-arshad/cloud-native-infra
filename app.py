from flask import Flask
import os
import datetime
import psycopg2

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
PORT = int(os.getenv("PORT", 5000))


def log_request(endpoint):
    timestamp = datetime.datetime.utcnow().isoformat()
    log = {
        "timestamp": timestamp,
        "endpoint": endpoint,
        "env": APP_ENV
    }
    print(log, flush=True)


def check_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("DB_NAME", "infradb"),
            user=os.getenv("DB_USER", "infrauser"),
            password=os.getenv("DB_PASSWORD", "infra123")
        )
        conn.close()
        return "Database: Connected"
    except Exception as e:
        print({
            "error": str(e),
            "type": "db_connection_error"
        }, flush=True)
        return "Database: Not Connected"

@app.route("/")
def home():
    log_request("/")
    return f"""
InfraReady Service<br>
Environment: {APP_ENV}<br>
Version: {APP_VERSION}<br>
{check_db()}
"""


@app.route("/health")
def health():
    log_request("/health")

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("DB_NAME", "infradb"),
            user=os.getenv("DB_USER", "infrauser"),
            password=os.getenv("DB_PASSWORD", "infra123")
        )
        conn.close()
        return {
            "status": "healthy",
            "database": "connected"
        }, 200

    except Exception as e:
        print({
            "error": str(e),
            "type": "healthcheck_failure"
        }, flush=True)

        return {
            "status": "unhealthy",
            "database": "disconnected"
        }, 500 #changed


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)