# Django ToDo App

A simple and elegant ToDo application built with Django, featuring a RESTful API, task management (CRUD), user authentication, and asynchronous task processing with Celery and Redis. Ready for development, staging, and production environments using Docker and Docker Compose.

---

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Configuration](#configuration)
* [Running with Docker](#running-with-docker)
* [Deployment](#deployment)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* **User Authentication**: Sign up, log in, and manage your own tasks securely.
* **CRUD Operations**: Create, view, update, and delete tasks via web UI and REST API.
* **Asynchronous Processing**: Offload periodic and long-running tasks (e.g., sending email reminders) to Celery workers.
* **Redis Integration**: Use Redis as the message broker and (optional) cache.
* **Dockerized Environments**: One command setup for development, staging, or production using Docker Compose.
* **Health Checks**: Built-in health checks for the web service.

---

## Tech Stack

* **Backend**: Python, Django, Django REST Framework
* **Async**: Celery, Redis
* **Web Server**: Gunicorn
* **Proxy**: Nginx
* **Containers**: Docker, Docker Compose (dev, staging, production)
* **Database**: SQLite (for development), PostgreSQL (recommended for production)

---

## Prerequisites

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mehdi-msv/Django-ToDo-App.git
cd Django-ToDo-App
```

### 2. Environment Variables

Copy the example environment file and set your own values:

```bash
cp .env.example .env
# Edit .env to configure SECRET_KEY, DEBUG, database credentials, etc.
```

### 3. Install Python dependencies (optional)

If you prefer running locally without Docker:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Apply Migrations (Only if not using Docker)

```bash
python manage.py makemigrations
python manage.py migrate
```

> If you're using Docker, migrations are handled automatically during container setup.

---

## Usage

### Local Development (without Docker)

```bash
python manage.py runserver
```

Access the web app at `http://127.0.0.1:8000/` and the API at `http://127.0.0.1:8000/api/`.

### Running Celery Worker & Beat

```bash
# Run Redis separately
celery -A core worker -l info
celery -A core beat -l info
```

---

## Project Structure

```text
├── core/
│   ├── accounts/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── apps.py
│   │   ├── tests.py
│   │   └── api/v1/
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── core/
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── logging_config.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── settings/
│   │       ├── base.py
│   │       ├── development.py
│   │       └── production.py
│   ├── todo/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── scheduler.py
│   │   ├── tasks.py
|   |   ├── management/
|   |   |   └── commands/
|   |   |       ├── prepare_app.py
│   │   |       └── create_task.py
│   │   └── api/v1/
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── weather/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── apps.py
│   │   ├── tests.py
│   │   └── serializers.py
│   ├── templates/
│   │   ├── accounts/
│   │   │   └── register.html
│   │   └── todo/
│   │       ├── task_update.html
│   │       └── tasks_list.html
│   ├── static/
│   ├── statics/
│   ├── logs/
│   ├── .flake8
│   ├── manage.py
│   ├── pytest.ini
│   └── requirements.txt
├── nginx/
│   └── default.conf
├── docker-compose.yml
├── docker-compose-stage.yml
├── docker-compose-prod.yml
├── dockerfile
├── .env.example
├── LICENSE
└── requirements.txt
```

---

## Configuration

* **`.env`**: Environment variables (SECRET\_KEY, DEBUG, DATABASE\_URL)
* **`docker-compose-*.yml`**: Compose files for different environments
* **`nginx/`**: Nginx config (`default.conf`)

---

## Running with Docker

Bring up containers for development:

```bash
docker-compose up --build
```

Services:

* `backend`: Django app served by Gunicorn on port 8000
* `redis`: Redis server on port 6379
* `celery_worker`: Celery worker for async tasks
* `celery_beat`: Celery beat for scheduled tasks

Visit `http://localhost:8000/` in your browser.

---

## Deployment

1. Configure environment variables in `.env`.
2. Use `docker-compose-prod.yml` for production settings.
3. Ensure `DEBUG=False` and proper allowed hosts set in `.env`.
4. Run:

   ```bash
   docker-compose -f docker-compose-prod.yml up -d --build
   ```
5. Point your domain/Nginx to the production container.

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/name`
3. Commit your changes: `git commit -m "feat: add ..."`
4. Push to the branch: `git push origin feature/name`
5. Open a Pull Request

Please follow [PEP8](https://www.python.org/dev/peps/pep-0008/) and include tests where appropriate.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
