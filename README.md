# School Management System

A full-stack school administration platform: manages colleges, courses, students, faculty, subjects, timetables, and marksheets, with JWT-authenticated REST APIs and a React admin dashboard.

## Tech stack

**Backend:** Django, Django REST Framework, Simple JWT, Celery + django-celery-beat (scheduled/background tasks), Channels/Daphne (websockets), drf-yasg (API docs), MySQL
**Frontend:** React, CoreUI

## Features

- JWT authentication with a custom user model
- College, course, and subject management
- Student and faculty records
- Marksheet management
- Timetable scheduling
- Auto-generated API docs (Swagger/OpenAPI via drf-yasg)
- Background/scheduled tasks via Celery

## Project structure

```
SchoolManagementSystem/
├── school_react/        # React admin dashboard (CoreUI)
└── SCM/                 # Django backend
    ├── SCM/              # project settings, urls, celery config
    ├── account/          # authentication
    └── s_manage/         # core domain: College, Course, Student, Faculty, Subject, TimeTable, Marksheet
        └── View/          # DRF views per model
```

## Getting started

### Backend

```bash
cd SCM
python -m venv .venv
source .venv/Scripts/activate   # Windows
# source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt

cp .env.example .env   # then fill in your own SECRET_KEY and email credentials

python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd school_react
npm install
npm start
```

## Environment variables

See [`SCM/.env.example`](SCM/.env.example) for the full list (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, SMTP email credentials). Never commit a real `.env` — it's gitignored.

## License

MIT
