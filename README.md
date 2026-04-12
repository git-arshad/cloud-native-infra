🚀 Cloud-Based Backend System

This project is a simple backend system that I built to understand how real applications are deployed and run on the cloud.

Instead of just running code locally, this system runs on a remote server and is accessible over the internet.

🧠 What This Project Does
Runs a backend application using Flask
Connects to a PostgreSQL database
Uses Docker to manage both services
Is deployed on a cloud server
Automatically updates when new code is pushed

The main goal was to learn how systems work in real environments, not just how to write code.

🏗 How It Works
User → Internet → Cloud Server
                     ↓
                Docker
              /        \
        Flask App   PostgreSQL
The Flask app handles requests
The database runs separately and stores data
Both communicate inside a Docker network


⚙️ Tech Used
Python (Flask)
PostgreSQL
Docker & Docker Compose
AWS EC2 (cloud server)
GitHub Actions (for automation)


🚀 How to Run It
Run locally
docker compose up -d --build
Open:
http://localhost:5000


Run on cloud
After deployment, access using:
http://<your-public-ip>:5000


🔁 Automatic Deployment (CI/CD)
Once everything is set up:

You push code to GitHub
GitHub Actions runs automatically
The server updates itself
No manual deployment needed.


📊 What I Focused On
This project is not about building features.
It focuses on:
How services communicate
How systems behave when something fails
How to deploy and update applications
How to observe logs and debug issues


🛠 Features Implemented
Multi-service setup (App + Database)
Containerized using Docker
Cloud deployment using EC2
Automatic deployment (CI/CD)
Basic logging and health checks
Retry logic for handling failures


⚠️ Limitations (What’s Missing)
This is not a full production system yet.

Missing things like:

HTTPS
Monitoring dashboards
Load balancing
Multiple servers (scaling)

🧠 What I Learned
How to run applications outside my local machine
How Docker helps manage services
How cloud servers work
How deployments can be automated
How to debug systems using logs