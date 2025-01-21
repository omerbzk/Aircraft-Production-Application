# Aircraft Production System

This project is a web application developed to manage the aircraft production process. The application manages aircraft types, parts, aircraft, personnel, and teams. This system is designed to make the production process more efficient and organized.

## Project Functionality and Purpose

The Aircraft Production System provides a comprehensive solution for managing the aircraft production process. This system makes it easy to manage all components and personnel involved in the production process. The main purpose of the project is to monitor, manage, and optimize the production process.

## Features

- **Aircraft Types Management**: Add, edit, and manage different aircraft types.
- **Parts Management**: Add, edit, and manage aircraft parts.
- **Aircraft Management**: Add, edit, and manage produced aircraft.
- **Personnel Management**: Add, edit, and manage personnel involved in the production process.
- **Team Management**: Add, edit, and manage different teams.
- **User Authorization and Authentication**: Allow users to log in and be authorized in the system.

## Installation

### Requirements

- Docker
- Docker Compose

### Step 1: Clone the Repository
```sh
git clone https://github.com/omerbzk/Aircraft-Production-Application.git
cd aircraft-production-system
```

### Step 2: Start Services with Docker Compose
```sh
docker-compose up --build
```
### Step 3: Apply Database Migrations
Run the following commands inside the Docker container to apply database migrations:
```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Step 4: Create a Superuser
Run the following command inside the Docker container to create a superuser:
```sh
docker-compose exec web python manage.py createsuperuser
```

### Step 5: Start the Development Server
The development server will already be started with Docker Compose. Open your browser and go to http://127.0.0.1:8000 to start using the application.

Usage
Admin Panel
To access the admin panel, go to http://127.0.0.1:8000/admin in your browser and log in with your superuser credentials. From the admin panel, you can manage aircraft types, parts, aircraft, personnel, and teams.

Admin Panel Features
Aircraft Types Management: Add, edit, and delete aircraft types.
Parts Management: Add, edit, and delete parts.
Aircraft Management: Add, edit, and delete aircraft.
Personnel Management: Add, edit, and delete personnel.
Team Management: Add, edit, and delete teams.
User Panel
To access the user panel, go to http://127.0.0.1:8000 in your browser and log in with your user credentials. From the user panel, you can view and manage aircraft types, parts, aircraft, personnel, and teams.

User Panel Features
Aircraft Types Management: List and view details of aircraft types.
Parts Management: List and view details of parts.
Aircraft Management: List and view details of aircraft.
Personnel Management: List and view details of personnel.
Team Management: List and view details of teams.
Contributing
If you would like to contribute, please send a pull request or open an issue.

### Docker Compose File (docker-compose.yml)

Below is an example `docker-compose.yml` file for your project:

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=aircraft_production
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DEBUG=1
      - SECRET_KEY=your-secret-key
      - DB_NAME=aircraft_production
      - DB_USER=postgres
      - DB_PASSWORD=postgres
      - DB_HOST=db
      - DB_PORT=5432
      - DJANGO_SETTINGS_MODULE=aircraft_production.settings
    working_dir: /app

volumes:
  postgres_data:
```
This README.md file and docker-compose.yml file provide the necessary steps and commands to set up and run your project using Docker. Add these files to the root directory of your project to help users easily set up and use the project. If you need to add more information, please let me know.
