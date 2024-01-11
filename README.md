# django_be

Execute the below to start the virtual environment: execute activate.bat file
 - C:\> <venv>\Scripts\activate.bat

I had to install the following (maybe not needed again if already installed in virtual environment):
 - pip install virtualenv
 - pip install Django
 - pip install django-rest-framework
 - pip install django-cors-headers (helps with security).
 - pip install Djoser (helps with authentication)
 - pip install pillow

When you want to set up a superuser/ admin
 - py manage.py createsuperuser (to create superuser) 
 - current admin details: [username: admin@djackets.com, email: admin@jackets.com, password: IoTpass1])

Do the following commands when you make changes to the Django code:
 - py manage.py makemigrations (create migration files)
 - py manage.py migrate (we have a new database with all these tables).

Start development server (this hosts the database)
 - py manage.py runserver


Website pages you can check:
 - http://127.0.0.1:8000/api/v1/check-free-box/
 - http://127.0.0.1:8000/api/v1/latest-products/1A/
 - http://127.0.0.1:8000/api/v1/boxes/1A2/product/


# Website

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```
The website is then accessible on port 8080


### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
