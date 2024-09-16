### Python Setup (django_be)
**Install Python:**
    - Download and install Python 3.12 from [Python Official Downloads](https://www.python.org/downloads/).
    - Clone the repository to create a "Querify" folder.
    - Inside the "Querify" folder, create a virtual environment: `python -m venv ../env`.
    - Activate the virtual environment:
        - Command Prompt: `call ..\env\Scripts\activate.bat`
        - Git Bash: `../env/Scripts/activate.bat`
    - Install required Python packages: `pip install -r requirements.txt`.

**Superuser**
When you want to set up a superuser/ admin
 - py manage.py createsuperuser (to create superuser) 
 - current admin details: [username: admin@djackets.com, email: admin@jackets.com, password: IoTpass1])

**Changes to code**
Do the following commands when you make changes to the Django code:

```py manage.py makemigrations```
```py manage.py migrate```


**Start development server**
```py manage.py runserver```


**Example urls for database**
 - http://127.0.0.1:8000/api/v1/check-free-box/
 - http://127.0.0.1:8000/api/v1/latest-products/1A/
 - http://127.0.0.1:8000/api/v1/boxes/1A2/product/


# Website

## Setting IP adress
Be sure to change the ip adresses to the correct ones in dblib

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
