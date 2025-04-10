# Student Dashboard System

![Python](https://img.shields.io/badge/python-3.8+-blue.svg) ![Django](https://img.shields.io/badge/django-4.0+-green.svg) ![Bootstrap](https://img.shields.io/badge/bootstrap-5.0+-purple.svg)

## Overview
A Django-based learning management system with dual interfaces:
- **Students**: Track course progress
- **Admins**: Manage courses and monitor students

## ✨ Features
| Student Features | Admin Features |
|----------------|----------------|
| View enrolled courses | Create/edit/delete courses |
| Track progress visually | View all student enrollments |
| Course enrollment system | Monitor class-wide progress |

## 🛠️ Installation
```bash
# Clone and setup
git clone https://github.com/Apurvastha/Student_Dashboard.git
cd student-dashboard

# Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install & run
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver