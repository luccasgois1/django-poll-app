# Poll App developed in Django: django-poll-app

This repository was developed as a study based on https://docs.djangoproject.com/en/4.2/intro/tutorial01/ 

## Enviroment used to develop this repository

* OS: Windows 11 22H1
* Python: 3.11.0
* PIP: 23.2.1
* Django: 4.2.4

## Setup environment to run the application

### 1. Create a python virtual environment

`python -m venv .venv`

### 2. Activate virtual environment for python

Each time you start a new command prompt, you’ll need to activate the environment again.

Run the follow command: 

`.\.venv\Scripts\activate.bat`

### 3. Install Django on python virtual environment

You need to run step 2 first to activate the virtual enviroment. Otherwise you will be installing this package in your local python.

Run the follow command: 

`python -m pip install Django`


## Changing ip or port that server will run

### If you want to run the server on a different port run the follow command:

`python mysite\manage.py runserver <port_number>`

e.g. python mysite\manage.py runserver 8080

### If you want to run the server on a different port and a different ip address run the follow command:

`python mysite\manage.py runserver <ip_address>:<port_number>`

e.g. python mysite\manage.py runserver 0.0.0.0:8000