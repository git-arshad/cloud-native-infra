🚀 Flask + PostgreSQL — Dockerized Infrastructure
This project showcases a production‑style containerized application built with Flask as the Python backend and PostgreSQL as the database, all orchestrated through Docker and Docker Compose. It’s designed to highlight the differences between stateful and stateless services, container networking, resilience, and how infrastructure behaves under failure conditions.

🏗 Architecture
The flow is simple: a user interacts with the Flask application, which runs inside its own container and connects to PostgreSQL through Docker’s internal DNS (using the service name db). All data is stored in Docker volumes, ensuring persistence even if containers are deleted. Both services run on the same Docker network, automatically created by Compose, which makes communication seamless.

📂 Project Structure
The repository is organized with a clear structure:
- app.py — Flask application code
- requirements.txt — Python dependencies
- Dockerfile — Image definition for the Flask app
- docker-compose.yml — Multi‑service orchestration
- README.md — Documentation and usage guide

⚙️ Running the Project
To start the stack, simply run:
docker compose up --build

And to stop it:
docker compose down


🧠 Key Concepts
Several important infrastructure concepts are demonstrated here:
- Container Networking: Services communicate using names like db, thanks to Docker’s internal DNS.
- Persistence with Volumes: Database data is stored in volumes, surviving container deletion unless the volume itself is removed.
- Healthchecks: Configured in docker-compose.yml, they track service states (starting, healthy, unhealthy) and can be verified with docker ps.
- Restart Policies: Containers are set to restart automatically on crashes (restart: always), ensuring resilience.
🔥 Failure Testing
The project also explores failure scenarios:
- Stopping a container → It restarts automatically due to the restart policy.
- Deleting a container → It does not restart, since restart policies only apply to existing containers.
- Database DNS failure → The app throws errors like “could not translate host name ‘db’”, revealing how critical Docker networking is.
📊 What This Demonstrates
Through these experiments, the project illustrates that containers are temporary, volumes make data permanent, restart policies handle crashes but not deletions, and Compose provides automatic networking. It also emphasizes resilience through exception handling and clarifies the distinction between images and containers.
🚀 Future Improvements
Potential next steps include adding retry logic for database connections, implementing a wait‑for‑db startup script, introducing an Nginx reverse proxy, setting up CI/CD pipelines, deploying to cloud platforms (AWS, Azure, GCP), and eventually building a Kubernetes version.
🎯 Learning Outcome
By working through this setup, you gain practical insight into stateful vs. stateless services, Docker networking, container lifecycles, infrastructure as code, failure handling, and production‑ready patterns.