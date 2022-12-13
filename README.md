# Basic Django CRUD Application
## Instructions - Dev
- Initialize a virtual environment with Django installed: `python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt`
- To create a project: `django-admin startproject project_name`
- To create an application within the project: `cd project_name && python manage.py startapp app_name`
- To start the server: `python manage.py runserver`
- Migrate (create db with default tables for admin purposes): `python manage.py makemigrations && python manage.py migrate`
- Create admin: `python manage.py createsuperuser`
- To head to the admin page: `localhost:8000/admin`

## SQL Models and Migrations
Once a data model is created, migrate the changes and generate the SQL queries to create tables: `python manage.py makemigrations && python manage.py sqlmigrate blog 0001 && python manage.py migrate`. Notice the 0001, this comes from the blog/migrations folder where we see the generated model code with the file name `0001_initial.py`.

## Django ORM
Useful queries:
- User.objects.all()
- User.objects.first()
- User.objects.last()
- User.objects.filter(username="...") (returns query set)
- User.objects.filter(username="...").first() (returns a single User object)
- new_user = User(...set fields), then: new_user.save()
- user_posts = user.post_set.all(), this returns all posts associated with the user object