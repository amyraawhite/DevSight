# DevSight

DevSight is a developer observability and infrastructure monitoring platform designed to help engineers monitor services, visualize metrics, and manage application health in real time.

The project is being built as a production-style full-stack application using modern software engineering and DevSecOps practices, including containerization, CI/CD pipelines, and cloud deployment workflows.

---

# Current Features

## Frontend
- React + TypeScript frontend
- Tailwind CSS v4 styling
- Vite development environment

## Backend
- FastAPI backend
- PostgreSQL database integration
- SQLAlchemy ORM setup
- Dockerized database environment

## DevOps
- GitHub Actions CI pipeline
- Docker Compose infrastructure
- Git version control

---

# Tech Stack

## Frontend
- React
- TypeScript
- Vite
- Tailwind CSS v4
- Axios
- React Router DOM

## Backend
- FastAPI
- SQLAlchemy
- Pydantic

## Database
- PostgreSQL

## Infrastructure
- Docker
- Docker Compose
- GitHub Actions

---

# Project Structure

```txt
DevSight/
├── frontend/
├── backend/
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

# Running the Frontend

## Navigate to Frontend

```bash
cd frontend
```

## Install Dependencies

```bash
npm install
```

## Start Development Server

```bash
npm run dev
```

Frontend will run at:

```txt
http://localhost:5173
```

---

# Running the Backend

## Navigate to Backend

```bash
cd backend
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```txt
http://localhost:8000
```

Swagger API documentation:

```txt
http://localhost:8000/docs
```

---

# Running PostgreSQL with Docker

From the project root:

```bash
docker compose up -d
```

Verify running containers:

```bash
docker ps
```

---

# GitHub Actions CI Pipeline

The project includes a CI pipeline that automatically:

- installs frontend dependencies
- builds the frontend
- installs backend dependencies
- validates backend imports

The pipeline runs automatically on:
- pushes to `main`
- pull requests to `main`

---

# Future Roadmap

## Authentication
- JWT authentication
- protected routes
- user registration/login

## Monitoring
- service registration
- uptime monitoring
- heartbeat tracking

## Observability
- metrics dashboards
- WebSocket live updates
- Prometheus integration
- Grafana dashboards

## Deployment
- Dockerized services
- Nginx reverse proxy
- AWS EC2 deployment
- HTTPS support

---

# Development Status

DevSight is currently in Phase 1 of development:
- foundational architecture
- frontend/backend setup
- database integration
- CI/CD setup
```