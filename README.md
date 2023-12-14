# django_be

Execute the below to start the virtual environment: execute activate.bat file
 - C:\> <venv>\Scripts\activate.bat

I had to install the following (maybe not needed again if already installed in virtual environment):
 - pip install virtualenv
 - pip install Django
 - pip install django-rest-framework
 - pip install django-cors-headers (helps with security).
 - pip install Djoser (helps with authentication)

When you want to set up a superuser/ admin
 - py manage.py createsuperuser (to create superuser) 
 - current admin details: [username: admin@djackets.com, email: admin@jackets.com, password: IoTpass1])

Do the following commands when you make changes to the Django code:
 - py manage.py make migrations (create migration files)
 - py manage.py migrate (we have a new database with all these tables).

Start development server (this hosts the database)
 - py manage.py runserver


Website pages you can check:
 - http://127.0.0.1:8000/api/v1/check-free-box/
 - http://127.0.0.1:8000/api/v1/latest-products/1A/
