## SALLY AWWARDS

## Author

Nancy Kemunto

## Description

This application will allow a user to post a project he/she has created and get it reviewed by his/her peers.

As a user of the web application you will be able to:

1.Sign up and log in
2.View projects submitted by other users
3.Submit your projects
4.Rate a project
5.Edit your profile
6.Generate APIs
7.Review a projects

## Getting started
## Prerequisites
python3.8
virtual environment
pip
Clone the Repo and rename it to suit your needs.
git clone https://https://github.com/nancy88199488/sally-awwards
Initialize git and add the remote repository
git init
git remote add origin <your-repository-url>
Create and activate the virtual environment
python3.6 -m virtualenv virtual
source virtual/bin/activate
Setting up environment variables
Create a .env file and paste paste the following filling where appropriate:

SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='awwards'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
Install dependancies
Install dependancies that will create an environment for the app to run pip install -r requirements.txt

Make and run migrations
python3.6 manage.py check
python manage.py makemigrations projects
python3.6 manage.py sqlmigrate projects 0001
python3.6 manage.py migrate
Run the app
python3.6 manage.py runserver
Open localhost:8000

You need to have git installed You can install it with the following command in your terminal `$ sudo apt install git-all`

##  Setup Instructions

Clone Project to your machine
Activate a virtual environment on terminal: source virtual/bin/activate
Install all the requirements found in requirements file.
On your terminal run python3.6 manage.py runserver
Access the live site using the local host provided

## Testing the Application
python manage.py test projects

##  Technologies Used

* Python
* Django

##  Contacts

Email:nancykemuntosalome@gmail.com

##  License

This project is under the [MIT] (LICENSE) license

Copyright (c) 2021. Nancy Kemunto 




