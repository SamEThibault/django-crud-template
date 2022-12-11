# Basic Django CRUD Application
## Instructions - Dev
- Initialize a virtual environment with Django installed: `python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt`
- To create a project: `django-admin startproject project_name`
- To create an application within the project: `cd project_name && python manage.py startapp app_name`
- To start the server: `python manage.py runserver`
- Migrate (create db with default tables for admin purposes): `python manage.py makemigrations && python manage.py migrate`
- Create admin: `python manage.py createsuperuser`
- To head to the admin page: `localhost:8000/admin`