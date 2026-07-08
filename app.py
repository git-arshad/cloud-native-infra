from flask import Flask, Response
from prometheus_client import Counter, generate_latest
import os
import datetime
import psycopg2
import time

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)

app = Flask(__name__)

# Application Configuration
APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
PORT = int(os.getenv("PORT", 5000))

# Database Configuration
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "infradb")
DB_USER = os.getenv("DB_USER", "infrauser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "infra123")


def log_request(endpoint):
    timestamp = datetime.datetime.utcnow().isoformat()
    log = {
        "timestamp": timestamp,
        "endpoint": endpoint,
        "env": APP_ENV
    }
    print(log, flush=True)


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def check_db():
    retries = 3
    delay = 2

    for attempt in range(retries):
        try:
            conn = get_db_connection()
            conn.close()
            return "Database: Connected"

        except Exception as e:
            print({
                "error": str(e),
                "attempt": attempt + 1,
                "type": "db_retry"
            }, flush=True)

            time.sleep(delay)

    return "Database: Not Connected (after retries)"


@app.route("/")
def home():
    REQUEST_COUNT.inc()

    log_request("/")

    return f"""
    InfraReady Service<br>
    Environment: {APP_ENV}<br>
    Version: {APP_VERSION}<br>
    {check_db()}
    """


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype="text/plain"
    )


# Liveness Probe
@app.route("/live")
def live():
    log_request("/live")

    return {
        "status": "alive"
    }, 200


# Readiness Probe
@app.route("/ready")
def ready():

    log_request("/ready")

    try:
        conn = get_db_connection()
        conn.close()

        return {
            "status": "ready",
            "database": "connected"
        }, 200

    except Exception as e:
        print({
            "error": str(e),
            "type": "readiness_failure"
        }, flush=True)

        return {
            "status": "not ready",
            "database": "disconnected"
        }, 503


# General Health Endpoint
@app.route("/health")
def health():

    log_request("/health")

    try:
        conn = get_db_connection()
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
        }, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)