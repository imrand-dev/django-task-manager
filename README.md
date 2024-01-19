<div align="center">
<h2>Task Manager REST APIs</h2>

<img src="https://img.shields.io/badge/Python 3.12-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Django 5.0.1-092E20?style=for-the-badge&logo=django&logoColor=green">
<img src="https://img.shields.io/badge/REST Framework 3.14.0-092E20?style=for-the-badge&logo=django&logoColor=red">

</div>

## Tools I used

* Frontend - HTML, CSS, Bootstrap
* Backend - Python 3.12, Django=5.0.1, Django Rest Framework= 3.14.0
* Database - PostgreSQL
* API Authentication - djangorestframework-simplejwt
* Version Management - Git
* API Schema - drf-spectacular
* Formatter & linter - black, flake8

## Home page

![home-page](https://i.ibb.co/TRN6DBc/image.png)

## Run locally 

* Clone this repository to your local machine `https://github.com/imrand-dev/django-task-manager.git`.
* Navigate to the project directory `cd django-task-manager`.
* here I used `python 3.12`, if your version is not match with me then you can do the following steps to run this project
    * Edit the `pip file`
        ```py
        [requires]
        python_version = "3.10"
        ```
    * Edit the `pipfile.lock`
        ```
        "requires": {
            "python_version": "3.10"
        },
        ```
* Set up the virtual environment `pip install pipenv` then `pipenv install`.
* Activate the virtual env `pipenv shell`
* Install the project dependencies `pip install -r requirements/dev.txt` (optional).
* Enter the directory `cd task_manager`.
* Rename the file `env.example` to `.env` and fill up all the fields
* Migrate the database `python manage.py migrate`.
* Create a superuser account `python manage.py superuser`.
* Run the development server `python manage.py runserver.
* Access the task manager locally by visiting `http://localhost:8000` in your web browser.

## Create database
```
postgresql> create database taskdb;
postgresql> show databases;
postgresql> use taskdb;
``````

## Import Data json

Run the below commands to import json data from `tasks.json`

* `python manage.py loaddata tasks.json`
* `python manage.py makemigrations`
* `python manage.py migrate`

## Login Admin Panel

* Run the server `python manage.py runserver`
* Browse the url `http://127.0.0.1/8000/admin/`
* Log in
    * email `imran@gmail.com` (superuser)
    * password `123456`

## REST APIs

#### Tasks

* Get all tasks `/api/v1/tasks` (authenticated)
* Retrieve/Update/Destroy single task `/api/v1/tasks/task_uid`

#### Photos

* Get all photos `/api/v1/photos` (authenticated)
* Retrieve/Update/Destroy single photo `/api/v1/photos/photo_uid`

#### Login/Signup

* To register a new user hit this url `/users/signup`
    * Fill out all the input forms
    * Then Submit
* To login(credentials) visit `/users/login`
    * Fill out he form
    * you will see `refresh` and `access` token.
* If your access token is expired then visit `/users/api/token-refresh` to regenerate
    * first copy the refresh token from your login credentials.
    * fill the refresh token form and submit.
    * You'll see your new token

### Endpoints Schema

![api-endpoints](https://i.ibb.co/mhzp13d/image.png)