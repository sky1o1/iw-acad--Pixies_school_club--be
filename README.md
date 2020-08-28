Pixies School Club
===
This project is an online platform that eases the activities of the Clubs of any college by partially shifting its activities online.

This project was created using Django and Django Rest Framework.

Full documentation for the Django project is available at https://docs.djangoproject.com/en/3.1/.

Full documentation for the DRF project is available at https://www.django-rest-framework.org/.

Team member : 
===

Aakash Dangol : aakash.dangol101@gmail.com

Abishek bhattarai : absekbhattarai@gmail.com

Megha Shrestha : meghashrestha30@gmail.com

Requirements
===
Python (3.5, 3.6, 3.7)

Django	3.0.8	

Pillow	7.2.0

asgiref	3.2.10

djangorestframework	3.11.0

pip	20.1.1	

pytz	2020.1

setuptools	49.2.0	

sqlparse	0.3.1	

We highly recommend and only officially support the latest patch release of each Python and Django series.

Installation
===
Install using pip...

Installing Django
`pip install Django==3.1`

Installing Django Rest Framework
`pip install djangorestframework`

Installing Virtual Environment
`pip3 install virtualenv`

Activating Virtual Environment on Linux/Mac
`. my_env_name/bin/activate`

Activating Virtual Environment on Windows
`my_env_name\Scripts\activate`

Add 'rest_framework' to your INSTALLED_APPS setting.

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
Installing Pillow
`$ pip install Pillow`

Installing Cors headers
`pip install django-cors-headers `

Add corsheaders to installed applications in settings.py

```
INSTALLED_APPS = [
    ...
    'corsheaders',
]
```
Add corsheaders.middleware.CorsMiddleware to middleware section in settings.py
```
  'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...

]
```


Make Migrations and Migrate the Models
`python manage.py makemigrations`

`python manage.py migrate`

Running the server
`python manage.py runserver`
